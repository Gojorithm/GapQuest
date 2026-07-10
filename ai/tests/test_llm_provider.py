from ai.llm_provider import LLMProvider

print("Creating provider...")

provider = LLMProvider()

print()

print("Asking Gemini...")

response = provider.generate(
    """
    In one sentence, explain what a research gap is and also the meaning of the name neha.
    """
)

print()

print("=" * 80)

print(response)