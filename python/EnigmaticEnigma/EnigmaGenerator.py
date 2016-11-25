#!/usr/bin/python3
# -*-coding:Utf-8 -*

from random import shuffle, choice, randint
from re import finditer, escape


class EnigmaGenerator:
	"""Generate enigma"""
	
	TEXT_1 = """
Python a été créé par Guido Van Rossum en 1990, son nom est une référence aux Monty Python.
Il s'est autoproclamé BDFL, Benevolent Dictator For Life, c'est-à-dire Dictateur Bienveillant à Vie,
dans la pure tradition initiée par Linus Torvald, fondateur du Kernel, le noyau de Linux.
Il veille au développement de Python et est l'autorité ultime concernant la conception de Python.
""".strip().replace('\n', ' ')
	
	TEXT_2 = """
Les PEP, Python Enhancement Proposal, sont les spécifications concernant le développement de Python.
Ils décrivent les ajouts et modifications à la syntaxe du langage et à la librairie standard, ainsi qu'au processus de développement.
Ils sont proposés par un auteur qui est alors en charge de mener et synthétiser les débats au sein de la communauté.
Une fois acceptée, une PEP est alors implémentée dans Python et paraitra lors de la prochaine mise à jour.
Deux PEP particulièrement importante sont à lire et garder à l'esprit :
la PEP 8, Coding Style for Python, décrit les standards de mise en forme du code et se doit d'etre respectée par tout programmeur,
tandis que la seconde, la PEP 20, Zen of Python, expose la philosophie de Python.
Elle dresse une liste ordonnée des principes de programmation ayant guidée le développement
de Python et devant guider la programmation en Python. Il est d'usage de faire primer lors d'un débat ou lors d'une prise de choix
les principes de la philosophie de Python devant tout autre argument.
Il reste néanmoins important de conserver un esprit critique envers ses préceptes.
""".strip().replace('\n', ' ')

	TEXT_3 = """
Python est en 2016 selon l’Institute of Electrical and Electronics Engineers (IEEE) le 3ème langage le plus utilisé au monde.
Son interpréteur CPython étant opensource et son utilisation quasi universelle,
il est intégré par défaut dans toutes les distributions du monde (excepté Windows).
Il est de manière générale particulièrement apprécié par les utilisateurs de GNU.
C'est le second langage le plus utilisé dans le monde opensource directement derrière le C.
""".strip().replace('\n', ' ')
	
	@classmethod
	def generate(cls, text, mode='complete'):
		"""Generate a complete enigma from a text
		
		Takes:
			text {str} The text to solve
			mode {str} 'complete' (by default), 'resolvable', 'riddlable'
		Returns:
			{str}, An uncomplete text, where letters have been replaced by underscores
			{list} An enigmatic representation of the text to complete, where each item represents a character
		"""
		
		if not mode in ('complete', 'resolvable', 'riddlable'):
			raise ValueError('{} is not a valid mode.'.format(mode))
		
		# Get all letters
		letters = []
		for letter in text:
			if not letter in letters:
				letters.append(letter)
		
		# Shuffle
		shuffle(letters)
		
		# Create dictionary
		dictionary = dict(zip(letters, range(len(letters))))
		
		# Create uncomplete text
		uncomplete_text_characters = ['_'] * len(text)
		for letter in letters:
			if mode == 'resolvable' and letter == letters[0]:
				continue
			if mode == 'riddlable' and letter in ('e', 'a', 'i'):
				continue
			
			# Get indexes of all occurences of letter in text
			indexes = [match.start() for match in finditer(escape(letter), text)]
			assert len(indexes)
			
			# Choice one or two indexes and
			for i in range(randint(1, 2)):
				index = choice(indexes)
				uncomplete_text_characters[index] = letter
		uncomplete_text = ''.join(uncomplete_text_characters)
		
		translated_text = [dictionary[letter] for letter in text]
		
		return uncomplete_text, translated_text


if __name__ == '__main__':
	# Tests
	uncomplete_text, enigma = EnigmaGenerator.generate(EnigmaGenerator.TEXT_1)
	assert('e' in uncomplete_text)
	
	uncomplete_text, enigma = EnigmaGenerator.generate(EnigmaGenerator.TEXT_1, mode='riddlable')
	assert(not 'e' in uncomplete_text)
	
	# Print
	with open('samples', 'w') as file:
		for text, mode in (EnigmaGenerator.TEXT_1, 'complete'), (EnigmaGenerator.TEXT_2, 'resolvable'), (EnigmaGenerator.TEXT_3, 'riddlable'):
			file.write(mode.upper() + '\n\n')
			for i in range(5):
				uncomplete_text, enigma = EnigmaGenerator.generate(text)
				file.write('uncomplete_text, enigma = "{}", {}\n\n'.format(uncomplete_text, enigma))
			file.write('-' * 50 + '\n\n')
