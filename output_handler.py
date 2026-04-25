
# output_handler.py  |  Member 3 — Output Display & Save
# CODEBREAKERS | AI-Powered CV Reviewer Tool
# ─────────────────────────────────────────────────────────────

import json
import os
from datetime import datetime


# ── RESPONSE PARSER ───────────────────────────────────────────
# The API returns a plain text string. This function checks
# the response is valid and prepares it for display.

def parse_response(raw_response):
    """
    Validates and cleans the raw text response from the API.
    Returns the cleaned response string, or None if invalid.
    """

    # Check that a response actually came back
    if not raw_response:
        return None

    # Strip any leading or trailing whitespace
    cleaned = raw_response.strip()

    # Confirm the response has meaningful content (over 50 characters)
    if len(cleaned) < 50:
        return None

    return cleaned


# ── DISPLAY FUNCTION ──────────────────────────────────────────
# Prints the CV review results to the terminal in a clean,
# readable format with clear borders and section spacing.

def display_output(response):
    """
    Formats and prints the AI response neatly in the terminal.
    Takes the parsed response string as input.
    """

    if not response:
        # Inform the user if no usable response came back
        print("\nNo review was returned. Please check your API key and try again.")
        return

    # Top border
    print("\n" + "=" * 60)
    print("              YOUR CV REVIEW RESULTS")
    print("=" * 60 + "\n")

    # Print the response with clean spacing
    print(response)

    # Bottom border
    print("\n" + "=" * 60)
    print("       Review complete — CODEBREAKERS CV Tool")
    print("=" * 60 + "\n")


# ── SAVE TO FILE FUNCTION ─────────────────────────────────────
# Gives the user the option to save their review results
# to a timestamped .txt file for future reference.

def save_output(response):
    """
    Asks the user if they want to save the results.
    If yes, saves the response to a .txt file with a timestamp.
    """

    if not response:
        # Nothing to save if there's no response
        return

    choice = input("Would you like to save your review to a file? (yes / no): ").strip().lower()

    if choice in ["yes", "y"]:

        # Generate a filename using the current date and time
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"cv_review_{timestamp}.txt"

        try:
            # Write the response to the file
            with open(filename, "w", encoding="utf-8") as f:
                f.write("CODEBREAKERS — CV REVIEWER RESULTS\n")
                f.write(f"Generated: {datetime.now().strftime('%d %B %Y at %H:%M')}\n")
                f.write("=" * 60 + "\n\n")
                f.write(response)
                f.write("\n\n" + "=" * 60 + "\n")

            print(f"\nResults saved to: {filename}\n")

        except Exception as e:
            # Inform the user if saving fails (e.g. permission issues)
            print(f"\nCould not save file: {e}\n")

    else:
        # User chose not to save — exit cleanly
        print("\nResults not saved. Thank you for using the CV Reviewer!\n")


# ── EXPORT AS JSON ────────────────────────────────────────────
# Optional: saves the raw response as a structured JSON file.
# Useful for developers or future integrations.

def export_as_json(response):
    """
    Exports the CV review response as a JSON file.
    The JSON includes the timestamp and the full review text.
    """

    if not response:
        return

    # Build a structured dictionary with metadata
    data = {
        "tool": "CODEBREAKERS CV Reviewer",
        "generated_at": datetime.now().isoformat(),
        "review": response
    }

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"cv_review_{timestamp}.json"

    try:
        with open(filename, "w", encoding="utf-8") as f:
            # Write the dictionary to a formatted JSON file
            json.dump(data, f, indent=4, ensure_ascii=False)

        print(f"JSON export saved to: {filename}\n")

    except Exception as e:
        print(f"Could not export JSON: {e}\n")
