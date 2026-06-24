from morse_dict import MORSE_CODE,REVERSE_MORSE
def text_to_morse(text):
    text=text.upper()
    morse=[]
    for i in text:
        if i in MORSE_CODE:
            morse.append(MORSE_CODE[i])
    return " ".join(morse)
def morse_to_text(morse):
    words=morse.split(' / ')
    decoded_words=[]
    for i in words:
        letters = i.split(' ')
        decoded=''.join(REVERSE_MORSE.get(j,'')for j in letters)
        decoded_words.append(decoded)
    return ' '.join(decoded_words)

