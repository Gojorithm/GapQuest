import re


def clean_markdown(md: str) -> str:
    """
    Cleans markdown while preserving headings and paragraph structure.
    """

    # Windows -> Unix newlines
    md = md.replace("\r\n", "\n")

    # remove trailing spaces
    md = re.sub(r"[ \t]+\n", "\n", md)

    # collapse 3+ blank lines
    md = re.sub(r"\n{3,}", "\n\n", md)

    # remove page numbers
    md = re.sub(r"^\d+\s*$", "", md, flags=re.MULTILINE)

    # remove strange page headers like "185"
    md = re.sub(r"^_{0,2}.*doi:.*$", "", md, flags=re.MULTILINE)

    # Remove corresponding author lines
    md = re.sub(
    r"^\d+\s+Corresponding Author.*$",
    "",
    md,
    flags=re.MULTILINE,
    )

# Remove page headers like:
# 186 W. Sun et al. /
    md = re.sub(
    r"^\d+\s+.*?Sun.*?Automatic Forest Fire.*$",
    "",
    md,
    flags=re.MULTILINE,
    )

# Remove standalone page numbers
    md = re.sub(
    r"^\d+\s*$",
    "",
    md,
    flags=re.MULTILINE,
    )

    return md.strip()


if __name__ == "__main__":

    from preprocessing.extract_pdf import extract_markdown

    md = extract_markdown("papers/Forest_fire.pdf")

    cleaned = clean_markdown(md)

    print(cleaned[:5000])



# import re


# def clean_text(text):
#     """
#     Clean extracted markdown while preserving structure.
#     """

#     # ---------------------------------------
#     # Normalize line endings
#     # ---------------------------------------

#     text = text.replace("\r\n", "\n")
#     text = text.replace("\r", "\n")

#     # ---------------------------------------
#     # Remove page numbers
#     # ---------------------------------------

#     text = re.sub(
#         r"^\s*\d+\s*$",
#         "",
#         text,
#         flags=re.MULTILINE,
#     )

#     # ---------------------------------------
#     # Remove DOI lines
#     # ---------------------------------------

#     text = re.sub(
#         r".*doi:.*",
#         "",
#         text,
#         flags=re.IGNORECASE,
#     )

#     # ---------------------------------------
#     # Remove Corresponding Author lines
#     # ---------------------------------------

#     text = re.sub(
#         r".*Corresponding Author.*",
#         "",
#         text,
#         flags=re.IGNORECASE,
#     )

#     # ---------------------------------------
#     # Remove Creative Commons lines
#     # ---------------------------------------

#     text = re.sub(
#         r".*Creative Commons.*",
#         "",
#         text,
#         flags=re.IGNORECASE,
#     )

#     # ---------------------------------------
#     # Remove copyright lines
#     # ---------------------------------------

#     text = re.sub(
#         r".*©.*",
#         "",
#         text,
#     )

#     # ---------------------------------------
#     # Remove page headers like
#     # Machine Intelligence...
#     # Internet of Things...
#     # etc.
#     # ---------------------------------------

#     bad_patterns = [

#         r".*Machine Intelligence.*",

#         r".*Internet of Things.*",

#         r".*Elsevier.*",

#         r".*IOS Press.*",

#         r".*ScienceDirect.*",

#         r".*Available online.*",

#     ]

#     for pattern in bad_patterns:

#         text = re.sub(
#             pattern,
#             "",
#             text,
#             flags=re.IGNORECASE,
#         )

#     # ---------------------------------------
#     # Remove multiple blank lines
#     # ---------------------------------------

#     text = re.sub(
#         r"\n{3,}",
#         "\n\n",
#         text,
#     )

#     # ---------------------------------------
#     # Strip whitespace
#     # ---------------------------------------

#     text = text.strip()

#     return text


# if __name__ == "__main__":

#     from extract_pdf import extract_text

#     text = extract_text("papers/Forest_fire.pdf")

#     cleaned = clean_text(text)

#     print(cleaned[:4000])









# import re


# def clean_text(text):
#     """
#     Clean extracted PDF text while preserving paragraph structure.
#     """

#     # Normalize Windows/Mac newlines
#     text = text.replace("\r\n", "\n")
#     text = text.replace("\r", "\n")

#     # Replace tabs with spaces
#     text = text.replace("\t", " ")

#     # Remove extra spaces inside lines
#     text = re.sub(r"[ ]{2,}", " ", text)

#     # Remove trailing spaces before newline
#     text = re.sub(r" *\n", "\n", text)

#     # Collapse 3+ blank lines into 2
#     text = re.sub(r"\n{3,}", "\n\n", text)

#     return text.strip()


# if __name__ == "__main__":

#     sample = """

# Abstract

# Forest fires are dangerous.


# Deep learning improves detection.



# Introduction

# CNNs are widely used.

# """

#     print(clean_text(sample))


# #OLDER CODE:
# # import json
# # import re


# # def clean_text(text):
# #     text = re.sub(r"\s+", " ", text)
# #     text = text.strip()
# #     return text


# # # with open("outputs/paper_data_v2.json", "r", encoding="utf-8") as f:
# # #     data = json.load(f)

# # # data["title"] = clean_text(data["title"])
# # # data["abstract"] = clean_text(data["abstract"])
# # # data["conclusion"] = clean_text(data["conclusion"])

# # # with open("outputs/paper_data_cleaned.json", "w", encoding="utf-8") as f:
# # #     json.dump(data, f, indent=4)

# # # print("Cleaned JSON saved successfully!")



# # if __name__ == "__main__":

# #     sample_text = """
# #     Forest fires pose significant threats.

# #     Traditional fire monitoring methods
# #     rely on satellite imagery.


# #     """

# #     cleaned = clean_text(sample_text)

# #     print(cleaned)