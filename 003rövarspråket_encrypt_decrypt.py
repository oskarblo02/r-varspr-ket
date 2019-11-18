from gtts import gTTS

import os

# Alla vokaler
vowels = 'aouåeiyäö'

# Mina frågor ligger i dictionarys
question = [('Vill du kryptera eller dekryptera(K eller D)?\n', 'k', 'd')]
question2 = [('Vill du få det uppläst, ja eller nej(J eller N)?\n', 'j', 'n')]

# Här får man välja om man vill ha till eller från rövarstråket och vad man vill översätta
def main() -> None:
        for i in question:
            answer = str(input(i[0]))
            if answer.lower() == i[1]:
                word = input('Vad vill du översätta?\n')
                final_word = rövarspråket(word)
                print(final_word)
                text_to_speech(final_word)
            elif answer.lower() == i[2]:
                word = input('Vad vill du översätta?\n')
                final_word = decode_rövarspråket(word)
                print(final_word) 
                text_to_speech(final_word)
            else:
                print('404 error')

# Kollar om det finns vokaler
def is_vowel(letter: str) -> bool:
    return letter.lower() in vowels

# Gör om svenska till rövarspråket
def rövarspråket(text: str) -> str:
    translation = ''
    for letter in text:
        if letter in 'qwrtpsdfghjklzxcvbnmQWRTPSDFGHJKLZXCVBNM':
            translation = translation + letter + 'o' + letter
        else:
            translation = translation + letter
    return translation

# Gör om rövarspråket till svenska
def decode_rövarspråket(word: str) -> str:
    original_word = []
    i = 0
    while i <= (len(word) - 1):
        character = word[i]
        original_word.append(character)
        if character.isalpha() and not is_vowel(character):
            i += 3
        else:
            i += 1
    return ''.join(original_word)

# Läser upp det som är översätt
def text_to_speech(text):
    for i in question2:
        answer = str(input(i[0]))
        if answer.lower() == i[1]:
            language = 'sv'
            myobj = gTTS(text=phrase, lang=language, slow=False)
            myobj.save("rövarspråket.mp3")
            os.system("rövarspråket.mp3")
        elif (answer.lower() == i[2]):
            print(text)
        else:
            print('404 error')

if __name__ == '__main__':
    main()