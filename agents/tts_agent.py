# backend/agents/tts_agent.py
import os
from tempfile import NamedTemporaryFile
from elevenlabs import ElevenLabs

api_key = os.getenv("ELEVENLABS_API_KEY")

def run_tts_agent(text):
    try:
        client = ElevenLabs(api_key=api_key)

        # Stream audio
        audio_stream = client.generate(
            text=text,
            voice="Rachel",
            model="eleven_monolingual_v1",
            stream=True  # ✅ Stream chunks
        )

        # Join all chunks into bytes
        audio_bytes = b"".join(audio_stream)

        # Save
        temp_dir = "static/audio"
        os.makedirs(temp_dir, exist_ok=True)

        temp_file = NamedTemporaryFile(delete=False, suffix=".mp3", dir=temp_dir)
        with open(temp_file.name, "wb") as f:
            f.write(audio_bytes)

        audio_url = f"/static/audio/{os.path.basename(temp_file.name)}"
        return audio_url

    except Exception as e:
        print(f"Error in TTS Agent: {e}")
        return str(e)
