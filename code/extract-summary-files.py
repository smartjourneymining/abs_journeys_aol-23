import re
import sys

def write_to_file(filename, lines):
    with open(filename, 'w') as file:
        for line in lines:
            file.write(line)

def main():
    current_file = None
    current_lines = []

    filename_pattern = re.compile(r"===== ([a-zA-Z0-9._]+) =====")

    for line in sys.stdin:
        match = filename_pattern.match(line.strip())
        if match:
            if current_file is not None:
                write_to_file(current_file, current_lines)
                current_lines = []

            current_file = match.group(1)  # Extract the filename from the matched pattern
        else:
            current_lines.append(line)

    if current_file is not None:
        write_to_file(current_file, current_lines)

if __name__ == '__main__':
    main()
