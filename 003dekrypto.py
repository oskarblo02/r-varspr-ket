vokaler = 'AEIOUYÅÄÖ'

fråga = [
    ('Vill du kryptera eller dekryptera(K eller D)?', 'k'),
]

def main() -> None:
    for i in fråga:
        answer = str(input(i[0]))
        if answer.lower() == i[1]:
            word = input('Vad vill du översätta? ')
            final_word = rövarspråket(word)
            print(final_word)
        else:
            word = input('Vad vill du översätta? ')
            final_word = decode_rövarspråket(word)
            print(final_word)

def is_vowel(letter: str) -> bool:
    return letter.upper() in vokaler

def rövarspråket(word: str) -> str:
    new_word = []
    for tecken in word:
        new_word.append(tecken)
        if tecken.isalpha() and not is_vowel(tecken):
            new_word.append('o' + tecken.lower())

    return ''.join(new_word)

def decode_rövarspråket(word: str) -> str:
    original_word = []
    i = 0
    while i <= (len(word) - 1):
        tecken = word[i]
        original_word.append(tecken)
        if tecken.isalpha() and not is_vowel(tecken):
            i += 3
        else:
            i += 1
    return ''.join(original_word)

if __name__ == '__main__':
    main()