# Dictionary representing the morse code chart
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


def convert():
    converted_message = ""
    while True:
        mode = int(input("Enter '1' for Message --> Morse Code\n"
                         "Enter '2' for Morse Code --> Message"))
        message = input("Enter your message: ").upper()
        if mode == 1:
            for element in message:
                converted_message += MORSE_CODE_DICT[element] + " "
            print(converted_message)
        elif mode == 2:
            morse_message = message.split(" ")
            for element in morse_message:
                value_list = list(MORSE_CODE_DICT.values())
                key_list = list(MORSE_CODE_DICT.keys())
                position = value_list.index(element)
                converted_message += key_list[position]
            print(converted_message)
        else:
            continue
        if input("Do you want to enter another message? Enter 'Y' or 'N'").upper() == 'Y':
            continue
        else:
            break


if __name__ == "__main__":
    convert()