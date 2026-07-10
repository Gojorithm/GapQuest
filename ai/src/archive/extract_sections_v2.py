import re

# def extract_title(full_text):
#     return ""
def extract_title(full_text):

    title = ""

    title_match = re.search(
        r"^(.*?)Abstract\.?",
        full_text,
        re.IGNORECASE
    )

    if title_match:
        title = title_match.group(1).strip()

    return title


# def extract_abstract(full_text):
#     return ""
def extract_abstract(full_text):

    # abstract = ""

    normalized_text = full_text

    normalized_text = normalized_text.replace(
        "A B S T R A C T",
        "ABSTRACT"
    )
    # ---------- Strategy 1 ----------
    # Standard papers containing:
    # Abstract ... Keywords / Introduction


    abstract_match = re.search(
        r"\bAbstract\b\s*\.?\s*(.*?)\s*(Keywords\s*[.:\-–—]?|Index\s+Terms\s*[.:\-–—]?|1\.\s*Introduction|Introduction|I\.\s*Introduction)",
        normalized_text,
        re.IGNORECASE | re.DOTALL
    )

   

    if abstract_match:
        print("\n===== REGEX DEBUG =====")
        print("Matched text starts with:")
        print(abstract_match.group(0)[:300])

        print("\nMatched text ends with:")
        print(abstract_match.group(0)[-300:])

        abstract = abstract_match.group(1).strip()

        return abstract
    # ---------- Strategy 2 ----------
    # (We'll implement this next.)

    return ""

# def extract_conclusion(full_text):
#     return ""
def extract_conclusion(full_text):
    headings = list(
        re.finditer(
            r"(?:^|\n)\s*(?:\d+\.?|[IVXLC]+\.)?\s*"
            r"(Conclusion(?:s)?(?:\s+and\s+Future\s+Work|\s+and\s+Future\s+Scope)?"
            r"|References?|Bibliography|Acknowledg(?:e)?ments?)",
            full_text,
            re.IGNORECASE
        )
    )

    if not headings:
        return ""

    conclusion_index = None

    for i, match in enumerate(headings):

        heading = match.group(1).lower()

        if "conclusion" in heading:
            conclusion_index = i

    if conclusion_index is None:
        return ""

    start = headings[conclusion_index].end()

    if conclusion_index + 1 < len(headings):
        end = headings[conclusion_index + 1].start()
    else:
        end = len(full_text)

    conclusion = full_text[start:end].strip()

    return conclusion
    # conclusion = ""

    # conclusion_match = re.search(
    #     # r"Conclusion(.*?)(References?|Reference)",
    #     r"\n\d*\.?\s*Conclusion\s*\n(.*?)(References?|Reference)",
    #     full_text,
    #     re.IGNORECASE | re.DOTALL
    # )

    # if conclusion_match:
    #     print("\n===== CONCLUSION DEBUG =====")
    #     # print(conclusion_match.group(0)[:400])
    #     # print(conclusion_match.start())
    #     # print(conclusion_match.end())
    #     print("\nConclusion length:")
    #     print(len(conclusion_match.group(1)))
    #     print("\nFirst 500 characters:\n")
    #     print(conclusion_match.group(1)[:500])

    #     print("\nLast 500 characters:\n")
    #     print(conclusion_match.group(1)[-500:])
    #     # print(full_text[conclusion_match.start()-100:
    #     #         conclusion_match.start()+250])
    #     print("\n----- ENDS WITH -----\n")
    #     print(conclusion_match.group(0)[-400:])

    # if conclusion_match:
    #     conclusion = conclusion_match.group(1).strip()

    # return conclusion
    # print("\n===== LOOKING FOR CONCLUSION =====")

    # index = full_text.lower().find("conclusion")

    # print("Index:", index)

    # if index != -1:
    #     print(full_text[index-300:index+800])
    # print("\n===== ALL CONCLUSION OCCURRENCES =====")

    # for m in re.finditer(r"conclusion", full_text, re.IGNORECASE):
    #     print("\n---------------------------")
    #     print("Index:", m.start())
    #     print(full_text[m.start()-120:m.start()+300])

    # # conclusion_match = re.search(
    #     r"\n\d*\.?\s*Conclusion\s*\n(.*?)(References?|Reference)",
    #     full_text,
    #     re.IGNORECASE | re.DOTALL
    # )
    # conclusion_match = re.search(
    # r"\b\d*\.?\s*Conclusion(?:s)?(?:\s+and\s+Future\s+Work)?\b[:.]?\s*(.*?)(?:References?|Acknowledg(?:e)?ments?|Bibliography|$)",
    # full_text,
    # re.IGNORECASE | re.DOTALL
    # )   
    # if conclusion_match:
    #     print("\nFOUND CONCLUSION!")
    # else:
    #     print("\nNO CONCLUSION FOUND")

    # if conclusion_match:
    #     conclusion = conclusion_match.group(1).strip()

    # return conclusion    

    # return ""

def extract_sections(full_text):
    """
    Extract title, abstract and conclusion from paper text.
    """

    # title = ""
    # abstract = ""
    # conclusion = ""

    title = extract_title(full_text)
    abstract = extract_abstract(full_text)
    conclusion = extract_conclusion(full_text)


#     # ---------- TITLE ----------
#     title_match = re.search(
#         # r"^(.*?)Abstract",
#         r"^(.*?)Abstract\.?",
#         full_text,
#         re.IGNORECASE
#     )

#     if title_match:
#         title = title_match.group(1).strip()

#     # ---------- ABSTRACT ----------
#     # abstract_match = re.search(
#     #     r"Abstract\.?(.*?)(Keywords\.|1\.\s*Introduction)",
#     #     full_text,
#     #     re.IGNORECASE
#     # )
#     # abstract_match = re.search(
#     # r"Abstract\s*\.?\s*(.*?)\s*(Keywords\s*[.:\-–—]?|Index\s+Terms\s*[.:\-–—]?|1\.\s*Introduction|Introduction|I\.\s*Introduction)",
#     # full_text,
#     # re.IGNORECASE | re.DOTALL
#     # )

#     # if abstract_match:
#     #     abstract = abstract_match.group(1).strip()
#     abstract_match = re.search(
#     r"Abstract\s*\.?\s*(.*?)\s*(Keywords\s*[.:\-–—]?|Index\s+Terms\s*[.:\-–—]?|1\.\s*Introduction|Introduction|I\.\s*Introduction)",
#     full_text,
#     re.IGNORECASE | re.DOTALL
# )

#     if abstract_match:
#         print("\n===== REGEX DEBUG =====")
#         print("Matched text starts with:")
#         print(abstract_match.group(0)[:300])

#         print("\nMatched text ends with:")
#         print(abstract_match.group(0)[-300:])

#         abstract = abstract_match.group(1).strip()

#     # ---------- CONCLUSION ----------
#     conclusion_match = re.search(
#         r"Conclusion(.*?)(References?|Reference)",
#         full_text,
#         re.IGNORECASE
#     )

#     if conclusion_match:
#         conclusion = conclusion_match.group(1).strip()

    return {
        "title": title,
        "abstract": abstract,
        "conclusion": conclusion,
    }


if __name__ == "__main__":

    # from extract_pdf import extract_text

    # text = extract_text("papers/Forest_fire.pdf")

    from preprocessing.extract_pdf import extract_text
    from preprocessing.clean_text import clean_text

    text = extract_text("papers/Forest_fire.pdf")

    text = clean_text(text)

    # print(text[:1000])

    paper = extract_sections(text)

    print("\nTITLE:\n")
    print(paper["title"])

    print("\nABSTRACT:\n")
    print(paper["abstract"][:300])

    print("\nCONCLUSION:\n")
    print(paper["conclusion"][:300])


# import fitz
# import json
# import re

# pdf_path = "papers/Forest_fire.pdf"

# # --------------------------
# # READ PDF
# # --------------------------

# doc = fitz.open(pdf_path)

# full_text = ""

# for page in doc:
#     full_text += page.get_text() + "\n"

# # Normalize spaces
# full_text = re.sub(r'\s+', ' ', full_text)

# # --------------------------
# # TITLE EXTRACTION
# # --------------------------

# title = ""

# abstract_match = re.search(
#     r"^(.*?)Abstract",
#     full_text,
#     re.IGNORECASE
# )

# if abstract_match:
#     title_block = abstract_match.group(1)

#     lines = title_block.split(" ")

#     title = title_block.strip()

# # --------------------------
# # ABSTRACT EXTRACTION
# # --------------------------

# abstract = ""

# abstract_match = re.search(
#     r"Abstract\.?(.*?)(Keywords\.|1\.\s*Introduction)",
#     full_text,
#     re.IGNORECASE
# )

# if abstract_match:
#     abstract = abstract_match.group(1).strip()

# # --------------------------
# # CONCLUSION EXTRACTION
# # --------------------------

# conclusion = ""

# conclusion_match = re.search(
#     r"Conclusion(.*?)(References?|Reference)",
#     full_text,
#     re.IGNORECASE
# )

# if conclusion_match:
#     conclusion = conclusion_match.group(1).strip()

# # --------------------------
# # SAVE JSON
# # --------------------------

# paper_data = {
#     "title": title,
#     "abstract": abstract,
#     "conclusion": conclusion
# }

# with open(
#     "outputs/paper_data_v2.json",
#     "w",
#     encoding="utf-8"
# ) as f:
#     json.dump(
#         paper_data,
#         f,
#         indent=4,
#         ensure_ascii=False
#     )

# print("Improved JSON generated!")