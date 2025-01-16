from intents import get_intent
from nlp_utils import generate_response

user_question = "Care sunt regulile jocului?"
intent = get_intent(user_question)
print(intent)
response = generate_response(intent, user_question)
print(f"AI Helper: {response}\n")
