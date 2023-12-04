MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}

def text_to_morse():
    morse=""
    text=input("Enter The text : ")
    text=text.upper()
    for char in text:
        if char in MORSE_CODE_DICT:
           morse+=MORSE_CODE_DICT[char]+" " 
        else:
            morse+=" "
    print("MORSE CODE = ",morse)
    
def morse_to_text():
    text = ""
    morse_code = input("Enter Morse Code (use spaces between characters): ")
    morse_code = morse_code.split(" ")
    
    for code in morse_code:
        for key, value in MORSE_CODE_DICT.items():
            if code == value:
                text += key
        if code == "":
            text += " "
    print("TEXT = ",text)

while True:
    ch=int(input("1. Text to Morse Code\n2. Morse Code to Text\n3. Exit\nEnter Your Choice : "))
    if ch==1:
        text_to_morse()
    elif ch==2:
        morse_to_text()
    elif ch==3:
        break
    else:
        print("Invalid Choice")
