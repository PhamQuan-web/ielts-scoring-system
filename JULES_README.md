# IELTS Sample Verification Project

## Purpose
Verify and classify 7,894 IELTS Speaking samples to ensure data quality for fine-tuning.

## Quick Start for Jules

1. Read `INSTRUCTIONS.md` for detailed verification criteria
2. Process `input/training_samples_normalized.json`
3. Output to `output/` directory

## Command for Jules

```
Verify all samples following INSTRUCTIONS.md criteria.
Classify each sample as VALID (genuine IELTS Q&A) or INVALID (feedback, greetings, instructions, etc).
Create:
- output/samples_verified.json (valid samples)
- output/samples_invalid.json (invalid samples)
- output/verification_summary.json (statistics)
```

## Files

| File | Description |
|------|-------------|
| `INSTRUCTIONS.md` | Detailed verification criteria and examples |
| `input/training_samples_normalized.json` | 7,894 samples to verify |
| `output/samples_verified.json` | Valid samples (Jules creates) |
| `output/samples_invalid.json` | Invalid samples (Jules creates) |
| `output/verification_summary.json` | Statistics (Jules creates) |

## Classification Quick Reference

✅ **VALID**: Examiner question + Candidate answer (real test content)
❌ **INVALID**: Feedback, scores, instructions, greetings, meta-communication

## After Completion

Send output files to Antigravity (Claude) for final review and validation.
