import json
import re
import os
from datetime import datetime

INPUT_FILE = 'training_samples_normalized.json'
OUTPUT_VERIFIED = 'output/samples_verified.json'
OUTPUT_INVALID = 'output/samples_invalid.json'
OUTPUT_SUMMARY = 'output/verification_summary.json'

# Ensure output directory exists
os.makedirs('output', exist_ok=True)

def load_samples(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data['samples']

def is_valid_sample(sample):
    question = sample.get('question', '').lower()
    transcript = sample.get('transcript', '').lower()

    # invalid criteria patterns
    invalid_patterns = {
        'examiner_feedback': [
            r"i gave you a", r"band score", r"score is", r"for your grammar",
            r"for your fluency", r"pronunciation was", r"feedback",
            r"well done", r"good job", r"great job", r"phenomenal job",
            r"nine out of nine", r"seven point five", r"six point five"
        ],
        'instructions': [
            r"part one", r"part two", r"part three", r"get started",
            r"minute to prepare", r"take notes", r"pencil", r"paper",
            r"cue card", r"q card", r"topic card", r"start talking",
            r"stop you there", r"move on to", r"end of the test",
            r"speaking test", r"describe a time", r"i am going to give you a topic",
            r"you have one minute"
        ],
        'meta_communication': [
            r"identification", r"passport", r"id card", r"full name",
            r"call you", r"address you", r"recording", r"check the sound",
            r"can i see your", r"may i see your"
        ],
        'greeting': [
            r"hello", r"good morning", r"good afternoon", r"nice to meet you",
            r"how are you", r"thank you very much"
        ],
        'mixed_speech': [
            # Hard to detect with simple regex, but long questions might indicate this
            # or rapid turn-taking indicators if present.
            # We'll rely on specific phrases often found in mixed/feedback turns.
            r"do you understand\?", r"any questions\?"
        ]
    }

    # Checks

    # 1. Check for Feedback/Meta/Instructions in Question OR Transcript
    for category, patterns in invalid_patterns.items():
        for pattern in patterns:
            if re.search(pattern, question) or re.search(pattern, transcript):
                # Exception: "part of" is common, "part one" is specific.
                # "full name" is in Q1 usually, but instructions say "Meta-communication" includes "Can I see your identification?".
                # "What is your full name" is a valid question?
                # Let's check instructions again. "Greetings: Hello, how are you?".
                # "Meta: Can I see your identification?".
                # "Instructions: Let us get started with Part 1".
                # If question is JUST "What is your full name?", it's arguably valid Part 1.
                # But "Can you tell me your full name please?" often comes with "Can I see your ID?".
                # Let's mark "identification" as definitely invalid.
                # "part one" in transcript is likely invalid (examiner talking).

                # Refinement: Allow "full name" if it's the ONLY thing?
                # Actually, many samples have "Can you tell me your full name" followed by "Can I see your ID".
                # Let's stick to the list.
                return False, category, f"Matched pattern: {pattern}"

    # 2. Check for Length (Incomplete)
    # Transcript with < 5 words is likely just "Yes", "No", "Thank you".
    if len(transcript.split()) < 5:
        return False, 'incomplete', "Transcript too short (< 5 words)"

    # 3. Check for specific "Instruction" phrasing in Question
    # e.g. "I'd like you to talk about..." is Part 2 instruction, not a question-answer pair.
    if "like you to talk about" in question or "give you a topic" in question:
        return False, 'instructions', "Part 2 instruction detected"

    return True, None, None

def main():
    print("Loading samples...")
    samples = load_samples(INPUT_FILE)

    verified_samples = []
    invalid_samples = []
    stats = {
        'examiner_feedback': 0,
        'instructions': 0,
        'greeting': 0,
        'meta_communication': 0,
        'mixed_speech': 0,
        'incomplete': 0
    }

    print(f"Processing {len(samples)} samples...")
    start_time = datetime.now()

    for sample in samples:
        is_valid, reason, note = is_valid_sample(sample)

        if is_valid:
            sample['verification_status'] = 'VALID'
            sample['verification_note'] = 'Passes heuristic checks'
            verified_samples.append(sample)
        else:
            sample['verification_status'] = 'INVALID'
            sample['invalid_reason'] = reason
            sample['verification_note'] = note
            invalid_samples.append(sample)
            if reason in stats:
                stats[reason] += 1
            else:
                # fallback for unknown reason keys if I made a typo
                stats.setdefault(reason, 0)
                stats[reason] += 1

    end_time = datetime.now()
    duration = str(end_time - start_time)

    # Save Verified
    with open(OUTPUT_VERIFIED, 'w', encoding='utf-8') as f:
        json.dump({
            "total": len(verified_samples),
            "verified_at": datetime.now().isoformat(),
            "verified_by": "Jules AI Agent (Script)",
            "samples": verified_samples
        }, f, indent=2)

    # Save Invalid
    with open(OUTPUT_INVALID, 'w', encoding='utf-8') as f:
        json.dump({
            "total": len(invalid_samples),
            "verified_at": datetime.now().isoformat(),
            "verified_by": "Jules AI Agent (Script)",
            "samples": invalid_samples
        }, f, indent=2)

    # Save Summary
    summary = {
        "total_processed": len(samples),
        "total_valid": len(verified_samples),
        "total_invalid": len(invalid_samples),
        "invalid_breakdown": stats,
        "processing_time": duration,
        "completed_at": datetime.now().isoformat()
    }
    with open(OUTPUT_SUMMARY, 'w', encoding='utf-8') as f:
        json.dump(summary, f, indent=2)

    print("Verification complete.")
    print(json.dumps(summary, indent=2))

if __name__ == "__main__":
    main()
