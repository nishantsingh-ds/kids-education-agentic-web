# backend/agents/stt_agent.py
import os
import openai
import io

openai.api_key = os.getenv("OPENAI_API_KEY")

async def run_stt_agent(audio_file):
    audio_data = await audio_file.read()
    file_like = io.BytesIO(audio_data)  # ✅ convert bytes to file-like
    response = openai.Audio.transcribe("whisper-1", file=file_like)
    return response["text"]
