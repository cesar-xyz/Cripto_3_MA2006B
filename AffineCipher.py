#!/usr/bin/python

def encryptAffineCipher(text, a, b):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if (char.isupper()):
            ch = ord(char) - 65
            result += chr((ch * a + b) % 26 + 65)
        else:
            ch = ord(char) - 97
            result += chr((ch * a + b) % 26 + 97)
    return result


def hackAffineCipher(message, knownKey=None):
    result = ''
    return result


def main():
    # Mensaje original ------------------------------------------------------------
    messagePlaintext = "TEC"
    print("\n\nTexto original: " + messagePlaintext)

    # Encriptado usando el cifrado Cesar ------------------------------------------
    # a = 9 y b = 13
    messageCaesarCipher = encryptAffineCipher(messagePlaintext, 9, 13)
    print("Mensaje codificado (Cesar Cipher): " + str(messageCaesarCipher))


if __name__ == '__main__':
    main()
