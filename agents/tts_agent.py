# agents/tts_agent.py

from gtts import gTTS
import os
import uuid

def run_tts_agent(text, language="en"):
    try:
        tts = gTTS(text=text, lang="en", tld="co.uk")

        
        # Save the audio file
        output_dir = "static/audio"
        os.makedirs(output_dir, exist_ok=True)
        
        filename = f"{output_dir}/{uuid.uuid4().hex}.mp3"
        tts.save(filename)
        
        return filename

    except Exception as e:
        print(f"Error in TTS Agent: {e}")
        return None
