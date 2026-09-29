# Task 2: Intelligent Rule-Based & Semantic Chatbot Agent — Implementation Phase Plan

Your next task is to move from documentation/setup into implementation.

For your **Task 2: Intelligent Rule-Based & Semantic Chatbot Agent**, implement it in these phases:

### 1. Phase 1 — Project Setup

Create the root files such as `main.py`, `requirements.txt`, `.gitignore`, and set up the Python virtual environment.

Create the project folders and install the required dependencies:

* Python 3.12
* Streamlit
* NLTK
* Sentence Transformers
* NumPy
* scikit-learn
* pytest

Verify that the development environment works correctly before starting the chatbot modules.

---

### 2. Phase 2 — Intent and Chatbot Data

Start with the `data/` folder.

Create `intents.json` and define the chatbot's initial intents, keywords, example messages, and responses.

Initial intents include:

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

Make sure the data structure can be used by both the rule-based and semantic engines.

---

### 3. Phase 3 — Text Preprocessing

Work inside the `chatbot/` folder.

Implement `preprocessing.py`.

Handle basic text preparation such as:

* Converting text to lowercase
* Removing unnecessary punctuation
* Normalizing whitespace
* Handling empty input
* Tokenization where needed

Test the preprocessing functions before moving to the next module.

---

### 4. Phase 4 — Rule-Based Engine

Work inside `chatbot/`.

Implement `rule_engine.py`.

Use the data from `intents.json` to recognize user intent using:

* Keywords
* Phrases
* Patterns
* Rule-based matching

Return the detected intent and an appropriate confidence/strength result.

Test common messages and unknown messages to make sure the rule-based engine behaves correctly.

---

### 5. Phase 5 — Semantic Matching Engine

Work inside `chatbot/`.

Implement `semantic_engine.py`.

Use **Sentence Transformers** with the `all-MiniLM-L6-v2` model to:

* Generate sentence embeddings
* Compare the user's message with intent examples
* Calculate cosine similarity
* Find the most semantically similar intent
* Apply a similarity threshold
* Reject low-confidence matches

Test different ways of asking the same question to verify that semantic matching recognizes similar meanings.

---

### 6. Phase 6 — Hybrid Chatbot Agent

Work inside `chatbot/`.

Implement `chatbot_agent.py`.

Combine the rule-based and semantic engines into one chatbot agent.

The processing flow will be:

```text
User Message
      ↓
Text Preprocessing
      ↓
Rule-Based Matching
      ↓
Strong Rule Match?
   Yes ↓       No ↓
 Intent      Semantic Matching
               ↓
        Similarity Threshold
           ↓           ↓
        Match       No Match
           ↓           ↓
        Intent      Fallback
           ↓
        Response
```

The chatbot should prioritize strong rule-based matches and use semantic matching when a suitable rule-based match is not found.

---

### 7. Phase 7 — Streamlit User Interface

Work inside the `ui/` folder.

Implement `app.py` using **Streamlit**.

Create a simple browser-based chatbot interface that allows users to:

* Enter messages
* Send messages
* View chatbot responses
* Maintain conversation history
* Clear or restart the conversation where appropriate

Connect the Streamlit interface to `chatbot_agent.py`.

---

### 8. Phase 8 — Error Handling and Improvements

Improve the complete chatbot system.

Handle situations such as:

* Empty user messages
* Unknown questions
* Low semantic similarity
* Invalid intent data
* Missing files
* Model loading errors
* Unexpected runtime errors

Make sure the chatbot provides a clear fallback response instead of inventing an answer when it cannot confidently identify the user's intent.

---

### 9. Phase 9 — Testing and Validation

Work inside the `tests/` folder.

Create and run tests for each major module:

* `test_preprocessing.py`
* `test_rule_engine.py`
* `test_semantic_engine.py`
* `test_chatbot_agent.py`

Test:

* Text preprocessing
* Rule-based intent detection
* Semantic intent detection
* Similarity thresholds
* Hybrid decision-making
* Correct responses
* Fallback behavior

Also perform manual testing through the Streamlit interface.

---

### 10. Phase 10 — Final Documentation and Submission

Complete the project documentation.

Update:

* `README.md`
* `docs/requirements.md`
* `docs/architecture.md`
* `docs/testing.md`

Document:

* Project overview
* Requirements
* Technology stack
* Folder structure
* Architecture
* Rule-based approach
* Semantic approach
* Hybrid decision process
* Installation instructions
* Usage instructions
* Testing results
* Example conversations
* Limitations and future improvements

Finally:

* Run all tests
* Verify the Streamlit application
* Check the project structure
* Check Git status
* Commit the final version
* Push the project to GitHub
* Verify the repository before submission
