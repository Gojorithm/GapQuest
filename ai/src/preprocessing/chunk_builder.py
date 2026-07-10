from models.paper_metadata import PaperMetadata
from models.section_hierarchy import SectionHierarchy
from models.knowledge_chunk import KnowledgeChunk


class ChunkBuilder:
    """
    Converts parsed markdown dictionaries into
    KnowledgeChunk objects.
    """

    def build(
        self,
        parsed_chunks: list[dict]
    ) -> list[KnowledgeChunk]:

        knowledge_chunks = []

        for chunk in parsed_chunks:

            metadata = PaperMetadata(
                title=chunk["paper_title"]
            )

            hierarchy = SectionHierarchy(
                main_section=chunk["main_section"],
                subsection=chunk["subsection"],
                subsubsection=chunk["subsubsection"]
            )

            knowledge_chunk = KnowledgeChunk(

                chunk_id=chunk["chunk_id"],

                metadata=metadata,

                hierarchy=hierarchy,

                chunk_number=chunk["chunk_number"],

                word_count=chunk["word_count"],

                text=chunk["text"]

            )

            knowledge_chunks.append(
                knowledge_chunk
            )

        return knowledge_chunks