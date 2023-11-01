#!/usr/bin/node
def read_and_print_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            print(content)
    except Exception as e:
        print(f"Error occurred: {e}")

# Check if the correct number of arguments is provided
if len(sys.argv) != 2:
    print("Usage: python script_name.py <file_path>")
else:
    file_path = sys.argv[1]
    read_and_print_file(file_path)
