# /// script
# dependencies = ["requests < 3.0", "rich","BeautifulSoup4","fastapi","scipy","pillow","pytesseract","uvicorn","pydantic","openai","numpy","tiktoken","python-dotenv"]
# ///

import os
import json
import base64
import io
from typing import Optional, List
from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
from PIL import Image
import pytesseract
import openai
import numpy as np
from scipy.spatial.distance import cosine

from retriever.load_data import load_data
from retriever.embedding import get_embedding
app = FastAPI()

data=[]
# Request schema
class QuestionRequest(BaseModel):
    question: str
    image: Optional[str] = None  # base64 string

@app.on_event("startup")
def startup():
    global data
    data = load_data()
    print(f"📚 Total records loaded: {len(data)}")

@app.post("/api/")
async def answer_query(query: QuestionRequest):
    question = query.question
    image_text = ""

    # If image is provided, do OCR
    if query.image:
        try:
            image_bytes = base64.b64decode(query.image)
            image = Image.open(io.BytesIO(image_bytes))
            image_text = pytesseract.image_to_string(image)
            question += "\n" + image_text
        except Exception as e:
            return {"error": f"Failed to decode or read image: {str(e)}"}

    try:
        query_vec = get_embedding(question)
    except Exception as e:
        return {"error": f"Embedding failed: {str(e)}"}

    # Cosine similarity
    ranked = sorted(data, key=lambda x: cosine(query_vec, x["embedding"]))
    top_results = ranked[:2]

    return {
        "answer": top_results[0]["text"] if top_results else "No answer found.",
        "links": [
            {"url": r.get("url", ""), "text": r.get("text", "")}
            for r in top_results
        ]
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)




