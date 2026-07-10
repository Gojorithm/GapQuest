from ai.embedding_engine import EmbeddingEngine
from database.vector_store import VectorStore

from models.paper_metadata import PaperMetadata
from models.section_hierarchy import SectionHierarchy
from models.knowledge_chunk import KnowledgeChunk
from models.retrieved_chunk import RetrievedChunk


class Retriever:
    """
    Retrieves the most relevant chunks for a user query.
    """

    def __init__(
        self,
        embedding_engine: EmbeddingEngine,
        vector_store: VectorStore
    ):

        self.embedding_engine = embedding_engine
        self.vector_store = vector_store

    def retrieve(
        self,
        query: str,
        top_k: int = 5
    ):

        # Convert the query into an embedding
        query_embedding = self.embedding_engine.embed(query)

        # Search ChromaDB
        results = self.vector_store.collection.query(
            query_embeddings=[query_embedding],
            n_results=top_k
        )

        retrieved_chunks = []

        documents = results["documents"][0]
        metadatas = results["metadatas"][0]
        distances = results["distances"][0]

        for document, metadata, distance in zip(
            documents,
            metadatas,
            distances
        ):

            # Reconstruct PaperMetadata
            paper_metadata = PaperMetadata(
                title=metadata["paper_title"]
            )

            # Reconstruct hierarchy
            hierarchy = SectionHierarchy(
                main_section=metadata["main_section"],
                subsection=metadata["subsection"],
                subsubsection=metadata["subsubsection"]
            )

            # Reconstruct KnowledgeChunk
            chunk = KnowledgeChunk(
                chunk_id="retrieved",
                metadata=paper_metadata,
                hierarchy=hierarchy,
                chunk_number=metadata["chunk_number"],
                word_count=metadata["word_count"],
                text=document
            )

            # Wrap everything into a RetrievedChunk
            retrieved_chunks.append(
                RetrievedChunk(
                    chunk=chunk,
                    similarity=1 - distance,
                    distance=distance
                )
            )

        return retrieved_chunks