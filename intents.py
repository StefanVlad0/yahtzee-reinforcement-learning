from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('paraphrase-multilingual-MiniLM-L12-v2')

faq = {
    "rules_request": "Care sunt regulile jocului?",
    "best_move_request": "Ce mutare ar trebui să fac acum?",
}

faq_embeddings = model.encode(list(faq.values()), convert_to_tensor=True)


def get_intent(question):
    question_embedding = model.encode(question, convert_to_tensor=True)
    scores = util.cos_sim(question_embedding, faq_embeddings)
    best_match_idx = scores.argmax().item()
    max_score = scores[0][best_match_idx].item()

    if max_score < 0.5:
        return "irrelevant"
    return list(faq.keys())[best_match_idx]
