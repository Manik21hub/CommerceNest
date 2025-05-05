from fastapi import FastAPI
from pydantic import BaseModel
import spacy

app = FastAPI()
nlp = spacy.load("en_core_web_sm")

class Query(BaseModel):
    text: str

@app.post("/api/chatbot/query")
async def chatbot_query(query: Query):
    doc = nlp(query.text)
    return {
        "response": f"You asked: '{query.text}'",
        "entities": [(ent.text, ent.label_) for ent in doc.ents]
    }
