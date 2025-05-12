import os
import requests

async def run_vision_agent(file):
    try:
        image_bytes = await file.read()

        headers = {
            "Authorization": f"Bearer {os.getenv('HF_API_TOKEN')}",
            "Content-Type": "application/octet-stream"
        }

        # Update the endpoint with the new model
        endpoint = "https://api-inference.huggingface.co/models/Salesforce/blip2-opt-2.7b"

        response = requests.post(
            endpoint,
            headers=headers,
            data=image_bytes
        )

        # Debugging information
        print(f"Response Status: {response.status_code}")
        print(f"Response Content: {response.content}")

        # Handle response
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 404:
            return {"error": "Model not found. Check the endpoint URL."}
        elif response.status_code == 401:
            return {"error": "Unauthorized - Invalid API Key"}
        else:
            return {"error": f"Unexpected response: {response.content}"}

    except Exception as e:
        print(f"Exception in Vision Agent: {e}")
        return {"error": str(e)}
