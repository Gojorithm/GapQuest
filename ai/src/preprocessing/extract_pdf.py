import pymupdf4llm


def extract_markdown(pdf_path):
    """
    Extract a PDF as Markdown using PyMuPDF4LLM.
    """

    markdown = pymupdf4llm.to_markdown(pdf_path)

    return markdown


if __name__ == "__main__":

    md = extract_markdown("papers/Forest_fire.pdf")

    print("=" * 80)
    print(md[:5000])
    print("=" * 80)

# import pymupdf4llm


# def extract_text(pdf_path):
#     """
#     Extract a research paper into clean Markdown while preserving
#     headings, reading order, and paragraph structure.
#     """

#     markdown = pymupdf4llm.to_markdown(pdf_path)

#     return markdown

# #CODE FOR TESTING: 
# if __name__ == "__main__":

#     text = extract_text("papers/Forest_fire.pdf")

#     print("=" * 80)
#     print(text[:4000])
#     print("=" * 80)



# #OLD CODE: 
# # # import fitz

# # # pdf_path = "papers/Forest_fire.pdf"

# # # doc = fitz.open(pdf_path)

# # # print(f"Number of pages: {len(doc)}")

# # # for page_num, page in enumerate(doc):
# # #     print(f"\n===== PAGE {page_num + 1} =====\n")
# # #     print(page.get_text())

# # import fitz


# # def extract_text(pdf_path):
# #     """
# #     Extracts all text from a PDF.
# #     """

# #     doc = fitz.open(pdf_path)

# #     full_text = ""

# #     for page in doc:
# #         full_text += page.get_text()

# #     return full_text


# # if __name__ == "__main__":

# #     text = extract_text("papers/Forest_fire.pdf")

# #     print(text[:1000])