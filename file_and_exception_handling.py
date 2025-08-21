# file_handling_assignment.py
# Assignment: File Handling & Exception Handling
# Outcomes: Learn how to read/write files and handle errors gracefully

def file_read_write():
    """
    Reads content from 'input.txt', modifies it, and writes to 'output.txt'.
    """
    try:
        with open("input.txt", "r") as infile:
            content = infile.read()

        # Example modification: Convert text to uppercase
        modified_content = content.upper()

        with open("output.txt", "w") as outfile:
            outfile.write(modified_content)

        print("✅ File processed successfully! Output written to output.txt")

    except FileNotFoundError:
        print("❌ Error: 'input.txt' not found. Please create the file and try again.")
    except PermissionError:
        print("❌ Error: Permission denied while accessing 'input.txt' or 'output.txt'.")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")


def error_handling_lab():
    """
    Asks user for a filename and handles errors if it doesn’t exist or can’t be read.
    """
    try:
        filename = input("Enter the filename to read: ")

        with open(filename, "r") as f:
            content = f.read()
            print("📄 File content:\n")
            print(content)

    except FileNotFoundError:
        print("❌ Error: File not found. Please check the filename and try again.")
    except PermissionError:
        print("❌ Error: You don't have permission to read this file.")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")


if __name__ == "__main__":
    print("===== File Handling & Exception Handling Assignment =====")
    print("1. File Read & Write Challenge")
    print("2. Error Handling Lab")
    choice = input("Choose an option (1 or 2): ")

    if choice == "1":
        file_read_write()
    elif choice == "2":
        error_handling_lab()
    else:
        print("❌ Invalid choice. Please select 1 or 2.")
