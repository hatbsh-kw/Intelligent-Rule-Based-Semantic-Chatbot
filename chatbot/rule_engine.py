import json
from pathlib import Path

from chatbot.preprocessing import normalize_text


class RuleBasedEngine:
    """
    Rule-based intent recognition engine.

    Uses keywords and phrases defined in data/intents.json
    to identify the most likely user intent.
    """

    def __init__(self, intents_path="data/intents.json"):
        self.intents_path = Path(intents_path)
        self.intents = self._load_intents()

    def _load_intents(self):
        """Load intent definitions from the JSON knowledge base."""
        with self.intents_path.open("r", encoding="utf-8") as file:
            data = json.load(file)

        return data["intents"]

    def detect_intent(self, text):
        """
        Detect an intent using keyword and phrase matching.

        Returns:
            {
                "intent": intent_name or None,
                "confidence": float
            }
        """
        normalized_text = normalize_text(text)

        if not normalized_text:
            return {
                "intent": None,
                "confidence": 0.0
            }

        best_intent = None
        best_score = 0.0

        for intent in self.intents:
            intent_name = intent["name"]

            # Fallback should not actively match user input.
            if intent_name == "fallback":
                continue

            # Include both keywords and example phrases from knowledge base
            patterns = intent.get("keywords", []) + intent.get("examples", [])

            # Normalize all keywords/phrases and remove duplicates.
            normalized_keywords = list(
                dict.fromkeys(
                    normalize_text(keyword)
                    for keyword in patterns
                    if keyword and keyword.strip()
                )
            )

            matched_phrases = []
            matched_keywords = []

            for keyword in normalized_keywords:
                # Phrase matching
                if " " in keyword and keyword in normalized_text:
                    matched_phrases.append(keyword)

                # Single keyword matching
                elif " " not in keyword:
                    words = normalized_text.split()

                    if keyword in words:
                        matched_keywords.append(keyword)

            # Calculate rule strength.
            if matched_phrases:
                score = 1.0

            elif matched_keywords:
                score = min(0.6 + (0.1 * (len(matched_keywords) - 1)), 0.9)

            else:
                score = 0.0

            if score > best_score:
                best_score = score
                best_intent = intent_name

        return {
            "intent": best_intent,
            "confidence": round(best_score, 2)
        }
