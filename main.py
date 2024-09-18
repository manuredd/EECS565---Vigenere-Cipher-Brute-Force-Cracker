'''
Manu Redd
EECS 565
Mini Project 1
'''

from itertools import product
from vigenere import vigenereDecrypt
from datetime import datetime
import sys

# Open dictionary file for reading
with open("MP1_dict.txt", "r") as file:
    # Read the contents of the file
    contents = file.readlines()  # Read lines into a list
    dictionary = {}  # Use a dictionary to store lists of lines by length
    
    for line in contents:
        line = line.strip()  # Strip whitespace/newline characters
        length = len(line)  # Get the length of the line
        
        # If the length is not a key in the dictionary, initialize it
        if length not in dictionary:
            dictionary[length] = []  # Initialize a list for this length
        
        dictionary[length].append(line)  # Add the line to the appropriate length list
        
    
    
def bruteForceCracker(ciphertext, key_length, first_word_length):
    solutions = []
    current_iter = 0
    for keys in product("ABCDEFGHIJKLMNOPQRSTUVWXYZ", repeat = key_length):
        key = ''.join(keys)
        #print(key)
        plaintext = ''
        progress = (current_iter / (26 ** key_length))*100
        sys.stdout.write("Percent of permutations tested: %d%%   \r" % (progress))
        sys.stdout.flush()
        
        for i, letter in enumerate(ciphertext):
            #print(i%key_length)
            plaintext += vigenereDecrypt(letter, key[i%key_length])
            
            if len(plaintext) == first_word_length:
                if plaintext not in dictionary.get(first_word_length, []):
                    #print(plaintext)
                    break  # Exit the loop if the first word is not valid
            
            # If we reach the end and have a valid first word, print it
            if i == len(ciphertext) - 1:
                #print(plaintext)
                solutions.append(f"Key: {key} -> Plaintext: {plaintext}")
        current_iter += 1        
    print(f'Ciphertext: {ciphertext}')
    for solution in solutions:
        print(solution)
    
def printTime():
    current_time = datetime.now().strftime("%H:%M:%S")
    print("\nCurrent Time:", current_time)

def main():
    printTime()
    bruteForceCracker("MSOKKJCOSXOEEKDTOSLGFWCMCHSUSGX", 2, 6)
    printTime()
    bruteForceCracker("PSPDYLOAFSGFREQKKPOERNIYVSDZSUOVGXSRRIPWERDIPCFSDIQZIASEJVCGXAYBGYXFPSREKFMEXEBIYDGFKREOWGXEQSXSKXGYRRRVMEKFFIPIWJSKFDJMBGCC", 3, 7)
    printTime()
    bruteForceCracker("MTZHZEOQKASVBDOWMWMKMNYIIHVWPEXJA", 4, 10)
    printTime()
    bruteForceCracker("SQLIMXEEKSXMDOSBITOTYVECRDXSCRURZYPOHRG", 5, 11)
    printTime()
    bruteForceCracker("LDWMEKPOPSWNOAVBIDHIPCEWAETYRVOAUPSINOVDIEDHCDSELHCCPVHRPOHZUSERSFS", 6, 9)
    printTime()
if __name__ == '__main__':
    main()