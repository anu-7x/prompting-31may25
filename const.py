import os

OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
	raise ValueError("OPENAI_API_KEY environment variable is not set.")
#
GPT4_1_NANO_MODEL: str = os.getenv("GPT4_1_NANO_MODEL", "gpt-4.1-nano")

