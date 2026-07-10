from preprocessing.document_processor import DocumentProcessor

from ai.embedding_engine import EmbeddingEngine
from ai.retriever import Retriever

from ai.paper_analyzer import PaperAnalyzer
from ai.literature_evidence_builder import LiteratureEvidenceBuilder

from ai.prompt_builder import PromptBuilder
from ai.llm_provider import LLMProvider
from ai.llm_reasoner import LLMReasoner

from database.vector_store import VectorStore

from ingestion.ingestion_engine import IngestionEngine
from ingestion.folder_ingestion_engine import FolderIngestionEngine


class GapQuest:
    """
    Main interface of the GapQuest AI Engine.

    This class hides all internal AI modules behind
    a simple API.
    """

    def __init__(self):

        print("\nInitializing GapQuest...\n")

        # =====================================================
        # Core Components
        # =====================================================

        self.document_processor = DocumentProcessor()

        self.embedding_engine = EmbeddingEngine()

        self.vector_store = VectorStore()

        # =====================================================
        # Ingestion
        # =====================================================

        self.ingestion_engine = IngestionEngine(
            document_processor=self.document_processor,
            embedding_engine=self.embedding_engine,
            vector_store=self.vector_store
        )

        self.folder_ingestion_engine = FolderIngestionEngine(
            ingestion_engine=self.ingestion_engine
        )

        # =====================================================
        # Retrieval
        # =====================================================

        self.retriever = Retriever(
            embedding_engine=self.embedding_engine,
            vector_store=self.vector_store
        )

        # =====================================================
        # Literature Pipeline
        # =====================================================

        self.paper_analyzer = PaperAnalyzer()

        self.evidence_builder = LiteratureEvidenceBuilder()

        # =====================================================
        # LLM
        # =====================================================

        self.prompt_builder = PromptBuilder()

        self.llm_provider = LLMProvider()

        self.reasoner = LLMReasoner(
            retriever=self.retriever,
            paper_analyzer=self.paper_analyzer,
            evidence_builder=self.evidence_builder,
            llm_provider=self.llm_provider,
            prompt_builder=self.prompt_builder
        )

        print("\n✓ GapQuest Ready.\n")

    # ==========================================================
    # Public API
    # ==========================================================

    def ingest_pdf(
        self,
        pdf_path: str
    ):
        """
        Ingest a single research paper.
        """

        self.ingestion_engine.ingest_pdf(pdf_path)

    def ingest_folder(
        self,
        folder_path: str
    ):
        """
        Ingest every PDF inside a folder.
        """

        self.folder_ingestion_engine.ingest_folder(folder_path)

    def ask(
        self,
        question: str
    ):
        """
        Ask GapQuest a research question.
        """

        return self.reasoner.analyze(
            question=question
        )