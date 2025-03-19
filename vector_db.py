import chromadb
from langchain_openai import OpenAIEmbeddings

# Initialize ChromaDB for storing document vectors
chroma_client = chromadb.PersistentClient(path="./data")

def store_documents(texts):
    """Store knowledge into ChromaDB"""
    embedding_function = OpenAIEmbeddings()
    
    # Ensure collection exists
    collection = chroma_client.get_or_create_collection("knowledge_base")
    
    for i, text in enumerate(texts):
        collection.add(ids=[str(i)], documents=[text], embeddings=[embedding_function.embed_query(text)])
    
    print("✅ Documents stored successfully in ChromaDB!")

def retrieve_docs(query):
    """Retrieve relevant documents for RAG"""
    try:
        collection = chroma_client.get_or_create_collection("knowledge_base")
    except Exception as e:
        print(f"Error retrieving collection: {e}")
        collection = chroma_client.create_collection("knowledge_base")
    results = collection.query(query_texts=[query], n_results=3)
    return results['documents'] if results else []
