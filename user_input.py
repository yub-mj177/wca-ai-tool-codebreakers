def display_banner():
    """Prints the welcome banner when the tool starts."""
    print("=" * 60)
    print("       CODEBREAKERS — AI CV REVIEWER TOOL")
    print("       Powered by Claude AI ")
    print("=" * 60)
    print()


def get_cv_from_text():
    """
    Prompts the user to paste their CV text directly
    into the terminal. Reads until a blank line is entered.
    Returns the full CV text as a string.
    """
    print("Paste your CV text below.")
    print("Press ENTER twice when you are done.\n")

    lines = []
    while True:
        line = input()
        if line == "":
            # Stop reading when user hits Enter on an empty line
            break
        lines.append(line)

    # Join all lines into one single string
    cv_text = "\n".join(lines)
    return cv_text


def get_cv_from_file():
    """
    Asks the user for a file path and reads the CV from that file.
    Supports .txt files. Returns the file contents as a string.
    """
    file_path = input("Enter the path to your CV file (.txt): ").strip()

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            cv_text = f.read()
        print(f"\nFile '{file_path}' loaded successfully.\n")
        return cv_text

    except FileNotFoundError:
        # Tell user if the file doesn't exist and try again
        print(f"\nError: File '{file_path}' not found. Please check the path.\n")
        return get_cv_from_file()

    except Exception as e:
        print(f"\nError reading file: {e}\n")
        return get_cv_from_file()


def get_user_input():
    """
    Main input function. Asks the user how they want to
    provide their CV — paste it or load from a file.
    Validates that the input is not empty before returning.
    """
    display_banner()

    print("How would you like to provide your CV?")
    print("  1. Paste text directly")
    print("  2. Load from a .txt file")
    print()

    choice = input("Enter 1 or 2: ").strip()

    if choice == "1":
        print()
        cv_text = get_cv_from_text()
    elif choice == "2":
        print()
        cv_text = get_cv_from_file()
    else:
        # If invalid choice, ask again
        print("\nInvalid choice. Please enter 1 or 2.\n")
        return get_user_input()

    # Validate that the CV is not empty
    if not cv_text.strip():
        print("\nNo CV text found. Please try again.\n")
        return get_user_input()

    # Confirm how many words were received
    word_count = len(cv_text.split())
    print(f"\nCV received — {word_count} words loaded.\n")

    return cv_text
