
# CODEBREAKERS | AI-Powered CV Reviewer Tool
#
# HOW TO RUN:
#   1. Install dependencies:   pip install anthropic
#   2. Run the tool:           python main.py
#   3. Follow the prompts to paste or load your CV
#
# WHAT IT DOES:
#   Takes a user's CV as text input, sends it to Claude AI
#   using a structured R-T-C-C-O prompt, and returns a
#   detailed review with strengths, weaknesses, and improvement suggestions.

import os

# Import each team member's module
from user_input import get_user_input          # Member 1
from ai_engine import build_prompt, call_ai_api  # Member 2
from output_handler import (                    # Member 3
    parse_response,
    display_output,
    save_output,
    export_as_json
)


# API KEY SETUP
# The API key is read from an environment variable for security.


def get_api_key():
    """
    Retrieves the Claude API key from the environment variable
    ANTHROPIC_API_KEY. If not set, prompts the user to enter it.
    Returns the API key string.
    """

    # First, try to read from environment variable
    api_key = os.environ.get("ANTHROPIC_API_KEY")

    if not api_key:
        # If not set as environment variable, ask the user directly
        print("No API key found in environment variables.")
        api_key = input("Please enter your Anthropic API key: ").strip()

    if not api_key:
        # Exit if still no key — tool cannot work without it
        print("Error: API key is required to run this tool.")
        exit(1)

    return api_key


# REPEAT OR EXIT 
# After a review, ask the user if they want to review another CV.

def ask_to_repeat():
    """
    Asks the user if they want to run another CV review.
    Returns True to repeat, False to exit.
    """
    choice = input("Would you like to review another CV? (yes / no): ").strip().lower()
    return choice in ["yes", "y"]


# MAIN FUNCTION 
# Ties all modules together and runs the full tool flow.

def main():
    """
    Main entry point for the CV Reviewer tool.
    Runs the full pipeline: input → prompt → API → display → save.
    """

    # Step 1: Get the API key
    api_key = get_api_key()
    print()

    # Loop so user can review multiple CVs in one session
    while True:

        # Step 2: Get the user's CV text (Member 1's function)
        cv_text = get_user_input()

        # Step 3: Build the R-T-C-C-O prompt (Member 2's function)
        prompt = build_prompt(cv_text)

        # Step 4: Send the prompt to Claude API (Member 2's function)
        raw_response = call_ai_api(prompt, api_key)

        # Step 5: Parse the API response (Member 3's function)
        parsed_response = parse_response(raw_response)

        # Step 6: Display the results to the terminal (Member 3's function)
        display_output(parsed_response)

        # Step 7: Offer to save the results as a .txt file (Member 3's function)
        save_output(parsed_response)

        # Step 8: Offer JSON export for developers (Member 3's function)
        export_choice = input("Export results as JSON as well? (yes / no): ").strip().lower()
        if export_choice in ["yes", "y"]:
            export_as_json(parsed_response)

        # Step 9: Ask if user wants to review another CV (Member 4's function)
        print()
        if not ask_to_repeat():
            print("\nThank you for using the CODEBREAKERS CV Reviewer!")
            print("Good luck with your job applications!\n")
            break

        print("\n" + "-" * 60 + "\n")


# ENTRY POINT 
# This block ensures main() only runs when the file is executed
# directly, not when imported as a module by another script.

if __name__ == "__main__":
    main()
