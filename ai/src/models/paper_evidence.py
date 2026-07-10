from dataclasses import dataclass

from models.retrieved_chunk import RetrievedChunk


@dataclass
class PaperEvidence:
    """
    Represents all retrieved evidence belonging
    to a single research paper.
    """

    paper_title: str

    chunks: list[RetrievedChunk]