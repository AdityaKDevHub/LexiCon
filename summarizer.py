import nltk
import string
from nltk.tokenize import word_tokenize, sent_tokenize
nltk.download('punkt', quiet=True)

def Summarize(corpus):
    word_dict = {}
    sent_dict = {}

    words = word_tokenize(corpus)
    sentences = sent_tokenize(corpus)
    length = len(sentences) // 3

    for word in words:
        word_dict[word] = 1 / words.count(word)

    for sentence in sentences:
        score = 0

        for word in word_tokenize(sentence):
            score += word_dict[word]

        sent_dict[sentence] = score

    first_sentence = sentences[0]
    top_sentences = sorted(sent_dict, key=sent_dict.get, reverse=True)[:length]
    summary = [first_sentence] + [s for s in sentences if s in top_sentences]
    summary_text = ' '.join(summary)

    return summary_text