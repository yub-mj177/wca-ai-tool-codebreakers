# ─────────────────────────────────────────────────────────────
# ai_engine.py  |  Member 2 — Prompt Design & API Call
# CODEBREAKERS | AI-Powered CV Reviewer Tool
# ─────────────────────────────────────────────────────────────

import anthropic


# ── R-T-C-C-O PROMPT  ─────────────────────────────────
# This function constructs the full AI instruction using the
# R-T-C-C-O framework before sending it to the Claude API.

def build_prompt(cv_text):
    """
    Builds the R-T-C-C-O structured prompt by inserting
    the user's CV text. Returns the full prompt string.

    R-T-C-C-O Breakdown:
      R — Role:        Professional CV reviewer / hiring expert
      T — Task:        Analyse the CV for strengths & weaknesses
      C — Context:     Kenyan job market, entry-to-mid level roles
      C — Constraints: Under 400 words, bullet points, structured
      O — Output:      Three labelled sections
    """

    prompt = f"""
ROLE:
You are a senior HR professional and CV coach with 15 years of 
experience reviewing CVs for Kenyan employers across tech, finance, 
and business sectors. You are honest, constructive, and encouraging.

TASK:
Carefully review the CV provided below. Identify what is working 
well, what needs improvement, and give specific actionable advice 
the candidate can use immediately.

CONTEXT:
The candidate is likely applying for entry-to-mid level roles in 
Kenya. Consider Kenyan employer expectations, formatting norms, and 
the local job market when giving your feedback.

CONSTRAINTS:
- Keep the total response under 400 words
- Use bullet points for every section — no long paragraphs
- Be specific — do not give vague advice like "improve your CV"
- Be encouraging even when pointing out weaknesses
- Do not repeat points across sections

OUTPUT FORMAT:
Return your response in exactly this structure:

✅ STRENGTHS
[Bullet points of what is done well]

 WEAKNESSES
[Bullet points of what needs improvement]

 SUGGESTED IMPROVEMENTS
[Bullet points of specific, actionable changes to make]

📊 OVERALL SCORE
Give the CV a score out of 10 and one sentence explaining the score.

---
CV TO REVIEW:
{cv_text}
"""
    return prompt


# ── API CALL FUNCTION ─────────────────────────────────────────
# Sends the constructed prompt to the Claude API and returns
# the text response. Handles connection and API errors cleanly.

def call_ai_api(prompt, api_key):
    """
    Sends the prompt to Claude using the Anthropic Python SDK.
    Takes the prompt string and API key as arguments.
    Returns the response text or None if an error occurs.
    """

    try:
        # Initialise the Anthropic client with the user's API key
        client = anthropic.Anthropic(api_key=api_key)

        print("Connecting to Claude AI — please wait...\n")

        # Send the message to the Claude model
        message = client.messages.create(
            model="claude-opus-4-5",   # Use the latest Claude model
            max_tokens=500,            # Enough tokens for a full review
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        # Extract the text from the first content block in the response
        response_text = message.content[0].text
        return response_text

    except anthropic.AuthenticationError:
        # Triggered when the API key is wrong or missing
        print("Error: Invalid API key. Please check your key and try again.")
        return None

    except anthropic.APIConnectionError:
        # Triggered when there is no internet connection
        print("Error: Could not connect to Claude API. Check your internet connection.")
        return None

    except anthropic.RateLimitError:
        # Triggered when too many requests are sent too quickly
        print("Error: Rate limit reached. Please wait a moment and try again.")
        return None

    except Exception as e:
        # Catch any other unexpected errors
        print(f"Unexpected error: {e}")
        return None