#!/usr/bin/python

def encryptCaesarCipher(text, s):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if (char.isupper()):
            result += chr((ord(char) + s - 65) % 26 + 65)
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)
    return result


def hackCaesarCipher(message, knownKey = None):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    result = ''
    if knownKey is None:
        searchSet = range(len(alphabet))
    else:
        searchSet = [knownKey]

    for key in searchSet:
        translated = ''
        for symbol in message:
            if symbol in alphabet:
                num = alphabet.find(symbol)
                num = num - key
                if num < 0:
                    num = num + len(alphabet)
                translated = translated + alphabet[num]
            else:
                translated = translated + symbol
        result = result+'Hacking key #'+str(key)+': '+str(translated)+'\n'
    return result


def main():
    # Mensaje original ------------------------------------------------------------
    messagePlaintext = "BIENVENIDO A CASA"
    print("\n\nTexto original: "+messagePlaintext)

    # Encriptado usando el cifrado Cesar ------------------------------------------
    shift = 15
    print("\nOffset de codificado: " + str(shift))
    messageCaesarCipher = encryptCaesarCipher(messagePlaintext, shift)
    print("Mensaje codificado (Cesar Cipher): " + str(messageCaesarCipher))

    # Hackeando el cifrado Cesar una vez ------------------------------------------
    r1 = hackCaesarCipher("KDSSB ELUWKGDB")
    print("Resultado de hackeo sin saber el offset:\n"+r1)

    r2 = hackCaesarCipher("QXTCKTCXSDcPcRPHP",15)
    print("Resultado de hackeo sin saber el offset:\n" + r2)


if __name__ == '__main__':
   main()
