from line.config import delimiters

def is_delimiter(char, my_delimiters = delimiters):
    return char in my_delimiters