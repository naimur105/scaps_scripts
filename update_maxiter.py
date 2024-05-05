import re

def update_maxiter(filename):
    try:
        # Read the file and store its content
        with open(filename, 'r') as file:
            lines = file.readlines()

        # Update the entire line for 'maxiter' if found using regular expressions
        for i, line in enumerate(lines):
            match = re.match(r'(maxiter\s*:\s*)\d+', line)
            if match:
                # Update the entire line to 'maxiter: 1000000'
                lines[i] = re.sub(r'\d+', '1000000', line)

        # Write the updated content back to the file
        with open(filename, 'w') as file:
            file.writelines(lines)

        return f"File '{filename}' updated successfully."

    except FileNotFoundError:
        return f"Error: File '{filename}' not found."

    except Exception as e:
        return f"Error: An unexpected error occurred while updating '{filename}'. Error message: {str(e)}"

if __name__ == "__main__":
    file_names = ["def/temporary top cell definition file.def", "def/temporary bottom cell definition file.def"]

    for file_name in file_names:
        result_message = update_maxiter(file_name)
        print(result_message)

    print("Done")
