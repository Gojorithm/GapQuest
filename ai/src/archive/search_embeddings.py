import chromadb

from archive.generate_embeddings import generate_embedding

# Connect to ChromaDB
client = chromadb.PersistentClient(path="data/chroma_db")

collection = client.get_collection("research_papers")


def search_similar(query, n_results=1):
    """
    Search for similar research papers.
    """

    query_embedding = generate_embedding(query).tolist()

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=n_results
    )

    return results


if __name__ == "__main__":

    query = "Deep learning methods for wildfire detection"

    results = search_similar(query)

    print("\nSearch Query:")
    print(query)

    print("\nMost Similar Document:\n")
    print(results["documents"][0][0])




# import chromadb
# from sentence_transformers import SentenceTransformer

# # Load embedding model
# model = SentenceTransformer("all-MiniLM-L6-v2")

# # Connect to ChromaDB
# client = chromadb.PersistentClient(path="data/chroma_db")

# collection = client.get_collection("research_papers")

# query = "Deep learning methods for wildfire detection"

# query_embedding = model.encode(query).tolist()

# results = collection.query(
#     query_embeddings=[query_embedding],
#     n_results=1
# )

# print("\nSearch Query:")
# print(query)

# print("\nMost Similar Document:\n")
# print(results["documents"][0][0])