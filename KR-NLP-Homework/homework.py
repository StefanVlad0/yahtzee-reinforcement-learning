# Implement an application with the following functionalities:

# - (0.25 points) Read a text from the command line or from a file.

# - (0.25 points) Identify the language in which the text is written.

# - (0.5 points) Display stylometric information (word and character length, word frequency, etc.) for that text (for example, using this guide: https://programminghistorian.org/en/lessons/introduction-to-stylometry-with-python).

# - (1 point) Generate alternative versions of the text in which at least 20% of the words are replaced with synonyms (e.g., "house" - "home") and/or hypernyms (e.g., "house" - "building") and/or negated antonyms (e.g., "far" - "not near"). Use WordNet (https://wordnet.princeton.edu/ or https://www.racai.ro/p/llod/index_en.html for the lexical resource, and https://www.nltk.org/howto/wordnet.html for the API, for example).

# - (1 point) Extract keywords from a paragraph (for example, using these methods: https://towardsdatascience.com/keyword-extraction-process-in-python-with-natural-language-processing-nlp-d769a9069d5c). Generate one sentence for each keyword found, preserving its meaning from the original text.

# - Bonus (0.25 points): The initial text is in Romanian.


import random
from nltk.corpus import wordnet
import nltk
from text_loader import load_text
from language_detection import detect_language
from stylometry import stylometry_analysis
from rowordnet import RoWordNet
import yake
from transformers import pipeline

kw_extractor = yake.KeywordExtractor()

nltk.download('wordnet')
nltk.download('omw-1.4')

wn = RoWordNet()


def generate_alternative_text(text, language='en'):
    if language == 'ro':
        return replace_words_with_romanian_synonyms(text)
    else:
        words = text.split()
        num_replacements = max(1, int(0.2 * len(words)))
        replaced_text = []

        for word in words:
            if num_replacements > 0 and random.random() < 0.2:
                synonym = get_synonym(word)
                if synonym:
                    replaced_text.append(synonym)
                    print(f"Replaced '{word}' with '{synonym}'")
                    num_replacements -= 1
                else:
                    replaced_text.append(word)
            else:
                replaced_text.append(word)
        return ' '.join(replaced_text)


def replace_words_with_romanian_synonyms(text):
    words = text.split()
    num_replacements = max(1, int(0.2 * len(words)))
    replaced_text = []
    changes = []

    for word in words:
        if num_replacements > 0:
            synonyms = get_romanian_synonyms(word)
            if synonyms:
                single_word_synonyms = [syn for syn in synonyms if ' ' not in syn]
                if single_word_synonyms:
                    synonym = random.choice(single_word_synonyms)
                    replaced_text.append(synonym)
                    changes.append(f"{word} -> {synonym}")
                    num_replacements -= 1
                else:
                    replaced_text.append(word)
            else:
                replaced_text.append(word)
        else:
            replaced_text.append(word)

    print("\nChanges made:")
    print("\n".join(changes))
    return ' '.join(replaced_text)


def get_synonym(word):
    synsets = wordnet.synsets(word)
    if synsets:
        synonyms = [lemma.replace('_', ' ') for lemma in synsets[0].lemma_names() if '_' not in lemma and len(lemma) > 1]
        if synonyms:
            return random.choice(synonyms)
    return None


def get_romanian_synonyms(word):
    synset_ids = wn.synsets(literal=word)
    synonyms = set()

    for synset_id in synset_ids:
        synset = wn.synset(synset_id)
        for literal in synset.literals:
            if '_' not in literal and literal.isalpha():
                synonyms.add(literal)

    synonyms.discard(word)
    return list(synonyms) if synonyms else None


source = input("\nEnter the text or file path: ")
text = load_text(source)
detected_language = detect_language(text)
print(f"\nDetected language: {detected_language}")
stylometry_analysis(text)

alternative_text = generate_alternative_text(text, 'ro')

max_ngram_size = 3
deduplication_threshold = 0.9
numOfKeywords = 1
custom_kw_extractor = yake.KeywordExtractor(lan=detected_language, n=max_ngram_size, dedupLim=deduplication_threshold, top=numOfKeywords, features=None)
keywords = custom_kw_extractor.extract_keywords(text)

generator = pipeline('text-generation', model='gpt2')

for kw in keywords:
    keyword = kw[0]
    prompt = f"Genereaza o propozitie cu cuvantul '{keyword}' in limba Romana:"
    generated_sentence = generator(prompt, max_length=50, num_return_sequences=1)[0]['generated_text']
    print(f"Keyword: {keyword}\nGenerated Sentence: {generated_sentence}\n")
