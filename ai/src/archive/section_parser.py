import re


def parse_sections(text):
    """
    Splits a markdown paper into logical sections.
    """

    sections = {}

    # -----------------------------------
    # Find markdown headings
    # -----------------------------------

    heading_pattern = re.compile(
        r"^(#{1,6}\s*.+)$",
        re.MULTILINE
    )

    matches = list(heading_pattern.finditer(text))

    # -----------------------------------
    # No headings?
    # -----------------------------------

    if not matches:

        sections["full_text"] = text

        return sections

    # -----------------------------------
    # Extract section contents
    # -----------------------------------

    for i, match in enumerate(matches):

        heading = match.group().strip()

        start = match.end()

        if i + 1 < len(matches):

            end = matches[i + 1].start()

        else:

            end = len(text)

        content = text[start:end].strip()

        heading_clean = heading.replace("#", "").strip()

        sections[heading_clean] = content

    return sections


if __name__ == "__main__":

    from preprocessing.extract_pdf import extract_text
    from preprocessing.clean_text import clean_text

    text = extract_text("papers/Forest_fire.pdf")

    text = clean_text(text)

    sections = parse_sections(text)

    print()

    print("=" * 80)

    print("Sections Found")

    print("=" * 80)

    for name in sections:

        print(name)