import os
import base64
import requests

GOOGLE_TTS_API_KEY = os.getenv("GOOGLE_TTS_API_KEY")  # Your API key should be set as env var

def text_to_speech(text, output_file_path):
    # Define the request payload
    url = f"https://texttospeech.googleapis.com/v1/text:synthesize?key={GOOGLE_TTS_API_KEY}"

    payload = {
        "input": {
            "text": text
        },
        "voice": {
            "languageCode": "en-US",  # or change as needed
            "name": "en-US-Standard-C",  # or use "en-US-Wavenet-D" if you want WaveNet
            "ssmlGender": "FEMALE"  # MALE, FEMALE, or NEUTRAL
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

        # Write the binary content to the output file
        with open(output_file_path, "wb") as out:
            out.write(base64.b64decode(audio_content))

        print(f"Audio content written to file {output_file_path}")

    except Exception as e:
        print(f"Error generating TTS audio: {e}")
