# TalentScout - AI Hiring Assistant

## Overview

TalentScout AI Hiring Assistant is a state-driven conversational screening system built using Large Language Models (LLMs). The application simulates an initial technical interview process by collecting candidate information, dynamically generating technical questions based on declared technologies, and automatically evaluating responses.

The system is designed with modular architecture and controlled conversation flow to ensure structured, reliable, and production-ready behavior.

---

## Features

- Structured multi-stage conversation workflow
- Candidate information collection
- Tech stack-based dynamic question generation
- Five short-answer questions per technology
- Stack-by-stack evaluation
- Automated scoring (out of 10 per technology)
- Strict evaluation with feedback and verdict
- Modular architecture with clean separation of concerns
- Environment-based API key management
- Dependency version control

---

## Architecture

The application follows a modular and layered architecture:

### 1. UI Layer (Streamlit)

Responsible for:
- Displaying chat interface
- Accepting user input
- Rendering conversation history
- Managing rerun logic
- Triggering state transitions

### 2. Session Manager

Handles:
- Conversation stage tracking
- Candidate information storage
- Tech stack management
- Current stack indexing
- Answer storage

The application uses `st.session_state` to persist conversation data across script reruns.

### 3. LLM Service Layer

Encapsulates:
- Groq API communication
- Model configuration
- Response generation

This abstraction ensures:
- Clean separation of concerns
- Easy model replacement
- Maintainability

### 4. State Machine Workflow

The assistant operates using a deterministic stage-based workflow:
greeting
collect_info
collect_stack
ask_questions
collect_answers
evaluate
end


This prevents uncontrolled generative behavior and ensures predictable execution.

---

## Technical Stack

- Python
- Streamlit
- Groq LLM API (Llama 3.3 model)
- python-dotenv

---


The application will open automatically in your default browser.

---

## Application Workflow

### Step 1: Greeting

The assistant introduces itself and explains the screening purpose.

### Step 2: Candidate Information Collection

The system collects:
- Name
- Email
- Phone number
- Years of experience
- Desired role
- Location

### Step 3: Tech Stack Declaration

The candidate provides technologies in comma-separated format.

Example:
Python, Django, MySQL


### Step 4: Question Generation

For each declared technology:
- Exactly five short, one-line answer-type questions are generated.
- Questions are strictly formatted.
- No descriptive or essay-type questions are allowed.

### Step 5: Answer Collection

The system:
- Collects answers stack-by-stack
- Stores responses in structured format
- Moves to the next stack only after completion

### Step 6: Evaluation

The evaluator:
- Scores each question (2 marks each)
- Calculates total score out of 10
- Provides concise feedback
- Assigns verdict (Strong / Moderate / Weak)

---

## Prompt Engineering Strategy

The system uses structured prompting techniques:

- Role conditioning (Technical Interviewer, Senior Evaluator)
- Output constraint enforcement
- Short-answer restriction
- Strict formatting rules
- Deterministic response guidance

This reduces hallucination and improves evaluation consistency.

---

## Design Decisions

### Deterministic State Machine

Instead of free-form conversation, a controlled state machine ensures:
- Predictable flow
- Better debugging
- Production readiness
- Reduced ambiguity

### Short-Answer Question Constraint

One-line answer questions improve:
- Evaluation consistency
- Scoring reliability
- Structured assessment
- Reduced subjectivity

### Modular Architecture

Separation of:
- UI logic
- Business logic
- LLM communication
- State management

This enhances scalability and maintainability.

### Secure Configuration

Environment-based API key storage prevents credential leakage.

---

## Limitations

- Evaluation relies on LLM reasoning
- No persistent database storage
- No authentication mechanism
- No bias mitigation layer
- No recruiter dashboard interface

---

## Future Enhancements

- Database integration
- Recruiter dashboard
- Exportable evaluation reports (PDF/CSV)
- Embedding-based semantic evaluation
- Confidence scoring
- Admin analytics panel
- Candidate history tracking

---

## Learning Outcomes Demonstrated

This project demonstrates:

- Large Language Model integration
- Prompt engineering
- Conversational AI system design
- State-machine architecture
- Modular software development
- Secure configuration management
- Version-controlled dependency handling
- Streamlit-based application deployment

---

## Author
Chethan D L


Developed as part of an AI/ML internship technical assignment.