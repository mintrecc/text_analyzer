from clining.analysis.word_stats import *
from length.digit_stats import count_digits, alternation_count
from line.parser.tokenizer import tokenize







def print_report_in_table(text):
    w1 = 27
    w2 = 8
    w3 = 6
    border = "+" + "-" * w1 + "+" + "-" * w2 + "+"
    print(border)
    left_title = " Показник".ljust(w1)
    right_title = " Значення ".ljust(w2)
    print(f"|{left_title}|{right_title}|")
    print(border)
    print("| Кількість слів".ljust(w1), f"| {str(count_words(text)).rjust(w3)} |")
    print("| Cлів довжини 3".ljust(w1), f"| {str(count_words_len(text, 3)).rjust(w3)} |")
    print("| Унікальних слів".ljust(w1), f"| {str(count_unique_words(text)).rjust(w3)} |")
    print("| Починаються з великої".ljust(w1), f"| {str(count_titlecase_words(text)).rjust(w3)} |")
    print("| Чисел".ljust(w1), f"| {str(count_digits(text)).rjust(w3)} |")
    print("| Кількість знакозмін".ljust(w1), f"| {str(alternation_count(text)).rjust(w3)} |")
    print(border)



