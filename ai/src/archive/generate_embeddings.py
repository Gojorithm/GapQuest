from sentence_transformers import SentenceTransformer

# Load the model only once
model = SentenceTransformer("all-MiniLM-L6-v2")


def generate_embedding(text):
    """
    Generates an embedding for a piece of text.
    """

    embedding = model.encode(text)

    return embedding


if __name__ == "__main__":

    sentence = "Forest fire detection using deep learning."

    embedding = generate_embedding(sentence)

    print("Sentence:")
    print(sentence)

    print("\nEmbedding length:")
    print(len(embedding))

    print("\nFirst 10 values:")
    print(embedding[:10])


# from sentence_transformers import SentenceTransformer

# # Load a pre-trained embedding model
# model = SentenceTransformer("all-MiniLM-L6-v2")

# sentence = "Forest fire detection using deep learning."

# embedding = model.encode(sentence)

# print("Sentence:")
# print(sentence)

# print("\nEmbedding length:")
# print(len(embedding))

# print("\nFirst 10 values:")
# print(embedding[:10])