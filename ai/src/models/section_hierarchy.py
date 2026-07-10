from dataclasses import dataclass


@dataclass
class SectionHierarchy:
    """
    Represents where a chunk belongs inside a paper.
    """

    main_section: str = ""

    subsection: str = ""

    subsubsection: str = ""