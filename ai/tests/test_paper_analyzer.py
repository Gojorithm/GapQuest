from preprocessing.document_processor import DocumentProcessor
from ai.embedding_engine import EmbeddingEngine
from database.vector_store import VectorStore
from ingestion.ingestion_engine import IngestionEngine
from ai.retriever import Retriever
from ai.paper_analyzer import PaperAnalyzer

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

print("\nIndexing paper...\n")

ingestion.ingest_pdf("papers/Forest_fire.pdf")

retriever = Retriever(
    embedding_engine=embedding_engine,
    vector_store=vector_store
)

print("\nRetrieving chunks...\n")

retrieved_chunks = retriever.retrieve(
    "research gaps in forest fire detection",
    top_k=20
)

paper_analyzer = PaperAnalyzer()

# # Step 1: Group chunks by paper
# grouped = paper_analyzer.group_by_paper(
#     retrieved_chunks
# )
# paper_analyzer = PaperAnalyzer()

grouped = paper_analyzer.group_by_paper(
    retrieved_chunks
)

# # Step 2: Sort sections into paper order
# grouped = paper_analyzer.sort_sections(
#     grouped
# )

print("\nGrouped & Sorted Papers\n")
print("=" * 70)

for paper in grouped:

    print(f"\n📄 {paper.paper_title}")
    print("-" * 70)

    print(f"Total Selected Chunks: {len(paper.chunks)}\n")

    for i, retrieved_chunk in enumerate(paper.chunks, start=1):

        section = (
            retrieved_chunk.chunk.hierarchy.main_section
            if retrieved_chunk.chunk.hierarchy.main_section
            else "Abstract"
        )

        print(f"{i:02}. {section}")
        print(f"    Similarity : {round(retrieved_chunk.similarity, 3)}")
        print(f"    Preview    : {retrieved_chunk.chunk.text[:120]}...")
        print()

