import re


REFERENCE_PATTERNS = [

    r"\n\s*references\s*\n",

    r"\n\s*bibliography\s*\n",

    r"\n\s*reference\s*\n",

    r"\n\s*works cited\s*\n",

    r"\n\s*acknowledg(?:e)?ments\s*\n",

]


def remove_references(text):

    lower = text.lower()

    cut_position = len(text)

    for pattern in REFERENCE_PATTERNS:

        match = re.search(pattern, lower)

        if match:

            cut_position = min(cut_position, match.start())

    return text[:cut_position].strip()


#TESTING CODE: 
# if __name__ == "__main__":

#     sample = """

# Introduction

# AI helps detect fires.

# Conclusion

# This model performs well.

# References

# [1] Paper A

# [2] Paper B

# """

#     cleaned = remove_references(sample)

#     print(cleaned)