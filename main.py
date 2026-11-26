import os

ENTRY_TEXT = "Experiment 12: hid the snacks from myself. Subject found them in nine minutes and left a thank-you note."
OUTPUT_NAME = "entry.txt"


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, OUTPUT_NAME), "w", encoding="utf-8", newline="") as entry_file:
        entry_file.write(ENTRY_TEXT)


if __name__ == "__main__":
    main()
