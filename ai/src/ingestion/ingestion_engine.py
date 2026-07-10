from preprocessing.document_processor import DocumentProcessor

from ai.embedding_engine import EmbeddingEngine

from database.vector_store import VectorStore


class IngestionEngine:
    """
    Responsible for processing PDFs and storing
    them inside ChromaDB.
    """

    def __init__(
        self,
        document_processor: DocumentProcessor,
        embedding_engine: EmbeddingEngine,
        vector_store: VectorStore
    ):

        self.document_processor = document_processor
        self.embedding_engine = embedding_engine
        self.vector_store = vector_store

    def ingest_pdf(
        self,
        pdf_path: str
    ):

        print(f"\nProcessing: {pdf_path}")

        knowledge_chunks = (
            self.document_processor.process_pdf(
                pdf_path
            )
        )

        print(
            f"{len(knowledge_chunks)} chunks created."
        )

        # Create embeddings
        for chunk in knowledge_chunks:

            chunk.embedding = self.embedding_engine.embed(
                chunk.text
            )

        # Store everything
        self.vector_store.add_chunks(
            knowledge_chunks
        )

        print("✓ PDF successfully indexed.")