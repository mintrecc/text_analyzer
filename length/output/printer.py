from clining.analysis.word_stats import *
from length.digit_stats import count_digits, alternation_count
from line.parser.tokenizer import tokenize








def print_report_in_table(report):
    w1 = 27
    w2 = 8
    w3 = 6
    border = "+" + "-" * w1 + "+" + "-" * w2 + "+"
    print(border)
    left_title = " Показник".ljust(w1)
    right_title = " Значення ".ljust(w2)
    print(f"|{left_title}|{right_title}|")
    print(border)
    print("| Кількість слів".ljust(w1), f"| {str(report['Кількість слів']).rjust(w3)} |")
    print("| Cлів довжини 3".ljust(w1), f"| {str(report['Слів довжини 3']).rjust(w3)} |")
    print("| Унікальних слів".ljust(w1), f"| {str(report['Унікальних слів']).rjust(w3)} |")
    print("| Починаються з великої".ljust(w1), f"| {str(report['Починаються з великої']).rjust(w3)} |")
    print("| Чисел".ljust(w1), f"| {str(report['Чисел']).rjust(w3)} |")
    print("| Кількість знакозмін".ljust(w1), f"| {str(report['Кількість знакозмін']).rjust(w3)} |")
    print(border)



