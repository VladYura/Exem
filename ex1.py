def card(number):
    l = len(number) - 4
    return ("*" * l + number[-4:])

print(card("1234567812345678"))