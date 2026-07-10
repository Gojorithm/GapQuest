from models.paper_evidence import PaperEvidence
from collections import defaultdict

from models.retrieved_chunk import RetrievedChunk


class PaperAnalyzer:
    """
    Groups retrieved chunks by paper and sorts them
    into the natural flow of a research paper.
    """

    SECTION_ORDER = {

        "abstract": 0,

        "introduction": 1,

        "related work": 2,

        "literature review": 2,

        "background": 2,

        "method": 3,

        "methodology": 3,

        "dataset": 4,

        "experiment": 5,

        "results": 6,

        "discussion": 7,

        "future work": 8,

        "conclusion": 9
    }

    def __init__(self):
        pass

    # ======================================================
    # Group retrieved chunks by paper
    # ======================================================
    def group_by_paper(
        self,
        retrieved_chunks: list[RetrievedChunk]
    ) -> list[PaperEvidence]:

        grouped = {}

        # -----------------------------
        # Group chunks by paper
        # -----------------------------

        for retrieved_chunk in retrieved_chunks:

            title = retrieved_chunk.chunk.metadata.title

            if title not in grouped:
                grouped[title] = []

            grouped[title].append(retrieved_chunk)

        # -----------------------------
        # Sort sections inside each paper
        # -----------------------------

        papers = []

        for title, chunks in grouped.items():

            sorted_chunks = self._sort_sections(chunks)

            papers.append(

                PaperEvidence(
                    paper_title=title,
                    chunks=sorted_chunks
                )

            )

        return papers
    # def group_by_paper(
    #     self,
    #     retrieved_chunks: list[RetrievedChunk]
    # ):

    #     grouped = defaultdict(list)

    #     for retrieved_chunk in retrieved_chunks:

    #         paper = retrieved_chunk.chunk.metadata.title

    #         grouped[paper].append(retrieved_chunk)

    #     # Sort every paper before returning
    #     sorted_grouped = {}

    #     for paper, chunks in grouped.items():

    #         sorted_grouped[paper] = self._sort_sections(chunks)

    #     return dict(sorted_grouped)

    # ======================================================
    # Internal section sorter
    # ======================================================

    def _sort_sections(
        self,
        chunks: list[RetrievedChunk]
    ):

        def get_section_order(retrieved_chunk):

            section = (
                retrieved_chunk.chunk.hierarchy.main_section.lower()
                if retrieved_chunk.chunk.hierarchy.main_section
                else "abstract"
            )

            for keyword, order in self.SECTION_ORDER.items():

                if keyword in section:

                    return order

            return 100

        return sorted(
            chunks,
            key=get_section_order
        )