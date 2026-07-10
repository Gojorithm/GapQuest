from gapquest.gapquest import GapQuest


print("Starting GapQuest...\n")

gapquest = GapQuest()

print("Clearing database...\n")

gapquest.vector_store.clear()

print("Ingesting folder...\n")

gapquest.ingest_folder("papers")

print("=" * 80)

print("Database contains")

print(gapquest.vector_store.count())

print("chunks.")