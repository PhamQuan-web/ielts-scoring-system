# Standard Protocol: Method Scoring Data Fine-tuning (V7.2)

**Version:** 7.2 (Ultra-Strict / Chain-of-Thought Optimized)
**Objective:** Manually score 6,430 IELTS Speaking samples to create a high-quality "Golden Dataset" for LLM fine-tuning.
**Core Philosophy:** "Analysis BEFORE Verdict" - Force the reasoning process to occur before the final score is decided.

---

## 1. The Workflow (The "All-in-One" Pass)

For each sample, follow this strict sequence:

### Step 1: Validation & Cleaning
*   **Check:** Is this a valid Q&A? (Reject intros, outros, pure feedback).
*   **Clean:** Remove non-answer text (e.g., "Examiner: Now...", timestamps). Keep ONLY candidate speech.
*   **Part Re-classification:** Ignore existing labels. Determine Part (1, 2, or 3) based on content/length.

### Step 2: Deep Analysis (The Thinking Phase)
*   **Scan Evidence:** Metadata, Micro Flaws, Discourse Metrics.
*   **Evaluate Control:** Lexical Risk, Anti-Halo check.
*   **Differential Diagnosis:** Compare against Band Boundary (Why not +1? Why not -1?).

### Step 3: Alignment & Scoring (The Verdict Phase)
*   **Anchor:** Cite official IELTS Descriptor text.
*   **Justify:** Write the "Reasoning" text.
*   **Score:** Assign strict INTEGER Band Scores (1-9).

### Step 4: Video-Level Consistency Check
*   After scoring all samples in a video, compare the **Average Band** vs **Ground Truth Overall Band**.
*   **Rule:** If variance > 1.0 Band -> REVIEW & RE-CALIBRATE.

---

## 2. Advanced Criteria (The "Big 6")

### 1️⃣ Band Boundary Signals (Decision Margin)
*   **Goal:** Teach the model the *marginal* difference between bands.
*   **Requirement:** Must be specific to the context, not generic.
*   **Fields:** `why_not_9` (Constraint), `why_not_7` (Superiority).

### 2️⃣ Lexical Risk & Anti-Halo
*   **Goal:** Prevent "High Score because Idiom".
*   **Logic:** Presence of idiom != Band 9. Usage must be *appropriate* and *sustained*.
*   **Field:** `anti_overrating` (Triggered if idiom exists but control is lacking).

### 3️⃣ Grammar Profile (Complexity vs Control)
*   **Goal:** Separate "Scope of Structures" from "Error Frequency".
*   **Enums:**
    *   `complexity_level`: basic | moderate | high
    *   `accuracy_level`: variable | controlled | high
    *   `flexibility`: limited | moderate | moderate_high | high | sustained

### 4️⃣ Micro Flaws (Negative Evidence)
*   **Goal:** Teach the model to see minute imperfections even in high bands.
*   **Tags:** `stylistic_fragment`, `mild_repetition`, `article_slip`, `connector_overuse`.

### 5️⃣ Discourse Metrics (Part-Dependent)
*   **Goal:** Calibrate scoring based on Part expectation.
*   **Part 1:** Concise, natural, personal. (Long winded != better).
*   **Part 3:** Extended, abstract, well-developed. (Short != better).

### 6️⃣ Examiner Anchor
*   **Goal:** Ground every decision in official text.
*   **Format:** Separated `band` (int) and `text` (string).

---

## 3. The Final JSON Schema (V7.2)

**Note:** Ordered to enforce Chain-of-Thought (Analysis -> Diagnosis -> Verdict).

```json
{
  "id": 0,
  "sample_id": "RBwx5atq-PY_q01",
  "video_id": "RBwx5atq-PY",
  "part": 1,
  "question": "What is your favorite type of food?",
  "transcript": "My favorite type of food...",
  "word_count": 47,

  // --- PHASE 1: EVIDENCE EXTRACTION (Observe) ---
  "analysis_metadata": {
    "grammar_error_patterns": ["stylistic_fragment"],
    "grammar_error_frequency": "rare",
    "vocab_collocation_usage": "idiomatic_natural",
    "vocab_evidence": ["dig deep", "poutines"],
    "grammar_structures_used": ["second_conditional", "topic_fronting"]
  },

  "micro_flaws": {
    "grammar": ["stylistic_fragment"],
    "vocabulary": ["mild_repetition"]
  },

  "vocab_control": {
    "appropriateness": "accurate",
    "risk_level": "moderate",
    "overextension": false
  },

  "anti_overrating": {
    "triggered": true,
    "reason": "Uses idiomatic language ('dig deep') but relies on repetition of basic nouns ('food'), limiting the range."
  },

  "grammar_profile": {
    "complexity_level": "moderate_high",
    "accuracy_level": "high",
    "flexibility": "moderate_high",
    "error_density": "rare"
  },

  "discourse_metrics": {
    "length_appropriateness": "optimal",
    "redundancy": "low",
    "development_depth": "adequate_for_part_1"
  },

  // --- PHASE 2: DIFFERENTIAL DIAGNOSIS (Compare) ---
  "band_boundary": {
    "grammar": {
      "why_not_9": "Lacks the sustained, sophisticated control of complex features required for Band 9; relies on stylistic fragments rather than full cohesive structures.",
      "why_not_7": "Structures are error-free and usage of complex conditional ('If I really had to...') is more natural and accurate than typical Band 7."
    },
    "vocabulary": {
      "why_not_9": "Repetition of basic keywords ('food', 'favorite') prevents Band 9 claim of 'total flexibility' and 'sustained precision'.",
      "why_not_7": "Uses idiomatic language ('dig deep') and specific terms ('poutines') with greater precision and naturalness than Band 7."
    }
  },

  // --- PHASE 3: ALIGNMENT & REASONING (Synthesize) ---
  "ielts_descriptor_alignment": {
    "grammar_band": 8,
    "grammar_text": "The majority of sentences are error free. Occasional inappropriacies occur.",
    "vocabulary_band": 8,
    "vocabulary_text": "Skilful use of less common and idiomatic items despite occasional inaccuracies."
  },

  "vocab_reason": "Observation: Uses 'dig deep' and topic-specific 'poutines'. Impact: Meaning is precise and register is natural. Justification: **Skilful use** meets Band 8; **repetition** prevents Band 9.",
  "grammar_reason": "Observation: Uses complex conditional ('If I really had to...'). Impact: Message conveyed without strain. Justification: **Majority error-free sentences** meets Band 8.",

  // --- PHASE 4: FINAL VERDICT (Decide) ---
  "vocabulary": 8,
  "grammar": 8
}
```

---

## 4. Part-Dependent Calibration Rules

| Feature | Part 1 Expectations | Part 3 Expectations |
| :--- | :--- | :--- |
| **Length** | Conversational, concise (2-4 sentences). | Extended, developed (full paragraph). |
| **Register** | Informal, personal is OK ("I guess...", "Well..."). | Formal, abstract, generalized ("It is generally believed..."). |
| **Vocabulary** | Natural collocations, daily life topics. | Abstract nouns, topic-specific jargon. |
| **Response** | Direct answer + 1-2 details. | Answer + Explain + Example + Alternative/Future. |

*Penalty:* applying Part 1 style to Part 3 -> downgrade Band.
*Penalty:* applying Part 3 "speechifying" to Part 1 -> downgrade Naturalness.
