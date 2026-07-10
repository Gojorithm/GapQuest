from dataclasses import dataclass
from typing import Optional

from models.paper_metadata import PaperMetadata
from models.section_hierarchy import SectionHierarchy


@dataclass
class KnowledgeChunk:
    """
    Represents a single semantic piece of knowledge extracted from
    a research paper.
    """

    # Unique identifier
    chunk_id: str

    # Information about the paper
    metadata: PaperMetadata

    # Where this chunk belongs in the paper
    hierarchy: SectionHierarchy

    # Original chunk produced by markdown_parser.py
    chunk_number: int

    # If semantic_chunker.py splits this chunk,
    # these become 1, 2, 3, ...
    semantic_chunk_number: int = 1

    # Number of words in this chunk
    word_count: int = 0

    # Actual chunk text
    text: str = ""

    # Vector embedding (generated later)
    embedding: Optional[list[float]] = None