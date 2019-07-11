#!/usr/bin/env python3
# de SQ3SWF

import sys

if len(sys.argv) < 2:
	print(f"Usage: {sys.argv[0]} \"your text\"")
	sys.exit(1)

text = sys.argv[1].lower()

symbols = { 'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.', 'g': '--.', 'h': '....', 'i': '..', 'j': '.---',
	'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---', 'p': '.--.', 'q': '--.-', 'r': '.-.', 's': '...', 't': '-', 'u': '..-',
	'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--', 'z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
	'5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '/': '-..-.', '=': '-...-', '?': '..--..', ',': '--..--' }

raw = { '.': '1', '-': '111' }

# split input text into words
words = text.split(' ')

# replace letters within each word with dits/dahs
dits_dahs = [ [symbols[q] for q in x] for x in words ] 
print( ' / '.join([ ' '.join(letter) for letter in dits_dahs ] ) )

# replace each symbol, of each letter, of each word with "0"s or "1"s...
# .. and join symbols within letters using single '0', letters using '000' and words using '0000000'
out = (7*'0').join([ (3*'0').join([ '0'.join([ raw[symbol] for symbol in letter ]) for letter in word]) for word in dits_dahs ])

# print with brackets, comma separated
print('('+','.join(out)+')')
