import chromadb
from chromadb.config import Settings

from models.knowledge_chunk import KnowledgeChunk


class VectorStore:
    """
    Wrapper around ChromaDB used by GapQuest.

    Responsible for storing and retrieving KnowledgeChunks.
    """

    def __init__(
        self,
        db_path: str = "database/chroma_db",
        collection_name: str = "research_chunks"
    ):

        print("Initializing ChromaDB...")

        self.client = chromadb.PersistentClient(
            path=db_path,
            settings=Settings(
                anonymized_telemetry=False
            )
        )

        self.collection = self.client.get_or_create_collection(
            name=collection_name
        )

        print("✓ ChromaDB ready.")
        print(f"Collection: {collection_name}")

    # ======================================================
    # Add chunks
    # ======================================================

    def add_chunks(self, chunks: list[KnowledgeChunk]):

        ids = []
        embeddings = []
        documents = []
        metadatas = []

        for chunk in chunks:

            ids.append(chunk.chunk_id)

            embeddings.append(chunk.embedding)

            documents.append(chunk.text)

            metadatas.append({

                "paper_title": chunk.metadata.title,

                "main_section": chunk.hierarchy.main_section,

                "subsection": chunk.hierarchy.subsection,

                "subsubsection": chunk.hierarchy.subsubsection,

                "chunk_number": chunk.chunk_number,

                "word_count": chunk.word_count

            })

        self.collection.add(

            ids=ids,

            embeddings=embeddings,

            documents=documents,

            metadatas=metadatas

        )

        print(f"✓ Stored {len(chunks)} chunks.")

    # ======================================================
    # Search
    # ======================================================

    def search(self, query_embedding, top_k=5):

        results = self.collection.query(

            query_embeddings=[query_embedding],

            n_results=top_k

        )

        return results

    # ======================================================
    # Count
    # ======================================================

    def count(self):

        return self.collection.count()

    # ======================================================
    # Clear database
    # ======================================================

    def clear(self):

        ids = self.collection.get()["ids"]

        if ids:

            self.collection.delete(ids=ids)

            print("✓ Database cleared.")

        else:

            print("Database already empty.")