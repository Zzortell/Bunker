#!/usr/bin/python3
# -*-coding:Utf-8 -*

from EnigmaGenerator import EnigmaGenerator
import solve


for text, mode in (EnigmaGenerator.TEXT_1, 'complete'), (EnigmaGenerator.TEXT_2, 'resolvable'), (EnigmaGenerator.TEXT_3, 'riddlable'):
	if hasattr(solve, 'solve' + mode.title()):
		for i in range(5):
			uncomplete_text, enigma = EnigmaGenerator.generate(text)
			answer = getattr(solve, 'solve' + mode.title())(uncomplete_text, enigma)
			assert(text == answer)
			print(answer, flush=True)
	else:
		print('solve module has no {} function'.format('solve' + mode.title()))
