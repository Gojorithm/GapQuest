from preprocessing.extract_pdf import extract_markdown
from preprocessing.clean_text import clean_markdown
from preprocessing.markdown_parser import markdown_chunk
from preprocessing.chunk_builder import ChunkBuilder

from models.knowledge_chunk import KnowledgeChunk


class DocumentProcessor:
    """
    Complete preprocessing pipeline.

    Workflow:

        PDF
            ↓
        Markdown Extraction
            ↓
        Markdown Cleaning
            ↓
        Semantic Chunking
            ↓
        KnowledgeChunk Objects
    """

    def __init__(self):

        self.chunk_builder = ChunkBuilder()

    def process_pdf(
        self,
        pdf_path: str
    ) -> list[KnowledgeChunk]:

        # Step 1
        markdown = extract_markdown(pdf_path)

        # Step 2
        cleaned_markdown = clean_markdown(markdown)

        # Step 3
        parsed_chunks = markdown_chunk(cleaned_markdown)

        # Step 4
        knowledge_chunks = self.chunk_builder.build(
            parsed_chunks
        )

        return knowledge_chunks