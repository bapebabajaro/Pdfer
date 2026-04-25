import json
import sys
from pathlib import Path


FORBIDDEN_OPTION_WORDS = ["eftersom", "därför", "på grund av", "korrekt", "fel"]


def fail(message: str) -> None:
    print(f"FAIL: {message}")
    raise SystemExit(1)


def main() -> None:
    if len(sys.argv) != 2:
        fail("Usage: python validate_singapore_item.py <question.json>")

    path = Path(sys.argv[1])
    data = json.loads(path.read_text(encoding="utf-8"))

    for key in ["id", "type", "stem", "options", "correct", "construction_note_en"]:
        if key not in data:
            fail(f"missing required key: {key}")

    options = data["options"]
    if len(options) != 4:
        fail("options must contain exactly 4 entries")

    ids = [o.get("id") for o in options]
    if data["correct"] not in ids:
        fail("correct value does not match any option id")

    labels = [o.get("label", "") for o in options]
    lengths = [len(label) for label in labels]
    median = sorted(lengths)[len(lengths) // 2]
    for opt_id, label, length in zip(ids, labels, lengths):
        if median and abs(length - median) / median > 0.35:
            fail(f"option {opt_id} length is outside 35 percent band")
        lower = label.lower()
        for word in FORBIDDEN_OPTION_WORDS:
            if word in lower:
                fail(f"option {opt_id} contains forbidden explanatory word: {word}")

    note = data["construction_note_en"]
    for phrase in ["Original tests:", "Distractor", "Cognitive dimensions", "Item classification"]:
        if phrase not in note:
            fail(f"construction_note_en missing phrase: {phrase}")

    print("PASS")


if __name__ == "__main__":
    main()

