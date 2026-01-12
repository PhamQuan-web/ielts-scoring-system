# IELTS Sample Verification Instructions for Jules

## 🎯 OBJECTIVE
Manually review and classify **7,894 IELTS Speaking samples** from `input/training_samples_normalized.json`.

Separate into:
- `output/samples_verified.json` - Valid IELTS test Q&A
- `output/samples_invalid.json` - Invalid samples needing re-extraction

---

## 📋 CLASSIFICATION CRITERIA

### ✅ VALID Sample (keep in verified.json):
A sample is **VALID** if and only if:
1. **Question** = Examiner asking a genuine IELTS Speaking test question
2. **Transcript** = Candidate answering that question

**Examples of VALID samples:**
```json
{
  "question": "What is your favorite type of food?",
  "transcript": "My favorite type of food is Italian cuisine, especially pasta. I love the variety of sauces and the fresh ingredients they use."
}
```

```json
{
  "question": "Do you prefer home-cooked meals or eating out?",
  "transcript": "I prefer home-cooked meals because they are healthier and I can control the ingredients."
}
```

### ❌ INVALID Sample (put in invalid.json):

| Type | Description | Example |
|------|-------------|---------|
| **Examiner Feedback** | Examiner giving scores or comments | "I gave you a 7 for grammar", "You did well today" |
| **Instructions** | Examiner explaining test format | "Let us get started with Part 1", "You have 1 minute to prepare" |
| **Greetings** | Opening/closing pleasantries | "Hello, how are you?", "Thank you, goodbye" |
| **Meta-communication** | Talking about the test itself | "Can I see your identification?", "Here is your paper and pen" |
| **Mixed Speech** | Contains both examiner and candidate talking (unclear who is speaking) | Long transcripts with feedback mixed in |
| **Incomplete** | Very short or meaningless responses | "Yes.", "Okay.", "Thank you." (< 10 words with no content) |

**Examples of INVALID samples:**
```json
{
  "question": "And can I see your identification please?",
  "transcript": "Yeah, here you go. Okay, thank you so much. Then let us get started with part one."
}
// REASON: Meta-communication, not test content
```

```json
{
  "question": "Everyone is third person, so everyone sees them, right?",
  "transcript": "And same goes for your plural as sometimes that is just missing."
}
// REASON: Examiner feedback about grammar errors
```

```json
{
  "question": "I gave you a seven for your grammar, right?",
  "transcript": "So, you know, just always keep an eye on these little things..."
}
// REASON: Examiner giving score and feedback
```

---

## 📥 INPUT FORMAT

File: `input/training_samples_normalized.json`

```json
{
  "total": 7894,
  "normalized": true,
  "samples": [
    {
      "sample_id": "RBwx5atq-PY_q01",
      "video_id": "RBwx5atq-PY",
      "band": 9.0,
      "question": "What is your favorite type of food?",
      "transcript": "My favorite type of food...",
      "part": 1,
      "source": "valid_original",
      "transcript_original": "Um, my favorite type of food..."
    }
  ]
}
```

---

## 📤 OUTPUT FORMAT

### File 1: `output/samples_verified.json`
```json
{
  "total": <number of verified samples>,
  "verified_at": "<ISO timestamp>",
  "verified_by": "Jules AI Agent",
  "samples": [
    {
      "sample_id": "...",
      "video_id": "...",
      "band": 9.0,
      "question": "...",
      "transcript": "...",
      "part": 1,
      "source": "...",
      "transcript_original": "...",
      "verification_status": "VALID",
      "verification_note": "Clear examiner question with candidate response"
    }
  ]
}
```

### File 2: `output/samples_invalid.json`
```json
{
  "total": <number of invalid samples>,
  "verified_at": "<ISO timestamp>",
  "verified_by": "Jules AI Agent",
  "samples": [
    {
      "sample_id": "...",
      "video_id": "...",
      "band": 9.0,
      "question": "...",
      "transcript": "...",
      "part": 1,
      "source": "...",
      "transcript_original": "...",
      "verification_status": "INVALID",
      "invalid_reason": "examiner_feedback|instructions|greeting|meta_communication|mixed_speech|incomplete",
      "verification_note": "Examiner giving feedback about grammar score"
    }
  ]
}
```

---

## 🔄 PROCESSING INSTRUCTIONS

1. **Read** `input/training_samples_normalized.json`
2. **For each sample**, analyze:
   - Is the `question` a genuine IELTS test question from examiner?
   - Is the `transcript` a candidate's answer to that question?
3. **Classify** as VALID or INVALID based on criteria above
4. **Add verification fields**:
   - `verification_status`: "VALID" or "INVALID"
   - `verification_note`: Brief explanation
   - `invalid_reason`: (only for invalid) Category of invalidity
5. **Write** to appropriate output file
6. **Create summary** at the end with statistics

---

## 📊 EXPECTED DELIVERABLES

1. `output/samples_verified.json` - All valid samples
2. `output/samples_invalid.json` - All invalid samples  
3. `output/verification_summary.json`:
```json
{
  "total_processed": 7894,
  "total_valid": <count>,
  "total_invalid": <count>,
  "invalid_breakdown": {
    "examiner_feedback": <count>,
    "instructions": <count>,
    "greeting": <count>,
    "meta_communication": <count>,
    "mixed_speech": <count>,
    "incomplete": <count>
  },
  "processing_time": "<duration>",
  "completed_at": "<ISO timestamp>"
}
```

---

## ⚠️ IMPORTANT NOTES

1. **Be conservative** - If unsure, mark as INVALID (can be manually reviewed later)
2. **Preserve all original fields** - Don't lose any data from input
3. **Add verification metadata** - For traceability
4. **Process ALL 7,894 samples** - Don't skip any
5. **Maintain JSON validity** - Output must be valid parseable JSON

---

## 🚀 START COMMAND

```
Review all samples in input/training_samples_normalized.json.
Classify each as VALID or INVALID based on the criteria in INSTRUCTIONS.md.
Output to output/samples_verified.json and output/samples_invalid.json.
Create output/verification_summary.json with statistics.
```
