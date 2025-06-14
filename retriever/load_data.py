# /// script
# dependencies = ["openai","python-dotenv"]
# ///

import os
import json
from dotenv import load_dotenv
import openai

# Load environment variables
load_dotenv()
client = openai.OpenAI(
    api_key=os.getenv("api_key"),
    base_url="https://aipipe.org/openai/v1"
)

DATA_PATH = "data/tds_combined_data.json"

def get_embedding(text):
    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=text
    )
    return response.data[0].embedding

def load_data():
    combined = []

    # Load Discourse.jsonl
    with open("data/Discourse.jsonl") as f:
        for line in f:
            post = json.loads(line)
            content = post.get("content") or post.get("text")
            if content:
                try:
                    print(f"📄 Embedding discourse: {content[:60]}...")
                    embedding = get_embedding(content)
                    combined.append({
                        "text": content,
                        "url": post.get("url", ""),
                        "embedding": embedding
                    })
                except Exception as e:
                    print(f"❌ Embedding failed for discourse post: {e}")

    # Load CourseContentData.json
    with open("data/CourseContentData.jsonl") as f:
        for line in f:
            item = json.loads(line)
            content = item.get("content") or item.get("text")
            if content:
                try:
                    print(f"📘 Embedding course content: {content[:60]}...")
                    embedding = get_embedding(content)
                    combined.append({
                        "text": content,
                        "url": item.get("url", ""),
                        "embedding": embedding
                    })
                except Exception as e:
                    print(f"❌ Embedding failed for course content: {e}")

    # Save data
    os.makedirs("data", exist_ok=True)
    with open(DATA_PATH, "w") as f:
        json.dump(combined, f)

    print(f"✅ Saved {len(combined)} items.")
    return combined

if __name__ == "__main__":
    print("🔍 Running embedding loader...")
    data = load_data()
    print(f"✅ Loaded {len(data)} items with embeddings.")
