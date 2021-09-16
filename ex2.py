def pol(word, i):
    if len(word) / 2 == i - 1 or (len(word) % 2 != 0 and len(word) / 2 == i - 0.5):
        return True
    elif word[i] == word[-(i + 1)]:
        return pol(word, i + 1)
    else:
        return False


word = ['aba', 'abgd', 'aaaa', 'a', 'VlLv', 'Vlad']
for i in word:
    if pol(i.lower(), 0):
        print(f"Слово {i} - полиндром")
    else:
        print(f"Слово {i} - не полиндром")