from ai.embedding_engine import EmbeddingEngine
from ai.retriever import Retriever
from database.vector_store import VectorStore

from models.knowledge_chunk import KnowledgeChunk
from models.paper_metadata import PaperMetadata
from models.section_hierarchy import SectionHierarchy


metadata = PaperMetadata(
    title="Forest Fire Detection Paper"
)

hierarchy = SectionHierarchy(
    main_section="Introduction"
)

chunk = KnowledgeChunk(
    chunk_id="chunk_001",
    metadata=metadata,
    hierarchy=hierarchy,
    chunk_number=1,
    word_count=15,
    text="Deep learning methods have significantly improved forest fire detection accuracy."
)

print("Loading embedding engine...")
embedding_engine = EmbeddingEngine()

print("\nGenerating embedding...")
chunk.embedding = embedding_engine.embed(chunk.text)

print("✓ Embedding ready.")

print("\nConnecting to vector database...")
vector_store = VectorStore()

print("\nResetting database...")

try:
    vector_store.collection.delete(ids=["chunk_001"])
except:
    pass

vector_store.add_chunks([chunk])

print("✓ Chunk stored.")

print("\nCreating Retriever...")

retriever = Retriever(
    embedding_engine=embedding_engine,
    vector_store=vector_store
)

print("✓ Retriever ready.")

print("\nSearching...\n")

results = retriever.retrieve(
    "deep learning for wildfire detection",
    top_k=3
)

print("=" * 80)


for i, result in enumerate(results, start=1):

    print(f"\nResult #{i}")

    print("-" * 80)

    print("Similarity :", round(result.similarity, 4))

    print("Distance   :", round(result.distance, 4))

    print("Paper      :", result.chunk.metadata.title)

    print("Section    :", result.chunk.hierarchy.main_section)

    print("Words      :", result.chunk.word_count)

    print("\nText:\n")

    print(result.chunk.text)

# for i, result in enumerate(results, start=1):

#     print(f"\nResult #{i}")

#     print("-" * 80)

#     print("Similarity :", round(result["similarity"], 4))

#     print("Distance   :", round(result["distance"], 4))

#     print("Metadata   :", result["metadata"])

#     print("\nText:")

#     print(result["text"])