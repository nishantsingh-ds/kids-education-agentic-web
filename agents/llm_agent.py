# backend/agents/llm_agent.py
import os
from groq import Groq

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

async def run_llm_agent(prompt):
    response = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content
