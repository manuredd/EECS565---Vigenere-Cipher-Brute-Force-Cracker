'''
Manu Redd
EECS 565
Mini Project 1
'''
# Define the alphabet dictionary with both lowercase and uppercase letters
alphabet = {
    'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10,
    'l': 11, 'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20,
    'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25, 'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5,
    'G': 6, 'H': 7, 'I': 8, 'J': 9, 'K': 10, 'L': 11, 'M': 12, 'N': 13, 'O': 14, 'P': 15, 'Q': 16,
    'R': 17, 'S': 18, 'T': 19, 'U': 20, 'V': 21, 'W': 22, 'X': 23, 'Y': 24, 'Z': 25
}

# Create the reverse alphabet dictionary to map numerical positions back to letters
reverse_alphabet = {v: k for k, v in alphabet.items()}
#print(reverse_alphabet)

# Encrypt with EK(m) = m + K mod 26
def vigenereEncrypt(plaintext_letter, key_letter):
    return reverse_alphabet[(alphabet[plaintext_letter] + alphabet[key_letter]) % 26]

# Decrypt with EK(m) = m - K mod 26
def vigenereDecrypt(cipher_letter, key_letter):
    return reverse_alphabet[(alphabet[cipher_letter] - alphabet[key_letter]) % 26]
    
#print(vigenereEncrypt("J", "E"))
#print(vigenereDecrypt("N", "E"))
