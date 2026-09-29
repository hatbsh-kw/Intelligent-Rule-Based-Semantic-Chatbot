# Intelligent Rule-Based & Semantic Chatbot Agent

## 1. Project Overview

The **Intelligent Rule-Based & Semantic Chatbot Agent** is a Python-based chatbot that combines two approaches for understanding user messages:

1. **Rule-Based Matching** — identifies user intent using predefined keywords, phrases, and patterns.
2. **Semantic Matching** — identifies the meaning of a user's message using sentence embeddings and similarity comparison.

The two approaches are combined to make the chatbot more flexible. If a user's message does not produce a strong rule-based match, the system can use semantic similarity to identify the most appropriate intent.

The chatbot will provide a **web-based interface using Streamlit**, allowing users to communicate with the chatbot through a browser.

---

# 2. Project Folder Structure

```text
Intelligent-Rule-Based-Semantic-Chatbot/
│
├── chatbot/
│
├── data/
│
├── ui/
│
├── tests/
│
├── docs/
│
├── models/
│
└── utils/
```

The project is organized into separate folders so that the chatbot's core logic, user interface, data, tests, documentation, models, and utility functions remain independent and easy to maintain.

---

# 3. Folder and File Description

## 3.1 chatbot/

The `chatbot/` folder contains the **core intelligence of the chatbot**.

It is responsible for processing user messages, detecting intents, performing rule-based matching, performing semantic matching, and generating the final response.

### Files inside this folder

```text
chatbot/
├── __init__.py
├── preprocessing.py
├── rule_engine.py
├── semantic_engine.py
└── chatbot_agent.py
```

### `__init__.py`

Initializes the `chatbot` directory as a Python package and allows its modules to be imported easily.

### `preprocessing.py`

Handles text preprocessing before the message is passed to the matching engines.

Possible responsibilities include:

* Converting text to lowercase
* Removing unnecessary punctuation
* Normalizing whitespace
* Tokenizing text where required
* Preparing text for rule-based and semantic processing

### `rule_engine.py`

Implements the **rule-based intent recognition system**.

It will check user messages against predefined:

* Keywords
* Phrases
* Patterns
* Intent rules

For example:

```text
User: I forgot my password.

Detected Intent:
password_reset
```

### `semantic_engine.py`

Implements the **semantic matching system**.

It will use **Sentence Transformers** and the `all-MiniLM-L6-v2` model to generate sentence embeddings and compare the user's message with predefined intent examples.

This allows the chatbot to recognize messages with similar meanings even when different words are used.

Example:

```text
User: I can't remember the password I use to log in.

Detected Intent:
password_reset
```

### `chatbot_agent.py`

Acts as the main controller of the chatbot.

It will:

1. Receive the user's message.
2. Apply text preprocessing.
3. Try rule-based matching.
4. Use semantic matching when necessary.
5. Compare confidence/similarity scores.
6. Select the appropriate intent.
7. Return the corresponding response.
8. Return a fallback response when no sufficiently confident intent is found.

---

# 3.2 data/

The `data/` folder stores the chatbot's **intent and response data**.

### Files inside this folder

```text
data/
└── intents.json
```

### `intents.json`

Contains structured chatbot knowledge, including:

* Intent names
* Keywords
* Example user messages
* Possible responses

Example structure:

```text
Intent
├── Name
├── Keywords
├── Examples
└── Responses
```

Example intents may include:

* Greeting
* Goodbye
* Thanks
* Help
* Password Reset
* Account Access
* Services
* Support
* Working Hours
* Contact Information
* General Information
* Fallback

Keeping this information in JSON makes it easier to add or modify intents without changing the chatbot's core code.

---

# 3.3 ui/

The `ui/` folder contains the **user interface** of the chatbot.

### Files inside this folder

```text
ui/
└── app.py
```

### `app.py`

Contains the Streamlit application.

It will provide a browser-based chat interface where users can:

* Enter messages
* Send messages
* View chatbot responses
* Continue a conversation
* See previous messages during the session

The UI communicates with `chatbot_agent.py` but does not contain the main chatbot intelligence.

---

# 3.4 tests/

The `tests/` folder contains automated tests used to verify that the chatbot works correctly.

### Files inside this folder

```text
tests/
├── __init__.py
├── test_preprocessing.py
├── test_rule_engine.py
├── test_semantic_engine.py
└── test_chatbot_agent.py
```

### `__init__.py`

Initializes the test directory as a Python package.

### `test_preprocessing.py`

Tests the text preprocessing functions.

Examples:

* Lowercase conversion
* Punctuation handling
* Whitespace normalization
* Tokenization

### `test_rule_engine.py`

Tests the rule-based intent recognition.

Examples:

* Correct keyword detection
* Correct phrase matching
* Correct intent selection
* Handling of unknown messages

### `test_semantic_engine.py`

Tests the semantic matching functionality.

Examples:

* Embedding generation
* Similarity calculation
* Correct semantic intent detection
* Similarity threshold behavior

### `test_chatbot_agent.py`

Tests the complete chatbot workflow.

It verifies that the chatbot correctly combines preprocessing, rule-based matching, semantic matching, intent selection, and response generation.

Testing will be performed using **pytest**.

---

# 3.5 docs/

The `docs/` folder contains project documentation.

### Files inside this folder

```text
docs/
├── requirements.md
├── architecture.md
└── testing.md
```

### `requirements.md`

Contains the project's requirements, including:

* Problem statement
* Stakeholders
* Inputs
* Outputs
* Functional requirements
* Non-functional requirements
* System constraints

### `architecture.md`

Documents the system architecture and explains how the major components communicate with each other.

It may include:

* System architecture
* Component descriptions
* Processing flow
* Rule-based engine flow
* Semantic engine flow
* Hybrid decision-making process

### `testing.md`

Documents the testing strategy and results.

It may include:

* Test cases
* Unit testing
* Integration testing
* Manual testing
* Test results
* Error cases

---

# 3.6 models/

The `models/` folder is reserved for machine-learning model-related files if they are needed locally.

### Files inside this folder

```text
models/
└── .gitkeep
```

### `.gitkeep`

The `.gitkeep` file keeps the otherwise empty directory available in the Git repository.

The `all-MiniLM-L6-v2` model does not necessarily need to be manually stored inside this folder because Sentence Transformers can load the model through its model-loading mechanism.

The folder is therefore kept available for future model-related resources if required.

---

# 3.7 utils/

The `utils/` folder contains reusable helper functions that do not belong directly to the chatbot engines.

### Files inside this folder

```text
utils/
├── __init__.py
└── helpers.py
```

### `__init__.py`

Initializes the `utils` directory as a Python package.

### `helpers.py`

Contains general-purpose helper functions that may be shared by different parts of the application.

Examples may include:

* Loading JSON data
* Configuration helpers
* Common validation functions
* Other reusable utility functions

Only functions that are genuinely reusable will be placed here to avoid unnecessary complexity.

---

# 4. Root-Level Files

In addition to the folders, the project will contain several files in the root directory.

```text
Intelligent-Rule-Based-Semantic-Chatbot/
│
├── main.py
├── requirements.txt
├── .gitignore
└── README.md
```

## `main.py`

The main entry point for the project.

It can be used to initialize or run the application and can also provide a simple entry point for development and testing.

The Streamlit interface itself will be located in `ui/app.py`.

## `requirements.txt`

Contains the Python dependencies required to install and run the project.

The expected libraries include:

* Streamlit
* Sentence Transformers
* NLTK
* NumPy
* scikit-learn
* pytest

The final dependency list will contain only packages actually used by the implementation.

## `.gitignore`

Specifies files and directories that should not be committed to GitHub.

Examples may include:

* Python virtual environment
* Cache files
* Temporary files
* Local configuration files
* Generated model/cache files

## `README.md`

The main project documentation file.

It will provide an overview of the project and explain:

* Project purpose
* Features
* Technology stack
* Installation
* Project structure
* How to run the chatbot
* How to run tests
* Example conversations
* Project architecture
* Development information

---

# 5. Complete Project Structure

The final project is expected to have the following structure:

```text
Intelligent-Rule-Based-Semantic-Chatbot/
│
├── chatbot/
│   ├── __init__.py
│   ├── preprocessing.py
│   ├── rule_engine.py
│   ├── semantic_engine.py
│   └── chatbot_agent.py
│
├── data/
│   └── intents.json
│
├── ui/
│   └── app.py
│
├── tests/
│   ├── __init__.py
│   ├── test_preprocessing.py
│   ├── test_rule_engine.py
│   ├── test_semantic_engine.py
│   └── test_chatbot_agent.py
│
├── docs/
│   ├── requirements.md
│   ├── architecture.md
│   └── testing.md
│
├── models/
│   └── .gitkeep
│
├── utils/
│   ├── __init__.py
│   └── helpers.py
│
├── main.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

# 6. High-Level Responsibility

The project follows a separation-of-responsibility approach:

```text
data/
    ↓
Intent and response knowledge

chatbot/
    ↓
Chatbot intelligence

ui/
    ↓
User interaction

tests/
    ↓
Quality verification

docs/
    ↓
Project documentation

models/
    ↓
Model-related resources

utils/
    ↓
Reusable helper functions
```
