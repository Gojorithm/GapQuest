from llama_index.embeddings.huggingface import HuggingFaceEmbedding

print("Loading embedding model...")

embed_model = HuggingFaceEmbedding(
    model_name="BAAI/bge-base-en-v1.5"
)

print("Embedding model loaded!")

vector = embed_model.get_text_embedding(
    "Forest fires are increasing due to climate change."
)

print()

print("Embedding Length:", len(vector))

print()

print(vector[:10])