from ai.embedding_engine import EmbeddingEngine
from ai.llm_provider import LLMProvider
from ai.prompt_builder import PromptBuilder
from ai.retriever import Retriever
from ai.llm_reasoner import LLMReasoner

from database.vector_store import VectorStore


print("Loading embedding engine...")
embedding_engine = EmbeddingEngine()

print("\nConnecting to vector database...")
vector_store = VectorStore()

print("\nLoading Gemini...")
llm_provider = LLMProvider()

print("\nCreating Prompt Builder...")
prompt_builder = PromptBuilder()

print("\nCreating Retriever...")
retriever = Retriever(
    embedding_engine=embedding_engine,
    vector_store=vector_store
)

print("\nCreating Reasoner...")
reasoner = LLMReasoner(
    retriever=retriever,
    llm_provider=llm_provider,
    prompt_builder=prompt_builder
)

print("\nRunning complete reasoning pipeline...")

report = reasoner.analyze(
    question="What are the research gaps in forest fire detection?"
)

print("\n" + "=" * 80)

print("SUMMARY")
print(report.summary)

print("\nKEY FINDINGS")
for finding in report.key_findings:
    print("-", finding)

print("\nCOMMON THEMES")
for theme in report.common_themes:
    print("-", theme)

print("\nCONTRADICTIONS")
for contradiction in report.contradictions:
    print("-", contradiction)

print("\nRESEARCH GAPS")
for gap in report.research_gaps:
    print("-", gap)

print("\nFUTURE RECOMMENDATIONS")
for recommendation in report.future_recommendations:
    print("-", recommendation)

print("\nCONFIDENCE SCORE")
print(report.confidence_score)