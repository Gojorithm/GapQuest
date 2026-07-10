from ai.retriever import Retriever
from ai.llm_provider import LLMProvider
from ai.prompt_builder import PromptBuilder

from ai.paper_analyzer import PaperAnalyzer
from ai.literature_evidence_builder import LiteratureEvidenceBuilder

from models.research_report import ResearchReport
from models.report_item import ReportItem
from models.evidence import Evidence


class LLMReasoner:
    """
    Coordinates the complete GapQuest reasoning pipeline.

    Workflow:

        User Question
              ↓
        Retriever
              ↓
        Paper Analyzer
              ↓
        Literature Evidence Builder
              ↓
        Prompt Builder
              ↓
        Gemini
              ↓
        Research Report
    """

    def __init__(
        self,
        retriever: Retriever,
        paper_analyzer: PaperAnalyzer,
        evidence_builder: LiteratureEvidenceBuilder,
        llm_provider: LLMProvider,
        prompt_builder: PromptBuilder
    ):

        self.retriever = retriever
        self.paper_analyzer = paper_analyzer
        self.evidence_builder = evidence_builder
        self.llm_provider = llm_provider
        self.prompt_builder = prompt_builder

    def _build_report_items(self, items):

        report_items = []

        for item in items:

            evidence_list = []

            for evidence in item.get("evidence", []):

                evidence_list.append(

                    Evidence(
                        paper_title=evidence.get(
                            "paper_title",
                            ""
                        ),

                        section=evidence.get(
                            "section",
                            ""
                        )
                    )

                )

            report_items.append(

                ReportItem(

                    text=item.get(
                        "text",
                        ""
                    ),

                    evidence=evidence_list

                )

            )

        return report_items

    def analyze(
        self,
        question: str,
        top_k: int = 30
    ) -> ResearchReport:

        # --------------------------------------------------
        # Step 1: Retrieve relevant chunks
        # --------------------------------------------------

        retrieved_chunks = self.retriever.retrieve(
            query=question,
            top_k=top_k
        )

        # --------------------------------------------------
        # Step 2: Group chunks by paper
        # --------------------------------------------------

        papers = self.paper_analyzer.group_by_paper(
            retrieved_chunks
        )

        # --------------------------------------------------
        # Step 3: Select the best sections from each paper
        # --------------------------------------------------

        papers = self.evidence_builder.build(
            papers
        )

        # --------------------------------------------------
        # Debug: Show selected evidence
        # --------------------------------------------------

        print("\nSelected Evidence\n")
        print("=" * 70)

        for paper in papers:

            print(f"\n📄 {paper.paper_title}")
            print("-" * 70)

            for chunk in paper.chunks:

                section = (
                    chunk.chunk.hierarchy.main_section
                    if chunk.chunk.hierarchy.main_section
                    else "Abstract"
                )

                print(section)
                print(f"Similarity : {round(chunk.similarity, 3)}")
                print()

        # --------------------------------------------------
        # Step 4: Build prompt
        # --------------------------------------------------

        prompt = self.prompt_builder.build_prompt(
            papers
        )

        # --------------------------------------------------
        # Step 5: Ask Gemini
        # --------------------------------------------------

        data = self.llm_provider.generate(
            prompt
        )

        # --------------------------------------------------
        # Step 6: Convert JSON into ResearchReport
        # --------------------------------------------------

        report = ResearchReport(

            domain=data.get(
                "domain",
                ""
            ),

            focus_area=data.get(
                "focus_area",
                ""
            ),

            papers_analyzed=len(papers),

            summary=data.get(
                "summary",
                ""
            ),

            key_findings=self._build_report_items(
                data.get(
                    "key_findings",
                    []
                )
            ),

            common_themes=self._build_report_items(
                data.get(
                    "common_themes",
                    []
                )
            ),

            contradictions=self._build_report_items(
                data.get(
                    "contradictions",
                    []
                )
            ),

            research_gaps=self._build_report_items(
                data.get(
                    "research_gaps",
                    []
                )
            ),

            future_recommendations=self._build_report_items(
                data.get(
                    "future_recommendations",
                    []
                )
            ),

            confidence_score=data.get(
                "confidence_score",
                0
            )

        )

        return report