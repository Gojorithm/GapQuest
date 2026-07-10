from ai.llm_provider import LLMProvider

provider = LLMProvider()

prompt = """
Return ONLY this JSON.

{
    "hello":"world"
}

Do not add markdown.
"""

print(provider.generate(prompt))