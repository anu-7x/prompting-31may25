
from services import PromptService
from const import GPT4_1_NANO_MODEL

def main():
    prompt_service = PromptService(model=GPT4_1_NANO_MODEL)
    #
    user_problem = "If a train travels 20 miles in 1 hour, how long will it take to travel 180 miles?"
    res = prompt_service.test_chain_of_thought(user_problem)
    #
    if res:
        print("Response from GPT-4.1 Nano:")
        print(res)
    else:
        print("No response received from the model.")

# It initializes the PromptService and tests the chain of thought reasoning with a sample problem.
if __name__ == "__main__":
    main()
