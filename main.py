import os

from fastapi import FastAPI
from fastapi.responses import FileResponse
from dotenv import load_dotenv
from google import genai


# Load .env file
load_dotenv()

# Create FastAPI app
app = FastAPI()

# Connect Gemini
client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


# Home page
@app.get("/")
def home():
    return FileResponse("index.html")


# Ask Gemini
@app.get("/ask")
def ask(question: str):
    response = client.models.generate_content(
        model="gemini-3.8-flash",
        contents=question
    )

    return {
        "question": question,
        "answer": response.text
    }