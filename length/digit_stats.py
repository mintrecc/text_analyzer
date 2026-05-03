def count_digits(tokens):
    count = 0
    for token in tokens:
        if token.lstrip("+-").isdigit():
            count += 1
    return count

def alternation_count(tokens):
    POS = 1
    NEG = -1
    ZERO = 0

    previous_value = None
    current_value = None
    count = 0

    for token in tokens:

        strip_num = token.lstrip("+-")

        if strip_num.isdigit():

            token = int(token)

            if token == 0:
                continue

            if token < 0:
                current_value = NEG

            elif token > 0:
                current_value = POS

            if previous_value is not None and current_value != previous_value:
                count += 1

            previous_value = current_value

    return count