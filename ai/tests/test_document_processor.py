from preprocessing.document_processor import DocumentProcessor


print("Creating Document Processor...\n")

processor = DocumentProcessor()

print("Processing PDF...\n")

chunks = processor.process_pdf(
    "papers/Forest_fire.pdf"
)

print("=" * 80)

print(f"Total Knowledge Chunks: {len(chunks)}")

for i, chunk in enumerate(chunks[:5], start=1):

    print("\n" + "=" * 80)

    print(f"Chunk #{i}")

    print("-" * 80)

    print("Paper:")
    print(chunk.metadata.title)

    print()

    print("Main Section:")
    print(chunk.hierarchy.main_section)

    print()

    print("Subsection:")
    print(chunk.hierarchy.subsection)

    print()

    print("Words:")
    print(chunk.word_count)

    print()

    print("Text Preview:\n")

    print(chunk.text[:400])

print("\n" + "=" * 80)