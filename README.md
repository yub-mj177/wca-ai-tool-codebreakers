# wca-ai-tool-codebreakers
cv reviewer ai tool
#  CODEBREAKERS — AI CV Reviewer Tool

> **End of Module Group Project | Artificial Intelligence Course**
> Built with Python + Claude AI | Powered by the Anthropic API

---

##  What This Tool Does

The **AI CV Reviewer** is a command-line Python tool that takes a user's CV as input, sends it to Claude AI using a carefully designed R-T-C-C-O prompt, and returns a structured, expert-level review in seconds — completely free.

It was built to solve a real problem: thousands of qualified Kenyan job seekers are filtered out before interviews simply because they have never received professional feedback on their CV. This tool changes that.

**Every review returns four sections:**

| Section | What It Contains |
|---|---|
|  Strengths | What the CV already does well |
|  Weaknesses | What is holding the candidate back |
|  Suggested Improvements | Specific, actionable changes to make |
|  Overall Score | A score out of 10 with a one-sentence explanation |

---

##  Group Members

| Name | GitHub | Role |
|---|---|---|
| Wangari Christine  | [@wangari262](https://github.com/wangari262) | Project Setup & User Input (`user_input.py`) |
| Lornah Muchiri | [@lornah2008](https://github.com/lornah2008) | Prompt Design & API Call (`ai_engine.py`) |
| Ian Gachengo | [@blackmilk](https://github.com/blackmilkx) | Output Display & Save (`output_handler.py`) |
| Mangale Ngome | [@yub-mj177](https://github.com/yub-mj177) | Main Script & Report Lead (`main.py`) |

---

##  File Structure

```
wca-ai-tool-[GroupName]/
│
├── main.py              ← Entry point — runs the full tool (Member 4)
├── user_input.py        ← User input, validation, file loading (Member 1)
├── ai_engine.py         ← R-T-C-C-O prompt builder & API call (Member 2)
├── output_handler.py    ← Display, .txt save, JSON export (Member 3)
├── requirements.txt     ← Python dependencies (anthropic)
└── README.md            ← This file
```

---

##  How to Run the Tool

### Step 1 — Clone the repository

```bash
git clone https://github.com/yub-mj177/wca-ai-tool-codebreakers.git
cd wca-ai-tool-codebreakers
```

### Step 2 — Install dependencies

```bash
pip install -r requirements.txt
```

### Step 3 — Set your Anthropic API key



**On Windows:**
```bash
set ANTHROPIC_API_KEY=sk-ant-api03-your-key-here
```


### Step 4 — Run the tool

```bash
python main.py
```

### Step 5 — Follow the prompts

```
============================================================
       Codebreakers — AI CV REVIEWER TOOL
       Powered by Claude AI | Group Project
============================================================

How would you like to provide your CV?
  1. Paste text directly
  2. Load from a .txt file

Enter 1 or 2: _
```

Paste or load your CV, wait a few seconds, and your review appears.

---

##  How the AI Prompt Works — R-T-C-C-O Framework

We designed our AI instruction using the **R-T-C-C-O framework** — a structured method for writing reliable, high-quality AI prompts.

| Letter | Component | What We Used |
|---|---|---|
| **R** | Role | Senior HR professional with 15 years reviewing CVs for Kenyan employers |
| **T** | Task | Review the CV for strengths, weaknesses, and actionable improvements |
| **C** | Context | Entry-to-mid level roles in the Kenyan job market |
| **C** | Constraints | Under 400 words, bullet points only, specific and encouraging |
| **O** | Output Format | Four fixed sections with emoji headers + overall score out of 10 |

---

##  How the Tool Flows

```
python main.py
      │
      ▼
[1] Get API Key  > os.environ / manual input
      │
      ▼
[2] Get CV Text  > user_input.py
      │  (paste or load from file)
      ▼
[3] Build Prompt  > ai_engine.py
      │  (insert CV into R-T-C-C-O template)
      ▼
[4] Call Claude API  > ai_engine.py
      │  (Anthropic SDK → claude-opus-4-5)
      ▼
[5] Parse Response  > output_handler.py
      │
      ▼
[6] Display Results  > output_handler.py
      │
      ▼
[7] Save to File?  > .txt or .json
```

---

##  Ethics & Privacy

- **Your CV data is transmitted to Anthropic's API** for processing. We do not store any data ourselves.
- **We never hardcode API keys** — the key is stored in an environment variable only.
- **AI feedback is one perspective** — always supplement with human career advice where possible.
- **Bias note:** Our prompt is specifically designed for the Kenyan job market to avoid applying Western CV norms unfairly.

---

##  Future Improvements

- Web interface (Flask or Streamlit) so users can access via browser
- PDF CV upload support
- Job description matching — compare CV against a specific role
- Swahili language feedback option
- WhatsApp integration for wider accessibility in Kenya

---

##  Dependencies

```
anthropic>=0.25.0
```

Install with:
```bash
pip install -r requirements.txt
```

---

##  License

This project was created for educational purposes as part of the WE CAN Academy Artificial Intelligence Course.

---
