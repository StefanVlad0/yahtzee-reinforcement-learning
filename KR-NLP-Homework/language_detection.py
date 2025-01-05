import os

languages = {}


def load_common_words(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return [line.strip() for line in file]


for file_name in os.listdir('lang-resources'):
    # the words from 'lang-resources' are from https://github.com/oprogramador/most-common-words-by-language
    if file_name.endswith(".txt"):
        language_name = file_name.split('.')[0]
        file_path = os.path.join('lang-resources', file_name)
        languages[language_name] = load_common_words(file_path)


def count_common_words(text, common_words):
    words = text.lower().split()
    return sum(1 for word in words if word in common_words)


def detect_language(text):
    text = text.lower()
    scores = {}

    for lang, common_words in languages.items():
        scores[lang] = count_common_words(text, common_words)

    if max(scores.values()) > 0:
        detected_language = max(scores, key=scores.get)
    else:
        # if no common words are found, assume it's English
        detected_language = "english"

    return detected_language
