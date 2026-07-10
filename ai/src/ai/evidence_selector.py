from models.retrieved_chunk import RetrievedChunk


class EvidenceSelector:
    """
    Selects the best evidence from the retrieved chunks.

    The Retriever is responsible for finding relevant chunks.

    The EvidenceSelector is responsible for deciding
    which of those chunks should actually be shown
    to the LLM.

    This keeps retrieval and reasoning separate.
    """

    def __init__(self):
        pass


    def select(
        self,
        retrieved_chunks: list[RetrievedChunk],
        max_chunks: int = 20
    ) -> list[RetrievedChunk]:
        """
        Select diverse chunks based on section and paper.

        Tries to avoid duplicate sections from the same paper while
        still keeping the highest similarity chunks.
        """

        selected_chunks = []

        seen = set()

        for retrieved_chunk in retrieved_chunks:

            paper = retrieved_chunk.chunk.metadata.title.lower()

            section = (
                retrieved_chunk.chunk.hierarchy.main_section.lower()
                if retrieved_chunk.chunk.hierarchy.main_section
                else "unknown"
            )

            key = (paper, section)

            if key in seen:
                continue

            selected_chunks.append(retrieved_chunk)
            seen.add(key)

            if len(selected_chunks) >= max_chunks:
                break

        return selected_chunks

    # def select(
    #     self,
    #     retrieved_chunks: list[RetrievedChunk],
    #     max_chunks: int = 8
    # ) -> list[RetrievedChunk]:
    #     """
    #     Select diverse evidence.

    #     Rule:
    #     Keep only the first chunk from each paper.

    #     This prevents one paper from dominating
    #     the LLM context.
    #     """

    #     selected_chunks = []

    #     seen_papers = set()

    #     for retrieved_chunk in retrieved_chunks:

    #         paper_title = (
    #             retrieved_chunk.chunk.metadata.title
    #         )

    #         if paper_title in seen_papers:
    #             continue

    #         selected_chunks.append(
    #             retrieved_chunk
    #         )

    #         seen_papers.add(
    #          paper_title
    #         )

    #         if len(selected_chunks) >= max_chunks:
    #             break

    #     return selected_chunks

    # def select(
    #     self,
    #     retrieved_chunks: list[RetrievedChunk],
    #     max_chunks: int = 8
    # ) -> list[RetrievedChunk]:
    #     """
    #     Select the best evidence for the LLM.

    #     Current Version:
    #     Simply returns the first N retrieved chunks.

    #     Future Versions:
    #     - Remove duplicate chunks
    #     - Prefer multiple papers
    #     - Prefer different sections
    #     - Maximize evidence diversity
    #     """

    #     return retrieved_chunks[:max_chunks]