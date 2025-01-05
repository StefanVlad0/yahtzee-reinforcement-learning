import nltk
import matplotlib.pyplot as plt
import re
from collections import Counter
from wordcloud import WordCloud

nltk.download('punkt')
nltk.download('punkt_tab')


def stylometry_analysis(text):
    sentences = [sentence.strip() for sentence in text.split('.') if sentence.strip()]

    # remove delimiters
    text = re.sub(r'[\W_]+', ' ', text)

    words = nltk.word_tokenize(text)

    num_words = len(words)
    num_sentences = len(sentences)
    avg_word_length = sum(len(word) for word in words) / num_words
    avg_sentence_length = num_words / num_sentences

    word_freq = Counter(words)

    most_common_words = word_freq.most_common(20)

    print("\nStylometric Analysis:")
    print(f"Total words: {num_words}")
    print(f"Total sentences: {num_sentences}")
    print(f"Average word length: {avg_word_length:.2f} characters")
    print(f"Average sentence length: {avg_sentence_length:.2f} words")

    plt.figure(figsize=(12, 6))
    words, frequencies = zip(*most_common_words)
    plt.bar(words, frequencies)
    plt.title("Word Frequency Distribution")
    plt.xlabel("Words")
    plt.ylabel("Freq")
    plt.xticks(rotation=45)
    plt.show()

    wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(word_freq)
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.show()
