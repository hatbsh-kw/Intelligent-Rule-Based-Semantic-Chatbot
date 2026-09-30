from chatbot.preprocessing import (
    normalize_text,
    tokenize_text,
    preprocess_text
)


def test_normalize_lowercase():
    result = normalize_text("HELLO WORLD")
    assert result == "hello world"


def test_remove_punctuation():
    result = normalize_text("Hello!!! How are you?")
    assert result == "hello how are you"


def test_normalize_whitespace():
    result = normalize_text("hello     how    are   you")
    assert result == "hello how are you"


def test_empty_input():
    result = preprocess_text("")
    assert result == []


def test_whitespace_input():
    result = preprocess_text("     ")
    assert result == []


def test_tokenization():
    result = tokenize_text("Hello how are you")
    assert result == ["hello", "how", "are", "you"]


def test_complete_preprocessing():
    result = preprocess_text("  HELLO!!!   How ARE you?  ")
    assert result == ["hello", "how", "are", "you"]
