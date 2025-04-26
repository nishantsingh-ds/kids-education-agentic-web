import os
import requests
import base64

GOOGLE_TTS_API_KEY = os.getenv("GOOGLE_TTS_API_KEY")

def text_to_speech(text, output_file_path):
    url = f"https://texttospeech.googleapis.com/v1/text:synthesize?key={GOOGLE_TTS_API_KEY}"

    payload = {
        "input": {
            "text": text
        },
        "voice": {
            "languageCode": "en-US",
            "name": "en-US-Standard-C",
            "ssmlGender": "FEMALE"
        },
        "audioConfig": {
            "audioEncoding": "MP3"
        }
    }

    headers = {
        "Content-Type": "application/json"
    }

    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()

        audio_content = response.json()["audioContent"]

        with open(output_file_path, "wb") as out:
            out.write(base64.b64decode(audio_content))

        print(f"Audio content written to file {output_file_path}")

    except Exception as e:
        print(f"Error generating TTS audio: {e}")

def run_tts_agent(text, output_file_path="static/audio/output.mp3"):
    text_to_speech(text, output_file_path)
    return output_file_path
