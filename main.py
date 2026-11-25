import os

ERROR_LINE = "ERROR: I toasted your bread twice. It asked me to stop. I cannot stop. I am a toaster."

MIN_CHARS = 1
MAX_CHARS = 120
OUTPUT_NAME = "entry.txt"


def validate_line(line):
    if not (MIN_CHARS <= len(line) <= MAX_CHARS):
        raise ValueError("line must be %d-%d chars, got %d" % (MIN_CHARS, MAX_CHARS, len(line)))
    if "\n" in line or "\r" in line:
        raise ValueError("line must be a single line")
    if not line.strip():
        raise ValueError("line must not be only whitespace")


def write_entry(line, out_dir):
    validate_line(line)
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, OUTPUT_NAME), "w", encoding="utf-8") as f:
        f.write(line)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    write_entry(ERROR_LINE, out_dir)


if __name__ == "__main__":
    main()
