from typing import List, Dict, Any

def build_tutor_prompt(sentence: str) -> str:
    """
    Build the user prompt for the LLM given one sentence from the transcript.
    """
    return f"""
You are an English tutor helping a Chinese learner understand real spoken English.

Given the following sentence from a YouTube conversation, do three things:

1. Explain the sentence in simple Chinese (1–2 sentences).
2. List 3–6 useful words or phrases with:
   - the original word/phrase
   - a brief Chinese meaning

Sentence:
\"\"\"{sentence.strip()}\"\"\"

Respond in this JSON structure (no extra text):

{{
  "cn_explanation": "...",
  "vocabulary": [
    {{"phrase": "...", "meaning_zh": "..."}}
  ],
}}
""".strip()