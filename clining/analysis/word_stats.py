from line.config import CASE_SENSITIVE

def count_words(tokens):
    count = len(tokens)
    return count


def count_words_len(tokens, n):
    count = 0
    for token in tokens:
        if len(token) == n:
            count += 1
    return count


def count_unique_words(tokens, my_case_sensitive = CASE_SENSITIVE):
    words = set()
    lower_tokens = []

    if not my_case_sensitive:
        for token in tokens:
            lower_tokens.append(token.lower())
    else:
        lower_tokens = tokens

    for token in lower_tokens:
        words.add(token)
    count = len(words)
    return count

def count_titlecase_words(tokens):
    count = 0
    for token in tokens:
        if token.istitle():
            count += 1
    return count

