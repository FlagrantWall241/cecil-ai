import os
from fastapi import FastAPI
from pydantic import BaseModel
import openai

# Create FastAPI app
app = FastAPI(title="Cecil AI")

# Get OpenAI API key from environment variable
openai.api_key = os.environ.get("OPENAI_API_KEY")

# Define request model
class Request(BaseModel):
    prompt: str

# Define AI endpoint
@app.post("/ai")
async def cecil_ai(request: Request):
    try:
        # Call OpenAI API
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=request.prompt,
            max_tokens=150,
            temperature=0.7
        )
        answer = response.choices[0].text.strip()
        return {"response": f"Cecil AI says: {answer}"}
    except Exception as e:
        return {"response": f"Error: {str(e)}"}
