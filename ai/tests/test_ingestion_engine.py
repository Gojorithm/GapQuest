from preprocessing.document_processor import DocumentProcessor

from ai.embedding_engine import EmbeddingEngine

from database.vector_store import VectorStore

from ingestion.ingestion_engine import IngestionEngine


print("Loading Document Processor...")
processor = DocumentProcessor()

print("\nLoading Embedding Engine...")
embedding_engine = EmbeddingEngine()

print("\nConnecting to Vector Database...")
vector_store = VectorStore()

print("\nClearing database...")
vector_store.clear()

print("\nCreating Ingestion Engine...")
engine = IngestionEngine(
    document_processor=processor,
    embedding_engine=embedding_engine,
    vector_store=vector_store
)

print("\nStarting ingestion...\n")

engine.ingest_pdf(
    "papers/Forest_fire.pdf"
)

print("\n" + "=" * 80)

print("Database contains")

print(vector_store.count())

print("chunks.")