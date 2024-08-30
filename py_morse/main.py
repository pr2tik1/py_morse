MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.', '0': '-----',
    ', ': '--..--', '.': '.-.-.-', '?': '..--..', '/': '-..-.', '-': '-....-', '(': '-.--.', ')': '-.--.-'
}

TEXT_TO_MORSE_DICT = {value: key for key, value in MORSE_CODE_DICT.items()}

def text_to_morse(message):
    try:
        morse_code = ''
        clean_message = message.upper()
        for char in clean_message :
            if char in MORSE_CODE_DICT:
                morse_code += MORSE_CODE_DICT[char] + ' '
            elif char == ' ':
                morse_code += ' '
            else:
                morse_code += '?'
        return morse_code
    except Exception as e:
        return f"Error due to : {e}"


def morse_to_text(code):
    try:
        decode_text = ''
        code_list = code.split(' ')
        for char in code_list :
            if char in TEXT_TO_MORSE_DICT:
                decode_text += TEXT_TO_MORSE_DICT[char]
            elif char == ' ':
                decode_text += ' '
            else:
                decode_text += '?'
        return ''.join(decode_text)
    except Exception as e:
        return f"Error due to : {e}"
            

if __name__ == "__main__":
    code_or_decode = int(input('Encode(1) or Decode(2) ?\n'))
    
    if code_or_decode == 1:
        input_string = str(input("Please enter the message\n"))
        print(text_to_morse(input_string))
    elif code_or_decode == 2:
        input_string = str(input("Please enter the message (using '.' and '-')\n"))
        print(morse_to_text(input_string))
    else:
        print('Please use available options : 1 or 2 ')