import binascii
import string

def okkOokOo(s):
    conv_table = {}
    for char in string.printable:
        conv_table[(bin(int(binascii.hexlify(char), 16))).replace("b","")] = char

    print conv_table

    #Format s and convert to 'binary'
    convs = {' ':"",'?':'!',',':"","o":'0','k':'1'}
    characters = s.lower()
    for punc in convs:
        characters = characters.replace(punc,convs[punc])
    characters =  characters.split('!')
    return "".join([conv_table[letter] if len(letter) > 0 else "" for letter in characters])


print okkOokOo('Ok, Ook, Okk? Okk, Ok, Ook? Okk, Okkk, O? Okk, Ookkk? Ok, Ookkk? Okkk, Ookk? Ok, Ooooo? Ok, Ooook, O? Okk, Okkkk? Okkk, Ok, Oo? Okkk, Ok, Oo? Okk, Okk, Oo? Okk, Ook, Ok!')

{'01000001': 'A', '01000000': '@', '01111000': 'x', '01111001': 'y', '01100000': '`', '01100001': 'a', '01111011': '{', '01111010': 'z', '0100101': '%', '0100100': '$', '01100011': 'c', '01100010': 'b', '0111101': '=', '0111100': '<', '0101111': '/', '0101110': '.', '01011': '\x0b', '01010': '\n', '0110111': '7', '0110110': '6', '01010110': 'V', '01010111': 'W', '0101100': ',', '0101101': '-', '01000100': 'D', '01000101': 'E', '0100110': '&', '0100111': "'", '0111110': '>', '0111111': '?', '01001': '\t', '0110100': '4', '0110101': '5', '01101001': 'i', '01101000': 'h', '01000111': 'G', '01000110': 'F', '0100011': '#', '0100010': '"', '01001110': 'N', '01001111': 'O', '01011100': '\\', '01011101': ']', '01110010': 'r', '01110011': 's', '0101001': ')', '0101000': '(', '0100000': ' ', '0100001': '!', '01101': '\r', '01100': '\x0c', '01001101': 'M', '01001100': 'L', '0110001': '1', '0110000': '0', '01011111': '_', '01010101': 'U', '01010100': 'T', '01110001': 'q', '01110000': 'p', '01010000': 'P', '01010001': 'Q', '01110100': 't', '01110101': 'u', '01111110': '~', '01101100': 'l', '01101101': 'm', '01011110': '^', '01100110': 'f', '01100111': 'g', '0101010': '*', '0101011': '+', '0110010': '2', '0110011': '3', '01010011': 'S', '01010010': 'R', '01101010': 'j', '01011010': 'Z', '01011011': '[', '01101011': 'k', '01111101': '}', '01111100': '|', '01101111': 'o', '01101110': 'n', '01100101': 'e', '01100100': 'd', '0111011': ';', '0111010': ':', '01001000': 'H', '01001001': 'I', '01011001': 'Y', '01011000': 'X', '01000010': 'B', '01000011': 'C', '01001011': 'K', '01001010': 'J', '0111000': '8', '0111001': '9', '01110111': 'w', '01110110': 'v'}
