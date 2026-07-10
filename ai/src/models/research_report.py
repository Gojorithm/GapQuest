from dataclasses import dataclass, field

from models.report_item import ReportItem


@dataclass
class ResearchReport:
    """
    Final intelligence report produced by GapQuest.
    """

    # Report metadata
    domain: str = ""

    focus_area: str = ""

    papers_analyzed: int = 0

    # Report contents
    summary: str = ""

    key_findings: list[ReportItem] = field(default_factory=list)

    common_themes: list[ReportItem] = field(default_factory=list)

    contradictions: list[ReportItem] = field(default_factory=list)

    research_gaps: list[ReportItem] = field(default_factory=list)

    future_recommendations: list[ReportItem] = field(default_factory=list)

    # Confidence
    confidence_score: float = 0.0