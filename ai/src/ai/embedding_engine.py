from models.knowledge_chunk import KnowledgeChunk
from llama_index.embeddings.huggingface import HuggingFaceEmbedding


class EmbeddingEngine:
    """
    EmbeddingEngine

    Responsible for converting research paper text into dense semantic
    vector embeddings using the BAAI/bge-base-en-v1.5 model.

    These embeddings are later stored inside the vector database
    (ChromaDB) and used for semantic search and retrieval.
    """

    def __init__(self) -> None:

        print("Loading BGE embedding model...")

        self.model = HuggingFaceEmbedding(
            model_name="BAAI/bge-base-en-v1.5"
        )

        print("✓ Embedding model ready.\n")

    def embed(self, text: str) -> list[float]:
        """
        Generate an embedding for a single piece of text.
        """

        return self.model.get_text_embedding(text)

    def embed_chunk(self, chunk: KnowledgeChunk) -> KnowledgeChunk:
        """
        Generate an embedding for a single KnowledgeChunk.
        """

        if chunk.embedding is None:
            chunk.embedding = self.embed(chunk.text)

        return chunk

    def embed_chunks(
        self,
        chunks: list[KnowledgeChunk]
    ) -> list[KnowledgeChunk]:
        """
        Generate embeddings for a list of KnowledgeChunks.

        Existing embeddings are skipped to avoid unnecessary
        recomputation.
        """

        total = len(chunks)

        print(f"Generating embeddings for {total} chunks...\n")

        for index, chunk in enumerate(chunks, start=1):

            if chunk.embedding is None:
                chunk.embedding = self.embed(chunk.text)

            print(f"[{index}/{total}] Embedded Chunk {chunk.chunk_id}")

        print("\n✓ All embeddings generated successfully.\n")

        return chunks