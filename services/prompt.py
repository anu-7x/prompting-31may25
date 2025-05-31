
from services import GPT4_1NanoSrv

class PromptService:
  def __init__(self, model: str = "gpt-4.1-nano"):
    if model == "gpt-4.1-nano":
      self.srv = GPT4_1NanoSrv()
    else:
      raise ValueError(f"Unsupported model: {model}")
    #
    print(f" ---- >> PromptService initialized with model: {model}")
  
  def __combine_prompts(
      self, 
      system_prompt: str, 
      user_prompt: str,
      example_prompt: str | None = None,
    ) -> str:
    """
    Combine system, user, and example prompts into a single prompt string.
    """
    combined = f"{system_prompt}\n\n"
    if example_prompt:
      examples = f"Examples:\n{example_prompt}"
      combined += examples + "\n\n"
    combined += f"Now solve this problem:\n{user_prompt}"
    #
    print(f" ---- >> Combined Prompt:\n{combined}")
    return combined.strip()
  
  def test_chain_of_thought(
      self,
      user_problem: str,
      custom_examples=None
  ):
      """
      Test chain of thought reasoning with flexible user input
      """
      # System prompt - defines the technique
      system_prompt = """You are an expert problem solver. Always use step-by-step reasoning to solve problems. 
      For each problem:
      1. Break it down into clear steps
      2. Show your work for each step
      3. Clearly state your final answer

      Use this format:
      Step 1: [describe what you're doing]
      Step 2: [next step]
      Step 3: [continue until solved]
      Final Answer: [your conclusion]"""

      # Default example if none provided
      default_examples = """Problem: If a train travels 60 miles in 1 hour, how long will it take to travel 180 miles?

      Step 1: Find the speed = 60 miles/hour
      Step 2: Use formula: Time = Distance ÷ Speed  
      Step 3: Time = 180 ÷ 60 = 3 hours
      Final Answer: 3 hours"""

      # Default problem if none provided
      default_problem = "Problem: A store sells 25 items per day. How many items will they sell in 2 weeks?"

      # use provided examples or default
      examples = custom_examples if custom_examples else default_examples
      user_prompt = user_problem if user_problem else default_problem
      #
      # combine prompts
      combined_prompt = self.__combine_prompts(
          system_prompt=system_prompt,
          user_prompt=user_prompt,
          example_prompt=examples
      )
      #
      print(" ---- >> Querying GPT-4.1 Nano for Chain of Thought reasoning...")
      response = self.srv.get_response(combined_prompt)
      if response:
          try:
              response = response.json()
          except Exception as e:
              print(f" ---- >> Error converting response to JSON: {e}")
      else:
          print(" ---- >> No response received.")
      #
      return response
