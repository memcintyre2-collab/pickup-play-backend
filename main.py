from fastapi import FastAPI
from pydantic import BaseModel
from openai import OpenAI
import requests  # import at top

app = FastAPI()

# Your OpenAI API key
client = OpenAI(api_key="YOUR_OPENAI_API_KEY")

# Google Sheet API link
SHEET_URL = "https://opensheet.elk.sh/1Vd6DaCvOlnZ_omVG_xGSj6kUT5OUpt3JGE7jDBXEAsQ/Sheet1"

# Message model
class Message(BaseModel):
    prompt: str

# Home endpoint
@app.get("/")
def home():
    return {"message": "Pickup Play backend running"}

# AI endpoint
@app.post("/ai")
def ai_chat(message: Message):
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": "You help users find pickup sports games."},
            {"role": "user", "content": message.prompt}
        ]
    )
    return {"response": response.choices[0].message.content}

# Google Sheets endpoint
@app.get("/games") 
def get_games():
    response = requests.get(SHEET_URL)
    return response.json()
