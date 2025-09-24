from transformers import pipeline
import numpy as np

scorer = pipeline("text-classification", model="distilbert-base-uncased")  # Or fine-tune for scoring

import requests

def score_text(text: str, criteria: list[dict]) -> tuple[dict, float]:
    scores = {}
    total = 0
    for crit in criteria:
        prompt = f"Evaluate this text: '{text}' against criterion '{crit['desc']}'. Assign a score from 0 to {crit['max']}. Respond only with the score number."
        response = requests.post("http://localhost:11434/api/generate", json={"model": "llama3:8b", "prompt": prompt})
        score = float(response.json()["response"].strip())  # Parse the numeric output
        scores[crit['criterion']] = score
        total += score
    return scores, total / len(criteria)