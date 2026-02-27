import streamlit as st
from services.llm_service import LLMService
from utils.session_manager import (
    initialize_session,
    add_message,
    get_messages
)

# -------- CONFIG --------
st.set_page_config(page_title="TalentScout AI Assistant", layout="centered")
st.title("🤖 TalentScout - AI Hiring Assistant")

# -------- INITIALIZE --------
initialize_session()
llm = LLMService()

# -------- INITIAL GREETING --------
if len(get_messages()) == 0:
    greeting = """
Hello 👋 Welcome to TalentScout!

I will assist you in the initial screening process.

Type 'exit' anytime to end the conversation.
"""
    add_message("assistant", greeting)

# -------- DISPLAY CHAT --------
for message in get_messages():
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# -------- USER INPUT --------
user_input = st.chat_input("Type your response here...")

# =========================
# USER-DRIVEN STAGES
# =========================
if user_input:
    add_message("user", user_input)

    # EXIT
    if user_input.lower() in ["exit", "quit", "bye"]:
        add_message("assistant", "Thank you for your time! Our team will review your profile.")
        st.session_state.stage = "end"

    # GREETING → ASK DETAILS
    elif st.session_state.stage == "greeting":
        add_message("assistant", """
Please provide the following details in this format:

Name:
Email:
Phone:
Years of Experience:
Desired Role:
Location:
""")
        st.session_state.stage = "collect_info"

    # STORE BASIC INFO
    elif st.session_state.stage == "collect_info":
        st.session_state.candidate_info["details"] = user_input
        add_message("assistant", "Great! Now please list your Tech Stack (comma separated).")
        st.session_state.stage = "collect_stack"

    # STORE STACK
    elif st.session_state.stage == "collect_stack":
        stacks = [s.strip() for s in user_input.split(",") if s.strip()]

        if not stacks:
            add_message("assistant", "Please enter at least one valid technology.")
        else:
            st.session_state.tech_stack = stacks
            st.session_state.current_stack_index = 0
            st.session_state.stage = "ask_questions"

    # STORE ANSWERS
    elif st.session_state.stage == "collect_answers":

        current_stack = st.session_state.tech_stack[
            st.session_state.current_stack_index
        ]

        st.session_state.answers[current_stack]["response"] = user_input
        st.session_state.current_stack_index += 1

        if st.session_state.current_stack_index < len(st.session_state.tech_stack):
            st.session_state.stage = "ask_questions"
        else:
            st.session_state.stage = "evaluate"

    st.rerun()


# =========================
# SYSTEM-DRIVEN STAGES
# =========================

# -------- ASK QUESTIONS --------
if st.session_state.stage == "ask_questions":

    current_stack = st.session_state.tech_stack[
        st.session_state.current_stack_index
    ]

    prompt = f"""
Generate exactly 5 short, one-line answer type technical interview questions 
to assess proficiency in {current_stack}.

Rules:
- Each question must require a brief answer (1-2 lines max).
- Each question must be under 15 words.
- Do NOT ask descriptive or essay questions.
- Do NOT include explanations.
- Return only numbered questions (1 to 5).
- Do NOT add any extra text before or after the questions.
"""

    messages = [
        {"role": "system", "content": "You are a technical interviewer."},
        {"role": "user", "content": prompt},
    ]

    questions = llm.generate_response(messages)

    st.session_state.answers[current_stack] = {
        "questions": questions,
        "response": None
    }

    add_message(
        "assistant",
        f"### Questions for {current_stack}:\n{questions}\n\nPlease provide your answers."
    )

    st.session_state.stage = "collect_answers"
    st.rerun()


# -------- EVALUATION --------
if st.session_state.stage == "evaluate":

    evaluation_prompt = f"""
You are a strict senior technical evaluator.

The candidate answered 5 short-answer questions per technology.

For each technology:
1. Evaluate each answer briefly.
2. Assign marks out of 2 per question.
3. Calculate total score out of 10.
4. Provide concise feedback (max 3 lines).
5. Give final verdict: Strong / Moderate / Weak.

Be objective and strict.

Candidate Data:
{st.session_state.answers}
"""

    messages = [
        {"role": "system", "content": "You are a senior technical evaluator."},
        {"role": "user", "content": evaluation_prompt},
    ]

    evaluation = llm.generate_response(messages)

    add_message("assistant", f"## Evaluation Results:\n{evaluation}")

    st.session_state.stage = "end"
    st.rerun()