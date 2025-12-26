import os
from openai import OpenAI

class BaseAgent:
    """A simple agent wrapper around the OpenAI API."""
    def __init__(self, name, system_message):
        self.name = name
        self.system_message = system_message
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    def run(self, user_message):
        """Send a message to the model and return the response text."""
        response = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": self.system_message},
                {"role": "user", "content": user_message},
            ],
            temperature=0.2
        )
        # FIXED: OpenAI SDK v2.x uses object attributes, not dict indexing
        return response.choices[0].message.content


class Agents:
    """Creates the agents used in the stock analysis workflow."""

    def initialize_agents(self):
        analyst = BaseAgent(
            name="analyst",
            system_message=(
                "You are a financial analyst. Provide deep, structured insights "
                "about stocks, trends, risks, and opportunities."
            )
        )

        researcher = BaseAgent(
            name="researcher",
            system_message=(
                "You gather factual financial data, news, and metrics. "
                "Return clean, structured information only."
            )
        )

        summarizer = BaseAgent(
            name="summarizer",
            system_message=(
                "You summarize findings into a clear, concise, investor‑friendly report."
            )
        )

        return analyst, researcher, summarizer