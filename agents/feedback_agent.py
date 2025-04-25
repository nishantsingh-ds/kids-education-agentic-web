# backend/agents/feedback_agent.py
def run_feedback_agent(feedback):
    if not feedback:
        return "No feedback given."
    # Here, we could log to a database, file, or future analysis tool
    print(f"🧠 Feedback received: {feedback}")
    return "Thank you for your feedback!"
