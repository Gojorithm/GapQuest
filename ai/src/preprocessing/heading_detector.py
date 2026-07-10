import re


# -----------------------------
# Common section names
# -----------------------------
COMMON_HEADINGS = {
    "abstract",
    "introduction",
    "background",
    "related work",
    "literature review",
    "method",
    "methodology",
    "materials",
    "materials and methods",
    "experiment",
    "experiments",
    "experimental setup",
    "results",
    "discussion",
    "conclusion",
    "future work",
    "acknowledgements",
    "acknowledgments",
    "references",
    "appendix"
}


def clean_heading(text):
    """Remove markdown formatting."""

    return (
        text.replace("*", "")
            .replace("#", "")
            .replace("_", "")
            .strip()
    )


def detect_heading(line):
    """
    Returns:

    {
        "is_heading": bool,
        "level": int,
        "title": str,
        "score": int
    }
    """

    original = line

    line = clean_heading(line)

    score = 0
    level = None

    # ---------------------------------------
    # Markdown heading
    # ---------------------------------------

    if original.startswith("# "):
        score += 40
        level = 0

    elif original.startswith("## "):
        score += 35
        level = 1

    elif original.startswith("### "):
        score += 30
        level = 2

    elif original.startswith("#### "):
        score += 25
        level = 3

    # ---------------------------------------
    # Numbered headings
    # ---------------------------------------

    if re.match(r'^\d+\.\s', line):
        score += 40
        level = 1

    elif re.match(r'^\d+\.\d+\.\s', line):
        score += 35
        level = 2

    elif re.match(r'^\d+\.\d+\.\d+\.\s', line):
        score += 30
        level = 3

    elif re.match(r'^\d+\.\d+\.\d+\.\d+\.\s', line):
        score += 25
        level = 4

    # ---------------------------------------
    # Common heading words
    # ---------------------------------------

    if line.lower() in COMMON_HEADINGS:
        score += 30

    # ---------------------------------------
    # Short line
    # ---------------------------------------

    words = len(line.split())

    if words <= 10:
        score += 10

    # ---------------------------------------
    # Mostly Title Case
    # ---------------------------------------

    if line.istitle():
        score += 10

    # ---------------------------------------
    # Mostly ALL CAPS
    # ---------------------------------------

    if line.isupper() and words <= 8:
        score += 10

    # ---------------------------------------

    return {
        "is_heading": score >= 40,
        "level": level,
        "title": line,
        "score": score
    }


# --------------------------------------------------------

if __name__ == "__main__":

    tests = [

        "# Research Paper",

        "## 2. Method",

        "### 2.1 Dataset",

        "#### 2.1.1 Image Collection",

        "Introduction",

        "RESULTS",

        "Forest fires are increasing rapidly."

    ]

    for t in tests:

        print(t)

        print(detect_heading(t))

        print()