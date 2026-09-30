import re
import nltk
from nltk.tokenize import word_tokenize


def normalize_text(text):
    """
    Convert text to lowercase, remove unnecessary punctuation,
    and normalize whitespace.
    """
    if not text or not text.strip():
        return ""

    # Convert to lowercase
    text = text.lower()

    # Remove punctuation and keep letters, numbers, and whitespace
    text = re.sub(r"[^\w\s]", "", text)

    # Normalize multiple spaces into a single space
    text = re.sub(r"\s+", " ", text)

    return text.strip()


def tokenize_text(text):
    """
    Tokenize the input text into individual words.
    """
    normalized_text = normalize_text(text)

    if not normalized_text:
        return []

    return word_tokenize(normalized_text)


def preprocess_text(text):
    """
    Complete preprocessing pipeline.

    Returns a list of normalized tokens.
    """
    return tokenize_text(text)
