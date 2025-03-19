import json
from vector_db import retrieve_docs

# Load preloaded CAG knowledge
with open("knowledge_base.json", "r") as f:
    knowledge_base = json.load(f)

def hybrid_chat(query, mode="hybrid"):
    """Choose between CAG, RAG, or Hybrid"""
    
    if mode == "CAG":
        return knowledge_base.get(query, "I don't know that yet.")
    
    elif mode == "RAG":
        docs = retrieve_docs(query)
        return f"🔎 Retrieved from documents:\n{docs}" if docs else "No relevant data found."
    
    elif mode == "hybrid":
        return knowledge_base.get(query, retrieve_docs(query))
    
    return "Invalid mode selected."
