# TASK 2 — INTELLIGENT RULE-BASED & SEMANTIC CHATBOT AGENT

## 1. Introduction

The Intelligent Rule-Based & Semantic Chatbot Agent is a domain-specific conversational system designed to understand user messages and provide appropriate responses.

The chatbot combines two approaches to natural-language understanding:

1. **Rule-Based Matching** — identifies predefined keywords, phrases, and patterns.
2. **Semantic Matching** — identifies messages with similar meanings even when different words or sentence structures are used.

The combination of these approaches creates a hybrid chatbot that is more flexible than a traditional keyword-based chatbot while remaining controlled, predictable, and suitable for a defined service domain.

The chatbot will be developed as a **Customer Support / Service Assistant**. This domain is a project design choice intended to provide realistic conversations and demonstrate the required rule-based and semantic capabilities. It is not presented as a domain explicitly specified by the internship assignment.

---

# 2. Problem Statement

Traditional rule-based chatbots depend heavily on predefined keywords and exact or closely matching phrases.

For example, a chatbot may recognize:

> "I forgot my password."

However, a user may express the same problem differently:

> "I can't remember the password I use to log in."

A simple keyword-based system may fail to recognize that both messages represent the same intent.

Therefore, the system needs a semantic matching capability that can identify similarities in meaning rather than relying only on exact words.

The proposed chatbot addresses this problem by combining rule-based matching with semantic similarity.

The overall process is:

**User Message → Text Preprocessing → Rule-Based Matching → Semantic Matching when necessary → Intent Detection → Response Selection → User**

---

# 3. Project Goal

The main goal of the project is to develop an intelligent customer-support chatbot that can:

* Understand common user requests.
* Recognize predefined intents using rules.
* Understand differently worded messages using semantic similarity.
* Select an appropriate response.
* Handle unknown or low-confidence messages using a fallback mechanism.
* Maintain a continuous conversation.
* Provide a simple and understandable user interface.
* Handle errors gracefully.
* Be easy to extend with additional intents and responses.

---

# 4. Selected Application Domain

## 4.1 Domain

The chatbot will operate as a:

**Customer Support / Service Assistant**

The chatbot will simulate a support assistant for a software or technology service company.

Users can communicate with the chatbot about topics such as:

* Account access
* Password recovery
* Available services
* Customer support
* Working hours
* Contact information
* General assistance
* Greetings and conversation closing

The chatbot is intentionally **domain-specific** rather than a general-purpose conversational AI.

---

# 5. Stakeholders

The main stakeholders of the system are:

### 5.1 Customers / End Users

Customers interact with the chatbot to obtain quick answers to common questions and support requests.

Examples include:

* Asking how to recover a password.
* Asking about available services.
* Asking how to contact support.
* Asking about working hours.

### 5.2 Support Team

The support team benefits by allowing the chatbot to handle simple and repetitive questions before they require human assistance.

### 5.3 System Administrator / Developer

The developer or administrator maintains the chatbot's intent data, rules, responses, semantic model, and configuration.

### 5.4 Project Evaluator

The internship evaluator can use the application to verify the implementation of:

* Rule-based intent recognition.
* Semantic similarity.
* Intent classification.
* Response generation.
* Fallback handling.
* Conversation management.

---

# 6. System Inputs

The primary input to the system is a user's natural-language message.

Examples include:

```text
Hello
```

```text
I forgot my password.
```

```text
I can't remember the password I use to log in.
```

```text
What services do you provide?
```

```text
How can I contact support?
```

```text
When are you open?
```

The system must also be capable of handling invalid, empty, or unknown input.

Examples:

```text
""
```

```text
!!!
```

```text
asdfghjkl
```

---

# 7. System Outputs

The chatbot produces a textual response based on the detected intent.

Examples:

### Greeting

```text
User:
Hello

Bot:
Hello! How can I help you today?
```

### Password Recovery

```text
User:
I forgot my password.

Bot:
You can reset your password using the password recovery option.
```

### Semantic Password Recovery

```text
User:
I can't remember the password I use to log in.

Bot:
You can reset your password using the password recovery option.
```

### Unknown Request

```text
User:
What is the population of Japan?

Bot:
I'm sorry, I don't have information about that.
I can help you with account, service, and support-related questions.
```

---

# 8. Functional Requirements

## FR-01 — User Input

The system shall allow users to enter natural-language messages.

---

## FR-02 — Text Preprocessing

The system shall preprocess user messages before performing intent matching.

The preprocessing layer may perform operations such as:

* Lowercase conversion.
* Punctuation cleanup.
* Whitespace normalization.
* Tokenization where appropriate.

For example:

```text
"HELLO!!! How are you?"
```

may become:

```text
"hello how are you"
```

---

## FR-03 — Rule-Based Intent Recognition

The system shall identify predefined user intents using rules, keywords, phrases, or patterns.

For example:

```text
Input:
hello

↓
Rule Matching

↓
Intent:
greeting
```

The rule-based engine should provide fast and deterministic handling for common requests.

---

## FR-04 — Semantic Intent Recognition

The system shall use semantic similarity to identify messages that have similar meanings even when their wording differs.

For example:

```text
Known example:
"I forgot my password."

User:
"I can't remember my login password."
```

Both messages should be associated with:

```text
password_reset
```

The semantic engine will use sentence representations or embeddings to compare the meaning of messages.

---

## FR-05 — Hybrid Intent Detection

The system shall combine rule-based and semantic approaches.

The intended decision flow is:

```text
User Message
      ↓
Text Preprocessing
      ↓
Rule-Based Matching
      ↓
Strong Rule Match?
   /          \
 YES           NO
 ↓              ↓
Intent       Semantic Matching
                 ↓
          Similarity Score
                 ↓
          Confidence Check
             /       \
           HIGH       LOW
            ↓          ↓
         Intent      Fallback
```

This hybrid approach is the central concept of the chatbot.

---

## FR-06 — Semantic Similarity Score

The semantic engine shall calculate a similarity score between the user's message and available intent examples or representations.

Conceptually:

```text
User Sentence
      ↓
Embedding Model
      ↓
Vector Representation
      ↓
Similarity Calculation
      ↓
Similarity Score
```

The system shall use the similarity score to determine whether a semantic match is sufficiently reliable.

---

## FR-07 — Confidence Threshold

The system shall use a configurable similarity threshold to prevent low-confidence semantic matches from producing unrelated responses.

For example:

```text
Similarity = 0.87
Threshold  = 0.70
```

Since:

```text
0.87 >= 0.70
```

the system may accept the semantic match.

However, the final threshold should be selected and validated through testing rather than being assumed to be optimal.

---

## FR-08 — Response Selection

Once an intent has been identified, the chatbot shall select an appropriate response associated with that intent.

For example:

```text
Intent:
password_reset

Response:
You can reset your password using the password recovery option.
```

---

## FR-09 — Fallback Response

If the chatbot cannot confidently determine the user's intent, it shall provide a fallback response.

Example:

```text
User:
Tell me about quantum physics.

Bot:
I'm sorry, I don't have information about that.
Could you please ask a question related to the services I support?
```

The fallback mechanism prevents the chatbot from returning an unrelated or misleading response.

---

## FR-10 — Conversation Loop

The chatbot shall support continuous interaction.

Example:

```text
Bot:
Hello! How can I help you?

User:
I forgot my password.

Bot:
You can reset your password using the password recovery option.

User:
Thank you.

Bot:
You're welcome!

User:
Bye.

Bot:
Goodbye! Have a great day.
```

---

## FR-11 — Exit Command

The system shall provide commands that allow users to terminate the conversation.

Examples include:

```text
bye
goodbye
exit
quit
```

---

## FR-12 — Intent and Response Data

The chatbot shall maintain intent examples and responses in a structured data source.

A JSON file is proposed for the initial implementation:

```text
data/
└── intents.json
```

The data should contain information such as:

* Intent name.
* Example user messages.
* Keywords or patterns where appropriate.
* Possible responses.

This approach allows new intents and responses to be added without redesigning the entire application.

---

# 9. Initial Intent Requirements

The initial chatbot will support the following intent categories:

| Intent                | Purpose                                      |
| --------------------- | -------------------------------------------- |
| `greeting`            | Handle greetings and welcome messages        |
| `goodbye`             | Handle conversation-ending messages          |
| `thanks`              | Respond to appreciation                      |
| `help`                | Explain what the chatbot can assist with     |
| `password_reset`      | Handle password recovery requests            |
| `account_access`      | Handle login and account-access problems     |
| `services`            | Provide information about available services |
| `support`             | Handle general support requests              |
| `working_hours`       | Provide service/support availability         |
| `contact_information` | Provide support/contact information          |
| `general_information` | Handle supported general questions           |
| `fallback`            | Handle unknown or low-confidence requests    |

This list is an initial design and can be refined during implementation and testing.

---

# 10. Example Conversations

## 10.1 Greeting

```text
User:
Hi

Bot:
Hello! How can I help you today?
```

## 10.2 Password Reset — Rule-Based

```text
User:
I forgot my password.

Bot:
You can reset your password using the password recovery option.
```

## 10.3 Password Reset — Semantic

```text
User:
I can't remember the password I use to log in.

Bot:
You can reset your password using the password recovery option.
```

The second example demonstrates why semantic matching is necessary.

---

## 10.4 Account Access

```text
User:
I can't log into my account.

Bot:
Please check your username and password. If you still cannot access your account, contact our support team.
```

---

## 10.5 Services

```text
User:
What services do you provide?

Bot:
We provide software development, IT consulting, and digital solutions.
```

---

## 10.6 Support

```text
User:
How can I contact support?

Bot:
You can contact our support team through the available support channels.
```

---

## 10.7 Working Hours

```text
User:
When are you open?

Bot:
Our support team is available during the configured working hours.
```

---

## 10.8 Thanks

```text
User:
Thank you for your help.

Bot:
You're welcome! I'm happy to help.
```

---

## 10.9 Unknown Request

```text
User:
What is the capital of France?

Bot:
I'm sorry, I don't have information about that.
I can help you with account, service, and support-related questions.
```

---

## 10.10 Conversation Ending

```text
User:
Bye

Bot:
Goodbye! Have a great day.
```

---

# 11. Non-Functional Requirements

## NFR-01 — Usability

The chatbot should provide a simple and understandable interaction experience.

---

## NFR-02 — Performance

The chatbot should process normal user messages and return responses within a reasonable amount of time.

---

## NFR-03 — Reliability

The system should continue operating correctly when users provide:

* Empty input.
* Unknown questions.
* Unexpected text.
* Repeated messages.
* Invalid input.

---

## NFR-04 — Maintainability

The application should use a modular architecture so that preprocessing, rule matching, semantic matching, response handling, and the user interface are separated.

---

## NFR-05 — Extensibility

The system should allow new intents, examples, and responses to be added without requiring major changes to the core chatbot engine.

---

## NFR-06 — Error Handling

The application should gracefully handle errors related to:

* Invalid input.
* Missing intent data.
* Malformed configuration.
* Semantic model initialization.
* Unexpected runtime exceptions.

The system should provide useful error information rather than terminating unexpectedly.

---

# 12. Proposed Technology Stack

The proposed technology stack is:

| Category | Technology | Purpose |
| --- | --- | --- |
| **Programming Language** | **Python 3.12** | Main development language |
| **Rule-Based Engine** | **Python** | Keyword, phrase, and pattern-based intent matching |
| **NLP / Text Processing** | **NLTK** | Tokenization and basic text preprocessing where needed |
| **Semantic AI** | **Sentence Transformers** | Generate sentence embeddings for semantic understanding |
| **Semantic Model** | **`all-MiniLM-L6-v2`** | Lightweight sentence-embedding model for semantic similarity |
| **Similarity Calculation** | **Cosine Similarity** | Compare user messages with intent examples |
| **Intent / Response Storage** | **JSON** | Store intents, examples, keywords, and responses |
| **User Interface** | **Streamlit** | Provide a browser-based interactive chatbot interface |
| **Testing** | **pytest** | Automated unit and integration testing |
| **Numerical Processing** | **NumPy** | Vector and numerical operations |
| **Version Control** | **Git** | Track project changes |
| **Repository** | **GitHub** | Store and submit the project |
| **Documentation** | **Markdown / Word** | README and project documentation |
| **Environment** | **Python `venv`** | Isolated project environment |


---

# 13. Proposed System Architecture

The system will follow a modular architecture.

```text
                         ┌──────────────────┐
                         │       User       │
                         └────────┬─────────┘
                                  ↓
                         ┌──────────────────┐
                         │   User Interface │
                         └────────┬─────────┘
                                  ↓
                         ┌──────────────────┐
                         │  Chatbot Agent   │
                         └────────┬─────────┘
                                  ↓
                         ┌──────────────────┐
                         │ Text Preprocessing│
                         └────────┬─────────┘
                                  ↓
                    ┌─────────────┴─────────────┐
                    ↓                           ↓
          ┌──────────────────┐       ┌──────────────────┐
          │ Rule-Based Engine│       │ Semantic Engine  │
          └────────┬─────────┘       └────────┬─────────┘
                   ↓                          ↓
                   └────────────┬─────────────┘
                                ↓
                     ┌────────────────────┐
                     │ Decision / Intent  │
                     │     Selection      │
                     └──────────┬─────────┘
                                ↓
                     ┌────────────────────┐
                     │ Response Generator │
                     └──────────┬─────────┘
                                ↓
                     ┌────────────────────┐
                     │    User Output     │
                     └──────────┬─────────┘
                                ↓
                     ┌────────────────────┐
                     │ Continuous Loop    │
                     └────────────────────┘
```

---

# 14. Proposed Project Structure

The project is expected to follow a structure similar to:

```text
Rule_Semantic_Chatbot/
│
├── chatbot/
│   ├── __init__.py
│   ├── rule_engine.py
│   ├── semantic_engine.py
│   ├── preprocessing.py
│   └── chatbot_agent.py
│
├── data/
│   └── intents.json
│
├── models/
│
├── ui/
│   └── cli.py
│
├── utils/
│
├── tests/
│
├── docs/
│
├── main.py
├── requirements.txt
├── .gitignore
└── README.md
```

Each component will have a specific responsibility.

### `chatbot/`

Contains the core chatbot logic.

### `data/`

Contains intents, example messages, and responses.

### `models/`

Contains locally required semantic model resources if the selected implementation requires them.

### `ui/`

Contains the user interaction layer.

### `utils/`

Contains reusable helper functions and configuration.

### `tests/`

Contains automated tests.

### `docs/`

Contains project documentation, diagrams, test reports, and other supporting documents.

---

# 15. Core Processing Flow

The chatbot's complete processing pipeline will be:

```text
1. User enters a message
          ↓
2. Validate input
          ↓
3. Preprocess text
          ↓
4. Attempt rule-based matching
          ↓
5. Strong rule match?
       /       \
     Yes        No
      ↓          ↓
   Intent     Semantic matching
                 ↓
           Calculate similarity
                 ↓
           Check threshold
             /       \
           High       Low
            ↓          ↓
         Intent      Fallback
            │          │
            └────┬─────┘
                 ↓
        Select appropriate response
                 ↓
          Display response
                 ↓
        Continue conversation
```

---

# 16. Semantic Matching Concept

The semantic engine will represent sentences as numerical vectors called embeddings.

For example:

```text
"I forgot my password."
```

is converted into an embedding.

Another sentence:

```text
"I can't remember my login password."
```

is also converted into an embedding.

The system then compares the resulting representations.

Conceptually:

```text
Sentence
   ↓
Embedding Model
   ↓
Vector Representation
   ↓
Similarity Calculation
   ↓
Similarity Score
```

A high similarity score indicates that the messages may have similar meanings.

The system will use a configurable threshold to determine whether the similarity is strong enough to accept the semantic intent.

---

# 17. Rule-Based and Semantic Responsibilities

The two engines have different responsibilities.

| Rule-Based Engine           | Semantic Engine           |
| --------------------------- | ------------------------- |
| Exact/common patterns       | Meaning-based matching    |
| Keywords                    | Sentence embeddings       |
| Fast deterministic matching | Handles paraphrases       |
| Predictable responses       | Handles different wording |
| Known expressions           | Similar meanings          |

The engines complement each other rather than replacing one another.

---

# 18. Fallback Strategy

The chatbot must not attempt to answer every question.

When neither the rule engine nor the semantic engine can confidently identify an intent, the chatbot will use a fallback response.

Example:

```text
User:
asdfghjkl

Bot:
I'm not sure I understand. Could you please rephrase your question?
```

This provides predictable behavior for unsupported requests.

---

# 19. User Interface Requirement

The initial interface will be a command-line chatbot.

Example:

```text
========================================
     Intelligent Chatbot Agent
========================================

Bot: Hello! How can I help you?

You: hello

Bot: Hello! How can I help you?

You: I can't remember my login password.

Bot: You can reset your password using the password recovery option.

You: bye

Bot: Goodbye! Have a great day.
```

The interface should clearly distinguish user messages from chatbot responses.

---

# 20. Error Handling Requirements

The system shall gracefully handle common errors.

### Empty Input

```text
User:

Bot:
Please enter a message.
```

### Unknown Input

The system shall return the fallback response.

### Invalid Intent Data

The system should detect missing or malformed intent information where practical.

### Semantic Model Failure

If the semantic model cannot be initialized or loaded, the application should provide a meaningful error rather than failing silently.

### Unexpected Runtime Error

Unexpected errors should be handled appropriately to prevent uncontrolled application termination.

---

# 21. Testing Requirements

Testing will cover both the individual components and the complete chatbot workflow.

## 21.1 Rule-Based Testing

Examples:

```text
"hello" → greeting
"hi" → greeting
"bye" → goodbye
"forgot password" → password_reset
"thank you" → thanks
```

## 21.2 Semantic Testing

Examples:

```text
"I forgot my password."
        ↓
password_reset
```

and:

```text
"I can't remember my login credentials."
        ↓
password_reset
```

The second example should demonstrate that the semantic engine can recognize similar meaning even when the wording differs.

## 21.3 Fallback Testing

Example:

```text
"Tell me about dinosaurs."
        ↓
fallback
```

## 21.4 Edge-Case Testing

Examples:

```text
""
"!!!"
"123456"
"hello     hello"
```

## 21.5 Conversation Testing

A complete conversation should be tested:

```text
Greeting
   ↓
Question
   ↓
Response
   ↓
Thanks
   ↓
Goodbye
```

Automated testing will be used for internal logic, while manual testing will be used to validate the complete user interaction.

---

# 22. Requirements-to-Testing Mapping

| Requirement          | Implementation Area  | Validation          |
| -------------------- | -------------------- | ------------------- |
| User input           | UI / Chatbot Agent   | Input test          |
| Text preprocessing   | Preprocessing module | Preprocessing tests |
| Rule matching        | Rule engine          | Intent tests        |
| Semantic matching    | Semantic engine      | Semantic tests      |
| Hybrid decision      | Chatbot agent        | Integration tests   |
| Similarity threshold | Semantic engine      | Threshold tests     |
| Response selection   | Response handling    | Response tests      |
| Fallback             | Chatbot agent        | Unknown-input tests |
| Conversation loop    | UI / Agent           | Conversation test   |
| Exit command         | UI / Agent           | Exit test           |
| Error handling       | All relevant modules | Error tests         |

---

# 23. Project Limitations

The chatbot will be intentionally domain-specific.

It will not attempt to:

* Answer every question in the world.
* Replace a general-purpose AI assistant.
* Generate unrestricted knowledge-based answers.
* Provide expert advice outside its supported domain.

Its purpose is to demonstrate intelligent intent recognition using rule-based and semantic techniques.

---

# 24. Expected Final Demonstration

The completed system should demonstrate three important behaviors.

### 1. Exact or Known Wording

```text
User:
Hello

↓
Rule-Based Engine

↓
greeting

↓
Bot:
Hello! How can I help you today?
```

### 2. Different Wording with Similar Meaning

```text
User:
I can't remember the password I use to log in.

↓
Semantic Engine

↓
password_reset

↓
Bot:
You can reset your password using the password recovery option.
```

### 3. Unknown Meaning

```text
User:
What is the capital of France?

↓
No confident intent

↓
Fallback

↓
Bot:
I'm sorry, I don't have information about that.
```

These three cases demonstrate the core intelligence of the system:

**Known wording → Rule-Based Matching**

**Similar meaning → Semantic Matching**

**Unsupported request → Fallback**

---

# 25. Phase 1 Deliverables

At the end of Phase 1, the following items should be prepared:

1. Project problem statement.
2. Project goal and objectives.
3. Selected application domain.
4. Stakeholder identification.
5. System inputs and outputs.
6. Functional requirements.
7. Non-functional requirements.
8. Initial intent list.
9. Technology stack.
10. Proposed system architecture.
11. Proposed project structure.
12. Initial testing strategy.
13. Error-handling requirements.
14. Initial README.
15. Python virtual environment.
16. Required project dependencies.
17. `.gitignore`.

---

# 26. Phase 1 Conclusion

The Intelligent Rule-Based & Semantic Chatbot Agent will be developed as a domain-specific **Customer Support / Service Assistant**.

The system will combine deterministic rule-based intent recognition with semantic similarity to understand both common predefined expressions and differently worded messages with similar meanings.

The overall objective is:

> **To build a reliable and maintainable chatbot that can recognize user intent using rules and semantic understanding, provide appropriate responses, and safely fall back when the user's intent cannot be determined with sufficient confidence.**

Once the requirements and project setup are complete, development can proceed to:

**Phase 2 — Rule-Based Chatbot Engine**

where the first functional chatbot components will be implemented.
