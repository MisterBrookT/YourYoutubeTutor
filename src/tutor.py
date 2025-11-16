from typing import List, Dict
import json
from src.utils.call_llm import call_llm
from prompts.explain import build_tutor_prompt
from src.utils.io import extract_json_from_markdown

class Tutor:
    """
    Interactive tutor that processes YouTube transcripts and provides explanations.
    """

    def __init__(self):
        """
        Initialize the Tutor.
        """
        pass

    @staticmethod
    def explain(transcript: List[Dict]) -> List[Dict]:
        """Explain, teach sentences using LLM."""
        enriched_list = []

        for i, unit in enumerate(transcript):
            sentence = unit["text"]
            print(f"Processing sentence {i}: {sentence}")
            prompt = build_tutor_prompt(sentence)
            explanation_raw = call_llm(prompt)
            # Extract JSON from markdown and parse it into a dict
            explanation_json_str = extract_json_from_markdown(explanation_raw)
            explanation = json.loads(explanation_json_str)
            enriched = {
                "text": sentence,
                "start": unit["start"],
                "duration": unit["duration"],
                "explanation": explanation
            }
            enriched_list.append(enriched)
            if i == 1:
                break
        return enriched_list
