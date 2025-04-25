import os
from dotenv import load_dotenv
load_dotenv()


from fastapi import FastAPI, UploadFile, File, Form
from typing import Optional, Union
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from agents.orchestrator import orchestrate_agent_flow


app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve audio files
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.post("/interact")
async def process_request(
    input_type: str = Form(...),
    output_type: str = Form(...),
    feedback: Optional[str] = Form(None),
    file: Union[UploadFile, str, None] = File(None),
    text: Optional[str] = Form(None)
):
    try:
        # Swagger sends file='' as a string — fix that here
        if isinstance(file, str) or file is None or file == "":
            file = None

        # Validation
        if input_type == "text" and not text:
            return {"error": "Missing 'text' input for text mode."}
        if input_type in ["audio", "image"] and file is None:
            return {"error": f"Missing file input for '{input_type}' mode."}
        
        input_data = file if file and not isinstance(file, str) else text

        result = await orchestrate_agent_flow(input_type, input_data, output_type, feedback)
        return result
    except Exception as e:
        return {"error": str(e)}