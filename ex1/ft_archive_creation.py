import sys
from typing import IO


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: python3 ft_archive_creation.py <file>")
        return

    filename: str = sys.argv[1]
    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file '{filename}'")

    try:
        f: IO = open(filename, 'r')
        content: str = f.read()
        print(f"\n{content}\n")
        f.close()
        print(f"File '{filename}' closed.\n")
    except Exception as e:
        print(f"Error opening file '{filename}': {e}")
        return

    print("Transform data:")
    transformed: str = ""
    for line in content.splitlines(True):
        if line.endswith('\n'):
            transformed += line[:-1] + "#\n"
        else:
            transformed += line + "#"

    print(f"\n{transformed}\n")

    new_filename: str = input("Enter new file name (or empty): ")
    if not new_filename:
        print("Not saving data.")
    else:
        print(f"Saving data to '{new_filename}'")
        try:
            out_f: IO = open(new_filename, 'w')
            out_f.write(transformed)
            out_f.close()
            print(f"Data saved in file '{new_filename}'.")
        except Exception as e:
            print(f"Error opening file '{new_filename}': {e}")


if __name__ == "__main__":
    main()
