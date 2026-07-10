from dataclasses import dataclass


@dataclass
class Evidence:
    """
    A single piece of literature supporting a conclusion.
    """

    paper_title: str
    section: str