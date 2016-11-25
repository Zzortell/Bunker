#!/usr/bin/python3
# -*-coding:Utf-8 -*


def solveComplete(uncomplete_text, enigma):
	# Create dictionary
	dictionary = dict(
		[(enigma[i], uncomplete_text[i]) for i in range(len(uncomplete_text)) if uncomplete_text[i] != '_']
	)

	return ''.join(
		[dictionary[letter] for letter in enigma]
	)
