# Implement an application with the following functionalities:

# - (0.25 points) Read a text from the command line or from a file.

# - (0.25 points) Identify the language in which the text is written.

# - (0.5 points) Display stylometric information (word and character length, word frequency, etc.) for that text (for example, using this guide: https://programminghistorian.org/en/lessons/introduction-to-stylometry-with-python).

# - (1 point) Generate alternative versions of the text in which at least 20% of the words are replaced with synonyms (e.g., "house" - "home") and/or hypernyms (e.g., "house" - "building") and/or negated antonyms (e.g., "far" - "not near"). Use WordNet (https://wordnet.princeton.edu/ or https://www.racai.ro/p/llod/index_en.html for the lexical resource, and https://www.nltk.org/howto/wordnet.html for the API, for example).

# - (1 point) Extract keywords from a paragraph (for example, using these methods: https://towardsdatascience.com/keyword-extraction-process-in-python-with-natural-language-processing-nlp-d769a9069d5c). Generate one sentence for each keyword found, preserving its meaning from the original text.

# - Bonus (0.25 points): The initial text is in Romanian.

import os


def load_text(source):
    if os.path.isfile(source):
        # read from file
        with open(source, 'r') as file:
            return file.read()
    else:
        # read from command line
        return source


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


source = input("Enter the text or file path: ")
text = load_text(source)
detected_language = detect_language(text)
print(f"Detected language: {detected_language}")
