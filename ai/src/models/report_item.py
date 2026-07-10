from dataclasses import dataclass, field

from models.evidence import Evidence


@dataclass
class ReportItem:
    """
    One AI-generated finding together with the evidence
    supporting it.
    """

    text: str

    evidence: list[Evidence] = field(default_factory=list)