import json
import random
from pathlib import Path

from chatbot.preprocessing import normalize_text
from chatbot.rule_engine import RuleBasedEngine
from chatbot.semantic_engine import SemanticEngine


class ChatbotAgent:
    """
    Hybrid chatbot agent that combines rule-based
    and semantic intent recognition.
    """

    def __init__(
        self,
        intents_path="data/intents.json",
        rule_threshold=0.8,
        semantic_threshold=0.45
    ):
        self.intents_path = Path(intents_path)
        self.rule_threshold = rule_threshold
        self.semantic_threshold = semantic_threshold

        self.intents = self._load_intents()

        self.rule_engine = RuleBasedEngine(
            intents_path=intents_path
        )

        self.semantic_engine = SemanticEngine(
            intents_path=intents_path,
            threshold=semantic_threshold
        )

    def _load_intents(self):
        """Load intents and responses from the JSON knowledge base."""
        with self.intents_path.open("r", encoding="utf-8") as file:
            data = json.load(file)

        return data["intents"]

    def _get_intent_data(self, intent_name):
        """Find the complete data for an intent."""
        for intent in self.intents:
            if intent["name"] == intent_name:
                return intent

        return None

    def _get_response(self, intent_name):
        """Select a response for the detected intent."""
        intent_data = self._get_intent_data(intent_name)

        if not intent_data:
            return (
                "I'm sorry, I don't have enough information "
                "to answer that."
            )

        responses = intent_data.get("responses", [])

        if not responses:
            return (
                "I'm sorry, I don't have enough information "
                "to answer that."
            )

        return random.choice(responses)

    def process_message(self, text):
        """
        Process a user message using the hybrid
        rule-based and semantic approach.

        Returns:
            {
                "intent": intent_name,
                "confidence": float,
                "method": "rule" or "semantic" or "fallback",
                "response": chatbot_response
            }
        """

        # Handle empty input.
        normalized_text = normalize_text(text)

        if not normalized_text:
            return {
                "intent": "fallback",
                "confidence": 0.0,
                "method": "fallback",
                "response": (
                    "Please enter a message so I can help you."
                )
            }

        # ------------------------------------------------
        # Step 1: Rule-Based Matching
        # ------------------------------------------------

        rule_result = self.rule_engine.detect_intent(text)

        if (
            rule_result["intent"] is not None
            and rule_result["confidence"] >= self.rule_threshold
        ):
            intent = rule_result["intent"]

            return {
                "intent": intent,
                "confidence": rule_result["confidence"],
                "method": "rule",
                "response": self._get_response(intent)
            }

        # ------------------------------------------------
        # Step 2: Semantic Matching
        # ------------------------------------------------

        semantic_result = self.semantic_engine.detect_intent(text)

        if (
            semantic_result["intent"] is not None
            and semantic_result["confidence"] >= self.semantic_threshold
        ):
            intent = semantic_result["intent"]

            return {
                "intent": intent,
                "confidence": semantic_result["confidence"],
                "method": "semantic",
                "response": self._get_response(intent)
            }

        # ------------------------------------------------
        # Step 3: Fallback
        # ------------------------------------------------

        return {
            "intent": "fallback",
            "confidence": max(
                rule_result["confidence"],
                semantic_result["confidence"]
            ),
            "method": "fallback",
            "response": self._get_response("fallback")
        }
