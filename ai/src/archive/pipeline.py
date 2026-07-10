from utils.file_handler import get_pdf_files
from preprocessing.extract_pdf import extract_text
from preprocessing.clean_text import clean_text
#from extract_sections_v2 import extract_sections
from archive.section_parser import extract_sections
from semantic_chunker import chunk_text
from archive.embeddings import store_embedding


pdf_files = get_pdf_files()

print(f"Found {len(pdf_files)} PDF(s).\n")

for pdf in pdf_files:
    # if pdf.name != "Forest_fire.pdf":
    #     continue

    print(f"Processing: {pdf.name}")

    text = extract_text(pdf)

    text = clean_text(text)

    paper = extract_sections(text)
    print("\nTITLE EXTRACTED:")
    print(paper["title"])
    print("-" * 80)
    print("\nPIPELINE CHECK")
    print("Conclusion length:", len(paper["conclusion"]))
    print(paper["conclusion"][:300])
#     sections = [
#     ("abstract", paper["abstract"]),
#     ("conclusion", paper["conclusion"])
# ]

    sections = [
    ("abstract", paper["abstract"]),
    ("conclusion", paper["conclusion"])
    ]

    # for section_name, section_text in sections:
    #     print(f"{section_name}: {len(section_text)} characters")
    for section_name, section_text in sections:

        chunks = chunk_text(section_text)

        print(f"{section_name}: {len(chunks)} chunks")
        
        # for chunk in chunks:
        for chunk_number, chunk in enumerate(chunks, start=1):
            chunk_id = (
            f"{pdf.stem}_{section_name}_{chunk_number}"
            )
            metadata = {
            "paper": pdf.stem,
            #"title": paper["title"],
            "title": paper["title"] if paper["title"] else pdf.stem,
            #"title": pdf.stem,
            "section": section_name,
            "chunk_number": chunk_number,
            "total_chunks": len(chunks)
            }

            store_embedding(
            chunk,
            chunk_id,
            metadata
            )
            print(chunk_id)
            # print(chunk[:80])
            # print("-" * 40)

    print(f"Extracted {len(text)} cleaned characters.\n")
    print(f"✅ Title Found: {'Yes' if paper['title'] else 'No'}")
    #print(f"Paper: {pdf.stem}")
    print(f"Paper: {paper['title'] if paper['title'] else pdf.stem}")
    print(f"✅ Title Found: {'Yes' if paper['title'] else 'No'}")
    print(f"✅ Abstract Found: {'Yes' if paper['abstract'] else 'No'}")
    print(f"✅ Conclusion Found: {'Yes' if paper['conclusion'] else 'No'}")

    # if pdf.name == "1-s2.0-S2542660524001124-main.pdf":
    if pdf.name == "1-s2.0-S2542660524001124-main.pdf":

        print("\n========== FIRST 5000 CHARACTERS ==========\n")
        print(text[:5000])
        print("\n===========================================\n")



        # start = text.find("Abstract")

        # print("\n========== ABSTRACT REGION ==========\n")
        # print(text[start:start+4000])
        # print("\n=====================================\n")
    # if pdf.name == "Residual Capsule Network for Forest Fire Detection Using UAV Imagery.pdf":
    #     print("\n========== FIRST 3000 CHARACTERS ==========\n")
    #     print(text[:3000])
    #     print("\n===========================================\n")
    # if pdf.name == "Artificial Intelligence for Wildfire Detection and Management.pdf":
    #     position = text.find("Abstract")

    #     print(text[position:position + 1200])
        # print("\nDoes 'Abstract' exist?")
        # print("Abstract" in text)

        # print("\nPosition of Abstract:")
        # print(text.find("Abstract"))
        # print(text[:1000])
    print()