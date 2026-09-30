from chatbot.chatbot_agent import ChatbotAgent


def test_strong_rule_match():
    agent = ChatbotAgent()

    result = agent.process_message("I forgot my password")

    assert result["intent"] == "password_reset"
    assert result["method"] == "rule"
    assert result["confidence"] >= agent.rule_threshold
    assert result["response"]


def test_greeting_rule_match():
    agent = ChatbotAgent()

    result = agent.process_message("Good morning")

    assert result["intent"] == "greeting"
    assert result["method"] == "rule"
    assert result["confidence"] >= agent.rule_threshold
    assert result["response"]


def test_semantic_matching():
    agent = ChatbotAgent()

    result = agent.process_message(
        "I cannot remember my password"
    )

    assert result["intent"] == "password_reset"
    assert result["method"] in ["rule", "semantic"]
    assert result["response"]


def test_unknown_message_uses_fallback():
    agent = ChatbotAgent()

    result = agent.process_message(
        "Can you explain photosynthesis?"
    )

    assert result["intent"] == "fallback"
    assert result["method"] == "fallback"
    assert result["response"]


def test_empty_message_uses_fallback():
    agent = ChatbotAgent()

    result = agent.process_message("")

    assert result["intent"] == "fallback"
    assert result["method"] == "fallback"
    assert result["response"]
