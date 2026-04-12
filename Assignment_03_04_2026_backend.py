from fastapi import FastAPI
from pydantic import BaseModel
import pickle

app = FastAPI()

# Load the trained model
with open('fake_news_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Define what the chatbot expects to receive
class NewsItem(BaseModel):
    text: str

@app.post("/analyze-news")
async def analyze(news: NewsItem):
    # Predict if the text is real or fake
    prediction = model.predict([news.text])[0]
    
    # Format the chatbot's response
    if prediction == 1:
        reply = "✅ Based on my analysis, this news appears to be **REAL**."
    else:
        reply = "🚨 Warning: This news contains patterns typically associated with **FAKE** news. Please verify with trusted sources."
        
    return {"bot_response": reply}