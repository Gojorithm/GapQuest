from preprocessing.extract_pdf import extract_markdown
from preprocessing.clean_text import clean_markdown
from preprocessing.markdown_parser import parse_markdown
from preprocessing.semantic_chunker import semantic_chunk
from ai.embedding_engine import EmbeddingEngine


PDF_PATH = "papers/Forest_fire.pdf"


def main():

    print("\nExtracting PDF...")

    markdown = extract_markdown(PDF_PATH)

    print("Cleaning text...")

    markdown = clean_markdown(markdown)

    print("Parsing headings...")

    tree = parse_markdown(markdown)

    print("Creating semantic chunks...")

    chunks = semantic_chunk(tree)

    print(f"Chunks created: {len(chunks)}")

    print("Generating embeddings...")

    engine = EmbeddingEngine()

    chunks = engine.embed_chunks(chunks)

    print("\nDone!")

    print()

    print("Example Chunk:")

    print("-------------------------")

    print(chunks[0].text[:300])

    print()

    print("Embedding Dimension:")

    print(len(chunks[0].embedding))


if __name__ == "__main__":
    main()