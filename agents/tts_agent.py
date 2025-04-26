from gtts import gTTS
import os
import uuid
import time

def run_tts_agent(text, language="en"):
    try:
        # Sleep for a second to avoid rate limit
        time.sleep(1)

        tts = gTTS(text=text, lang=language)
        
        output_dir = "static/audio"
        os.makedirs(output_dir, exist_ok=True)
        
        filename = f"{output_dir}/{uuid.uuid4().hex}.mp3"
        tts.save(filename)
        
        return filename

    except Exception as e:
        print(f"Error in TTS Agent: {e}")
        return None
