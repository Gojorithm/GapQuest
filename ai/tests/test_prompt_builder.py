from preprocessing.document_processor import DocumentProcessor
from ai.embedding_engine import EmbeddingEngine
from database.vector_store import VectorStore
from ingestion.ingestion_engine import IngestionEngine
from ai.retriever import Retriever

from ai.paper_analyzer import PaperAnalyzer
from ai.literature_evidence_builder import LiteratureEvidenceBuilder
from ai.prompt_builder import PromptBuilder


print("Loading components...\n")

document_processor = DocumentProcessor()
embedding_engine = EmbeddingEngine()
vector_store = VectorStore()

vector_store.clear()

ingestion = IngestionEngine(
    document_processor=document_processor,
    embedding_engine=embedding_engine,
    vector_store=vector_store
)

print("Indexing paper...\n")

ingestion.ingest_pdf(
    "papers/Forest_fire.pdf"
)

retriever = Retriever(
    embedding_engine=embedding_engine,
    vector_store=vector_store
)

print("Retrieving chunks...\n")

retrieved_chunks = retriever.retrieve(
    "forest fire detection",
    top_k=20
)

paper_analyzer = PaperAnalyzer()

papers = paper_analyzer.group_by_paper(
    retrieved_chunks
)

builder = LiteratureEvidenceBuilder()

papers = builder.build(
    papers
)

prompt_builder = PromptBuilder()

prompt = prompt_builder.build_prompt(
    papers
)

print("\n")
print("=" * 80)
print("FINAL PROMPT")
print("=" * 80)
print(prompt)