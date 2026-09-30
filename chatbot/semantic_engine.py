import json
from pathlib import Path

import numpy as np
from sentence_transformers import SentenceTransformer


class SemanticEngine:
    """
    Semantic intent recognition engine.

    Uses Sentence Transformers to compare a user's message
    with intent examples using cosine similarity.
    """

    def __init__(
        self,
        intents_path="data/intents.json",
        model_name="all-MiniLM-L6-v2",
        threshold=0.45
    ):
        self.intents_path = Path(intents_path)
        self.model_name = model_name
        self.threshold = threshold

        self.intents = self._load_intents()
        self.model = SentenceTransformer(self.model_name)

        self.examples = []
        self.example_intents = []

        self._prepare_examples()

        if self.examples:
            self.example_embeddings = self.model.encode(
                self.examples,
                convert_to_numpy=True,
                normalize_embeddings=True
            )
        else:
            self.example_embeddings = np.array([])

    def _load_intents(self):
        """Load intent definitions from the JSON knowledge base."""
        with self.intents_path.open("r", encoding="utf-8") as file:
            data = json.load(file)

        return data["intents"]

    def _prepare_examples(self):
        """
        Collect semantic examples and associate each example
        with its corresponding intent.
        """
        for intent in self.intents:
            intent_name = intent["name"]

            # Fallback should not be used as a semantic example.
            if intent_name == "fallback":
                continue

            for example in intent.get("examples", []):
                if example.strip():
                    self.examples.append(example)
                    self.example_intents.append(intent_name)

    def _cosine_similarity(self, vector_a, vector_b):
        """Calculate cosine similarity between two vectors."""
        denominator = (
            np.linalg.norm(vector_a) *
            np.linalg.norm(vector_b)
        )

        if denominator == 0:
            return 0.0

        return float(np.dot(vector_a, vector_b) / denominator)

    def detect_intent(self, text):
        """
        Find the intent whose example is most semantically similar
        to the user's message.

        Returns:
            {
                "intent": intent_name or None,
                "confidence": similarity_score
            }
        """
        if not text or not text.strip():
            return {
                "intent": None,
                "confidence": 0.0
            }

        if not self.examples:
            return {
                "intent": None,
                "confidence": 0.0
            }

        user_embedding = self.model.encode(
            text,
            convert_to_numpy=True,
            normalize_embeddings=True
        )

        similarities = np.dot(
            self.example_embeddings,
            user_embedding
        )

        best_index = int(np.argmax(similarities))
        best_score = float(similarities[best_index])

        if best_score < self.threshold:
            return {
                "intent": None,
                "confidence": round(best_score, 4)
            }

        return {
            "intent": self.example_intents[best_index],
            "confidence": round(best_score, 4)
        }
