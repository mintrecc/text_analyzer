from length.helpers import is_delimiter
from  ..config import delimeters_for_sentence

def tokenize(text):
    words = []
    word = ""
    first_ind = 0
    end_ind = 0
    for i in range(len(text)):
        is_delimit = is_delimiter(text[i])

        if not is_delimit:
            end_ind += 1

        if is_delimit:
            word = text[first_ind:end_ind]
            words.append(word)
            first_ind = end_ind+1
            end_ind += 1
    return words







