import sys

from clining import analysis
from length.output.printer import *
from line.config import separate_by_sentence
from line.parser.tokenizer import tokenize_by_sentence


def main():


    if len(sys.argv) < 1:
        print('No arguments')
        sys.exit(1)

    if '-f' in sys.argv:
        if len(sys.argv) == 2:
            file_name = 'length/data/test.txt'
        else:
            file_name = sys.argv[sys.argv.index('-f') + 1]

        with (open(file_name, 'r', encoding='utf-8')) as file:
            text = file.read()

    else:
        text = " ".join(sys.argv[1:])

    if separate_by_sentence:
        sentences = tokenize_by_sentence(text)
        print(sentences)
        for sentence in sentences:
            words = tokenize(sentence)
            print("\n")
            print_report_in_table(words)



    if not separate_by_sentence:
        words = tokenize(text)
        print_report_in_table(words)

if __name__ == '__main__':
    main()