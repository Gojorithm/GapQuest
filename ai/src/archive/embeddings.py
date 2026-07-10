import json
import chromadb

from archive.generate_embeddings import generate_embedding

# Create ChromaDB client
client = chromadb.PersistentClient(path="data/chroma_db")

# Create or load collection
collection = client.get_or_create_collection(
    name="research_papers"
)


def store_embedding(text, chunk_id, metadata):
    """
    Store a paper inside ChromaDB.
    """

    embedding = generate_embedding(text).tolist()

    collection.add(
        documents=[text],
        embeddings=[embedding],
        ids=[chunk_id],
        metadatas=[metadata]
    )


if __name__ == "__main__":

    with open(
        "outputs/paper_data_cleaned.json",
        "r",
        encoding="utf-8"
    ) as f:

        data = json.load(f)

    text = data["abstract"]

    # store_embedding(text, "paper1")
    store_embedding(
    text,
    "paper1",
    {
        "paper": "paper1"
    }
    )

    print("✅ Paper stored successfully!")


# import json
# import chromadb
# from generate_embeddings import generate_embedding
# # from sentence_transformers import SentenceTransformer

# # # Load embedding model
# # model = SentenceTransformer("all-MiniLM-L6-v2")

# # Create ChromaDB client
# client = chromadb.PersistentClient(path="data/chroma_db")

# # Create or load collection
# collection = client.get_or_create_collection(name="research_papers")

# # Load cleaned paper
# with open("outputs/paper_data_cleaned.json", "r", encoding="utf-8") as f:
#     data = json.load(f)

# # We'll store the abstract for now
# text = data["abstract"]

# # Generate embedding
# embedding = generate_embedding(text).tolist()

# # Store in ChromaDB
# collection.add(
#     documents=[text],
#     embeddings=[embedding],
#     ids=["paper1"]
# )

# print("✅ Paper stored successfully!")