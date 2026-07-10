from pathlib import Path

from ingestion.ingestion_engine import IngestionEngine


class FolderIngestionEngine:
    """
    Responsible for ingesting an entire folder
    of research papers.

    It delegates the actual PDF ingestion to
    IngestionEngine.
    """

    def __init__(
        self,
        ingestion_engine: IngestionEngine
    ):

        self.ingestion_engine = ingestion_engine


    def ingest_folder(
        self,
        folder_path: str
    ):
        folder = Path(folder_path)

        if not folder.exists():
            raise FileNotFoundError(
                f"Folder not found: {folder_path}"
            )   
        print(f"\nScanning folder: {folder}\n")

        pdf_files = sorted(
            folder.glob("*.pdf")
        )   

        if not pdf_files:
            print("No PDF files found.")
            return   
        print(f"Found {len(pdf_files)} PDF(s).\n") 

        for pdf_file in pdf_files:

            print(f"Ingesting: {pdf_file.name}")

            self.ingestion_engine.ingest_pdf(
                str(pdf_file)
            )

            print()