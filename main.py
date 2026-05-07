import sys


from length.output.printer import *
from line.config import separate_by_sentence
from line.parser.tokenizer import tokenize_by_sentence
from length.output.export import *

class TextAnalyzer:
    def __init__(self, text):
        self.text = text

        self.sentences = tokenize_by_sentence(self.text)

        self.tokens = tokenize(self.text)

    def create_a_report(self):
        counted_words = count_words(self.tokens)
        counted_words_len = count_words_len(self.tokens, 3)
        counted_unique_words = count_unique_words(self.tokens)
        counted_titlecase_words = count_titlecase_words(self.tokens)
        counted_digits = count_digits(self.tokens)
        alternation_counted = alternation_count(self.tokens)

        report = {"Кількість слів": counted_words,
                    "Слів довжини 3": counted_words_len,
                    "Унікальних слів": counted_unique_words,
                    "Починаються з великої": counted_titlecase_words,
                    "Чисел": counted_digits,
                    "Кількість знакозмін": alternation_counted}

        return report

    def create_sentence_report(self):
        all_reports = []

        for sentence in self.sentences:
            words = tokenize(sentence)

            sentence_report = {
            "Кількість слів": count_words(words),
            "Слів довжини 3": count_words_len(words, 3),
            "Унікальних слів": count_unique_words(words),
            "Починаються з великої": count_titlecase_words(words),
            "Чисел": count_digits(words),
            "Кількість знакозмін": alternation_count(words)
            }

            all_reports.append(sentence_report)

        return all_reports

def main():

    if len(sys.argv) == 1:
        print('No arguments')
        sys.exit(1)

    elif '-f' in sys.argv:
        if len(sys.argv) == 2:
            file_name = 'length/data/test.txt'
        elif len(sys.argv) == 3 and sys.argv[2] == '-o':
            file_name = 'length/data/test.txt'
        else:
            file_name = sys.argv[sys.argv.index('-f') + 1]

        with (open(file_name, 'r', encoding='utf-8')) as file:
            text = file.read()

    else:
        if '-o' in sys.argv:
            text = " ".join(sys.argv[1:sys.argv.index('-o')])
        else:
            text = " ".join(sys.argv[1:])

    analyzer = TextAnalyzer(text)


    if separate_by_sentence:
        sentences_report = analyzer.create_sentence_report()
        if '-o' in sys.argv:
            export_report_json(sentences_report)
        for report in sentences_report:
            print("\n")
            print_report_in_table(report)



    if not separate_by_sentence:

        full_report = analyzer.create_a_report()
        if '-o' in sys.argv:
            export_report_json(full_report)
        print_report_in_table(full_report)

if __name__ == '__main__':
    main()