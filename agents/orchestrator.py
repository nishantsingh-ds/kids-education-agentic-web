# backend/agents/orchestrator.py
from .llm_agent import run_llm_agent
from .stt_agent import run_stt_agent
from .tts_agent import run_tts_agent
from .vision_agent import run_vision_agent
from .feedback_agent import run_feedback_agent

async def orchestrate_agent_flow(input_type, input_data, output_type, feedback=None):
    try:
        # Feedback logging (non-blocking)
        if feedback:
            run_feedback_agent(feedback)

        # 1. Handle Input
        if input_type == "text":
            prompt = input_data
        elif input_type == "audio":
            prompt = await run_stt_agent(input_data)
        elif input_type == "image":
            labels = await run_vision_agent(input_data)  # ✅ simpler
            if isinstance(labels, list):
                label = labels[0]
            else:
                label = labels
            prompt = f"What is {label} in simple words for kids?"
        else:
            return {"error": "Unsupported input type"}

        # 2. Run LLM
        explanation = await run_llm_agent(prompt)

        # 3. Handle Output
        if output_type == "text":
            return {"response": explanation}
        elif output_type == "audio":
            audio_url = run_tts_agent(explanation)
            return {"response": explanation, "audio_url": audio_url}  # ✅ no prefix here
        else:
            return {"error": "Unsupported output type"}

    except Exception as e:
        return {"error": str(e)}
