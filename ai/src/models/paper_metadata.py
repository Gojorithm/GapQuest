from dataclasses import dataclass
from typing import Optional


@dataclass
class PaperMetadata:
    """
    Stores metadata describing an entire research paper.
    """

    title: str

    authors: Optional[list[str]] = None

    year: Optional[int] = None

    doi: Optional[str] = None

    publisher: Optional[str] = None

    journal: Optional[str] = None

    conference: Optional[str] = None

    filename: Optional[str] = None

    source_path: Optional[str] = None