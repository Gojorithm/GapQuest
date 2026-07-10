import re


def markdown_chunk(markdown_text):
    """
    Splits markdown into semantic chunks while preserving
    the hierarchy of the research paper.
    """

    chunks = []

    paper_title = ""
    main_section = ""
    subsection = ""
    subsubsection = ""

    current_text = []

    lines = markdown_text.split("\n")

    def save_chunk():
        nonlocal current_text

        if not current_text:
            return

        chunks.append({

            "chunk_id":
                f"{paper_title[:20].replace(' ','_')}_{len(chunks)+1:04}",

            "paper_title":
                paper_title.strip(),

            "main_section":
                main_section.replace("*", "").replace("_", "").strip(),

            "subsection":
                subsection.replace("*", "").replace("_", "").strip(),

            "subsubsection":
                subsubsection.replace("*", "").replace("_", "").strip(),

            "chunk_number":
                len(chunks) + 1,

            "word_count":
                len(" ".join(current_text).split()),

            "text":
                "\n".join(current_text).strip()

        })

        current_text = []

    for line in lines:

        line = line.strip()

        if not line:
            continue

        # -------------------------
        # Paper Title
        # -------------------------
        if line.startswith("# ") and not line.startswith("##"):

            save_chunk()

            paper_title = line.replace("#", "").strip()

            continue

        # Remove markdown symbols for regex matching
        clean = (
            line.replace("*", "")
                .replace("_", "")
                .replace("#", "")
                .strip()
        )

        # ====================================================
        # MAIN SECTION
        # ====================================================
        if (
            line.startswith("## ")
            or re.match(r"^\d+\.\s", clean)
        ):

            save_chunk()

            main_section = clean
            subsection = ""
            subsubsection = ""

            continue

        # ====================================================
        # SUBSECTION
        # ====================================================
        if (
            line.startswith("### ")
            or re.match(r"^\d+\.\d+\.\s", clean)
        ):

            save_chunk()

            subsection = clean
            subsubsection = ""

            continue

        # ====================================================
        # SUB-SUBSECTION
        # ====================================================
        if (
            line.startswith("#### ")
            or re.match(r"^\d+\.\d+\.\d+\.\s", clean)
        ):

            save_chunk()

            subsubsection = clean

            continue

        current_text.append(line)

    save_chunk()

    return chunks


if __name__ == "__main__":

    from preprocessing.extract_pdf import extract_markdown
    from preprocessing.clean_text import clean_markdown

    markdown = extract_markdown("papers/Forest_fire.pdf")

    markdown = clean_markdown(markdown)

    chunks = markdown_chunk(markdown)

    print(f"\nChunks Found: {len(chunks)}")

    for chunk in chunks:

        print("\n" + "=" * 70)

        print("Chunk ID      :", chunk["chunk_id"])
        print("Paper         :", chunk["paper_title"])
        print("Main Section  :", chunk["main_section"])
        print("Subsection    :", chunk["subsection"])
        print("SubSubsection :", chunk["subsubsection"])
        print("Chunk Number  :", chunk["chunk_number"])
        print("Word Count    :", chunk["word_count"])

        print("\nTEXT:\n")

        print(chunk["text"][:500])