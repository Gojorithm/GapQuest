import json
import time
import os

from dotenv import load_dotenv
from google import genai


class LLMProvider:
    """
    Wrapper around Google's Gemini API.

    Responsible only for communicating with Gemini.
    """

    def __init__(self):

        load_dotenv()

        api_key = os.getenv("GEMINI_API_KEY")

        if not api_key:
            raise ValueError(
                "GEMINI_API_KEY not found in .env"
            )

        print("Loading Gemini...")

        self.client = genai.Client(
            api_key=api_key
        )

        print("✓ Gemini ready.")

    def generate(
        self,
        prompt: str
    ) -> dict:
        """
        Sends a prompt to Gemini.

        Automatically retries if Gemini is temporarily unavailable.

        Returns:
            Parsed JSON as a Python dictionary.
        """

        max_retries = 5

        for attempt in range(1, max_retries + 1):

            try:

                response = self.client.models.generate_content(
                    model="gemini-2.5-flash",
                    contents=prompt
                )

                text = response.text.strip()

                # Remove markdown if Gemini adds it

                if text.startswith("```json"):
                    text = text.replace("```json", "", 1)

                if text.startswith("```"):
                    text = text.replace("```", "", 1)

                if text.endswith("```"):
                    text = text[:-3]

                return json.loads(text.strip())

            except Exception as error:

                print(
                    f"Gemini attempt {attempt}/{max_retries} failed."
                )

                if attempt == max_retries:
                    raise RuntimeError(
                        "Gemini is unavailable after multiple retries."
                    ) from error

                print("Retrying in 2 seconds...")

                time.sleep(5)