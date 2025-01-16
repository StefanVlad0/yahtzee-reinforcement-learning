from intents import get_intent
from nlp_utils import generate_response


def get_answer(user_question):
    intent = get_intent(user_question)
    print(intent)
    response = generate_response(intent, user_question)
    return response
