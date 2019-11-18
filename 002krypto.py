from gtts import gTTS

import os

def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter in "qwrtpsdfghjklzxcvbnmQWRTPSDFGHJKLZXCVBNM":
            translation = translation + letter + "o" + letter
        else:
            translation = translation + letter
    return translation

print(translate(input("Enter a phrase: ")))

mytext = translate(input())
language = 'sv'
myobj = gTTS(text=mytext, lang=language, slow=False)
myobj.save("hej.mp3")
os.system("hej.mp3")
