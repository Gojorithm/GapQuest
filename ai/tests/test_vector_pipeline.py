from ai.embedding_engine import EmbeddingEngine
from database.vector_store import VectorStore

from models.paper_metadata import PaperMetadata
from models.section_hierarchy import SectionHierarchy
from models.knowledge_chunk import KnowledgeChunk


print("\nCreating fake KnowledgeChunk...")

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

print("✓ Chunk created")


print("\nLoading embedding engine...")

engine = EmbeddingEngine()

chunk.embedding = engine.embed(chunk.text)

print("✓ Embedding generated")


print("\nConnecting to ChromaDB...")

db = VectorStore()

print("\nClearing old test data...")

db.clear()

print("\nAdding chunk...")

db.add_chunks([chunk])

print()

print("Database Count:", db.count())


print("\nSearching...")

query = "deep learning for wildfire detection"

query_embedding = engine.embed(query)

results = db.search(query_embedding)

print("\n========== SEARCH RESULT ==========\n")

print("Document:")

print(results["documents"][0][0])

print()

print("Metadata:")

print(results["metadatas"][0][0])

print()

print("Distance:")

print(results["distances"][0][0])