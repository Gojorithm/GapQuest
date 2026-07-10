from ai.embedding_engine import EmbeddingEngine

from models.paper_metadata import PaperMetadata
from models.section_hierarchy import SectionHierarchy
from models.knowledge_chunk import KnowledgeChunk


metadata = PaperMetadata(
    title="Test Paper"
)

hierarchy = SectionHierarchy(
    main_section="Introduction",
    subsection="",
    subsubsection=""
)

chunk = KnowledgeChunk(
    chunk_id="test_001",

    metadata=metadata,

    hierarchy=hierarchy,

    chunk_number=1,

    word_count=7,

    text="Forest fires are becoming increasingly dangerous."
)

engine = EmbeddingEngine()

embedded_chunk = engine.embed_chunk(chunk)

print("\nEmbedding Length:", len(embedded_chunk.embedding))

print("\nFirst 10 values:")

print(embedded_chunk.embedding[:10])