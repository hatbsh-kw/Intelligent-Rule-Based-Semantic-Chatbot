from chatbot.rule_engine import RuleBasedEngine


def test_greeting_intent():
    engine = RuleBasedEngine()

    result = engine.detect_intent("Hello!")

    assert result["intent"] == "greeting"
    assert result["confidence"] > 0


def test_password_reset_intent():
    engine = RuleBasedEngine()

    result = engine.detect_intent("I forgot my password")

    assert result["intent"] == "password_reset"
    assert result["confidence"] == 1.0


def test_services_intent():
    engine = RuleBasedEngine()

    result = engine.detect_intent("What services do you offer?")

    assert result["intent"] == "services"
    assert result["confidence"] == 1.0


def test_support_intent():
    engine = RuleBasedEngine()

    result = engine.detect_intent("I need customer support")

    assert result["intent"] == "support"
    assert result["confidence"] == 1.0


def test_unknown_message():
    engine = RuleBasedEngine()

    result = engine.detect_intent("What is the weather today?")

    assert result["intent"] is None
    assert result["confidence"] == 0.0


def test_empty_message():
    engine = RuleBasedEngine()

    result = engine.detect_intent("")

    assert result["intent"] is None
    assert result["confidence"] == 0.0
