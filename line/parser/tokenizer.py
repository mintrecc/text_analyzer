from length.helpers import is_delimiter
from  ..config import delimiters_for_sentence


def tokenize_by_sentence(text):
    full_text = []
    first_ind = 0
    for i in range(len(text)):
        is_delimit = is_delimiter(text[i], delimiters_for_sentence)

        if is_delimit:

            sentences = text[first_ind:i]
            full_text.append(sentences)
            first_ind = i + 2

    return full_text


def tokenize(text):
    tokens = []
    first_ind = 0
    for i in range(len(text)):

        is_delimit = is_delimiter(text[i])

        if is_delimit:
            token = text[first_ind:i]
            tokens.append(token)
            first_ind = i+1

    tokens.append(text[first_ind:])
    tokens = [word for word in tokens if word != ""]

    return tokens







