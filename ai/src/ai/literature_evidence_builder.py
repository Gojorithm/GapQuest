from models.paper_evidence import PaperEvidence


class LiteratureEvidenceBuilder:
    """
    Cleans and compresses each paper into its
    most valuable evidence before sending it
    to the LLM.
    """

    # Importance of each section for research understanding
    SECTION_PRIORITY = {

        "abstract": 100,

        "discussion": 95,

        "future work": 95,

        "conclusion": 90,

        "introduction": 85,

        "related work": 85,

        "literature review": 85,

        "results": 80,

        "experiment": 75,

        "method": 60,

        "methodology": 60,

        "dataset": 0,

        "implementation": 20,

        "reference": -1000,
        "references": -1000,

        "appendix": -1000,

        "acknowledgement": -1000,
        "acknowledgements": -1000,
    }

    # Final reading order
    SECTION_ORDER = {

        "abstract": 0,

        "introduction": 1,

        "related work": 2,
        "literature review": 2,

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

    def build(
        self,
        papers: list[PaperEvidence],
        max_chunks_per_paper: int = 9
    ) -> list[PaperEvidence]:

        cleaned_papers = []

        for paper in papers:

            best_sections = {}

            for retrieved_chunk in paper.chunks:

                section = (
                    retrieved_chunk.chunk.hierarchy.main_section.lower()
                    if retrieved_chunk.chunk.hierarchy.main_section
                    else "abstract"
                )

                keep = True
                section_key = "other"

                for keyword, score in self.SECTION_PRIORITY.items():

                    if keyword in section:

                        section_key = keyword

                        if score < 0:
                            keep = False

                        break

                if not keep:
                    continue

                existing = best_sections.get(section_key)

                if (
                    existing is None
                    or retrieved_chunk.similarity > existing.similarity
                ):
                    best_sections[section_key] = retrieved_chunk

            selected_chunks = list(best_sections.values())

            selected_chunks.sort(
                key=self._section_order
            )

            cleaned_papers.append(

                PaperEvidence(
                    paper_title=paper.paper_title,
                    chunks=selected_chunks[:max_chunks_per_paper]
                )

            )

        return cleaned_papers

    def _section_order(self, retrieved_chunk):

        section = (
            retrieved_chunk.chunk.hierarchy.main_section.lower()
            if retrieved_chunk.chunk.hierarchy.main_section
            else "abstract"
        )

        for keyword, order in self.SECTION_ORDER.items():

            if keyword in section:
                return order

        return 100