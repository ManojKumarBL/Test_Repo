import sys

def process_files(input_file, output_file):
    try:
        with open(input_file, 'r') as input_f:
            content = input_f.read()

        processed_content = content.upper()

        with open(output_file, 'w') as output_f:
            output_f.write(processed_content)

    except FileNotFoundError:
        print(f"Error: Input file '{input_file}' not found.")
        sys.exit(1)
    except PermissionError:
        print(f"Error: Permission denied when writing to '{output_file}'.")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python process_files.py <input_file> <output_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    process_files(input_file, output_file)
