Caesar_Cipher_dic = {'A': 'f', 'B': 'g',
                     'C': 'h', 'D': 'i', 'E': 'j',
                     'F': 'k', 'G': 'l', 'H': 'm',
                     'I': 'n', 'J': 'o', 'K': 'p',
                     'L': 'q', 'M': 'r', 'N': 's',
                     'O': 't', 'P': 'u', 'Q': 'v',
                     'R': 'w', 'S': 'x', 'T': 'y',
                     'U': 'z', 'V': 'a', 'W': 'b',
                     'X': 'c', 'Y': 'd', 'Z': 'e', }


def encrpyt(plain_text):
    cipher = ''

    for letters in plain_text:
        if letters != ' ':
            if plain_text.lower() or plain_text.upper():
                cipher += Caesar_Cipher_dic[letters] + ''
        else:
            cipher += ' '

    return cipher.title()


def decrypt(plain_text):
    global j
    plain_text += ' '
    decipher = ''
    ci_text = ''

    for letters in plain_text:
        if letters != ' ':
            j = 0

            ci_text += letters
        else:
            j += 1
            if j == 2:
                decipher += ' '

            else:

                decipher += list(Caesar_Cipher_dic.keys())[list(Caesar_Cipher_dic.values()).index(ci_text)]
                ci_text = ''
    return decipher


def main():
    while True:
        """used the try statement to handle error if it occurs"""
        try:
            plain_text = input('Plain text: ')
            result = encrpyt(plain_text.upper())
            print(result)
            if plain_text == 'exit' or plain_text == 'EXIT':
                break
            else:
                print('\nDONE? enter "EXIT" \n ')

        except:
            print('Invalid character !! \n')
            continue

    print('')
    print('Thank you')


# Executes the main function
if __name__ == '__main__':
    main()
