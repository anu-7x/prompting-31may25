
from openai import OpenAI
from const import OPENAI_API_KEY, GPT4_1_NANO_MODEL

class GPT4_1NanoSrv:
  def __init__(self):
    self.api_key: str = OPENAI_API_KEY
    self.model: str = GPT4_1_NANO_MODEL
    self.client = OpenAI(
      api_key=self.api_key,
    )
    #
    print(f" ---- >> Client Intialized with model: {self.model}")

  def get_response(self, prompt: str) -> dict | None:
    """Query the GPT-4.1 Nano model with a prompt."""
    try:
      response = self.client.responses.create(
        model=self.model,
        input=prompt,
        # todo: add more parameters like temperature, max_tokens, etc...
      )
      return response
    except Exception as e:
      print(f"Error querying GPT-4.1 Nano: {e}")
      return None
