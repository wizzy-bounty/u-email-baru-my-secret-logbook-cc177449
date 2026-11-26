import os

ENTRY = "Day 9: he said, 'Don't write this down,' then spelled the password twice."


def write_entry(entry_path):
    with open(entry_path, "w", encoding="utf-8", newline="") as entry_file:
        entry_file.write(ENTRY)


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    entry_path = os.path.join(output_dir, "entry.txt")
    write_entry(entry_path)


if __name__ == "__main__":
    main()
