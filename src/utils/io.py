# read list of json
from typing import List, Dict
import json
import re
from pathlib import Path

def read_json(file_path: Path | str) -> List[Dict]:
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)


def extract_json_from_markdown(text):
    # Match ```json ... ``` or ``` ... ```
    match = re.search(r"```(?:json)?\s*(\{.*?\})\s*```", text, re.DOTALL)
    if match:
        return match.group(1)
    return text