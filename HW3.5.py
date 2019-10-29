stroka = 'abBcccd'.lower()
def on (stroka_func):
    letter_counts = {letter: stroka.count(letter) for letter in set(stroka)}
    return letter_counts
    print(letter_counts)
print(on(stroka))






