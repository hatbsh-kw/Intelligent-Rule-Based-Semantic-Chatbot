from chatbot.semantic_engine import SemanticEngine


def test_password_reset_semantic_match():
    engine = SemanticEngine()

    result = engine.detect_intent(
        "I can't remember the password I use to sign in"
    )

    assert result["intent"] == "password_reset"
    assert result["confidence"] >= engine.threshold


def test_services_semantic_match():
    engine = SemanticEngine()

    result = engine.detect_intent(
        "What kind of software solutions do you provide?"
    )

    assert result["intent"] == "services"
    assert result["confidence"] >= engine.threshold


def test_support_semantic_match():
    engine = SemanticEngine()

    result = engine.detect_intent(
        "I need assistance from your technical team"
    )

    assert result["intent"] == "support"
    assert result["confidence"] >= engine.threshold


def test_greeting_semantic_match():
    engine = SemanticEngine()

    result = engine.detect_intent(
        "Greetings to you"
    )

    assert result["intent"] == "greeting"
    assert result["confidence"] >= engine.threshold


def test_unknown_message_is_rejected():
    engine = SemanticEngine()

    result = engine.detect_intent(
        "Can you explain how photosynthesis works?"
    )

    assert result["intent"] is None
    assert result["confidence"] < engine.threshold


def test_empty_message_is_rejected():
    engine = SemanticEngine()

    result = engine.detect_intent("")

    assert result["intent"] is None
    assert result["confidence"] == 0.0
