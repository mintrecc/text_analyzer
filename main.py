
import sys

from length.output.printer import *


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

    words = tokenize(text)
    print(print_report_in_table(words))

if __name__ == '__main__':
    main()