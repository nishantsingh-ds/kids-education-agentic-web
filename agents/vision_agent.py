import os
import requests

async def run_vision_agent(file):
    try:
        image_bytes = await file.read()
        headers = {
            "Authorization": f"Bearer {os.getenv('HF_API_TOKEN')}",
            "Content-Type": "application/octet-stream"
        }

        response = requests.post(
            "https://api-inference.huggingface.co/models/Salesforce/blip-image-captioning-base",
            headers=headers,
            data=image_bytes  # 🚨 send raw image data, NOT base64
        )

        result = response.json()
        print("✅ Hugging Face Output:", result)

        if isinstance(result, list) and "generated_text" in result[0]:
            return [result[0]["generated_text"]]
        else:
            return {"error": str(result)}

    except Exception as e:
        print("❌ Hugging Face Error:", e)
        return {"error": str(e)}
