import os

def get_input_files_strings():
    input_files_strings = []
    txt_files = []
    files = os.listdir()
    for file in files:
        if file.endswith(".txt"):
            if file in txt_files:
                print(f"Duplicate file found: {file}. Please remove the duplicate.")
            else:
                with open(file, "r") as f:
                    contents = f.read()
                    input_files_strings.append((file, contents))
                txt_files.append(file)
    if len(input_files_strings) == 0:
        print("No input files found.")
    return input_files_strings
