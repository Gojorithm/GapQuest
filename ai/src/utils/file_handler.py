from pathlib import Path


def get_pdf_files(folder="papers"):
    """
    Returns a list of all PDF files inside the given folder.
    """

    folder_path = Path(folder)

    pdf_files = list(folder_path.glob("*.pdf"))

    return pdf_files


if __name__ == "__main__":

    files = get_pdf_files()

    print("PDF files found:\n")

    for file in files:
        print(file.name)