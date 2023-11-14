from textblob import TextBlob
from gingerit.gingerit import GingerIt


class SpellCheckerModule:
	def __init__(self):
		self.spell_check = TextBlob("")
		self.grammar_check = GingerIt()


	def correct_spell(self,text):
	
	    #Hello, World, I, am, Anik,

		words = text.split()
		corrected_words = []
		for word in words:
			corrected_word = str(TextBlob(word).correct())
			corrected_words.append(corrected_word)
			return " ".join(corrected_words)	


	def correct_grammar(self,text):
		matches = self.grammar_check.parse(text)

		foundmistakes = []

		for error in matches['corrections']:
			foundmistakes.append(error['text'])
			foundmistakes_count = len(foundmistakes)
		return foundmistakes,foundmistakes_count


if __name__ == "__main__":
	obj = SpellCheckerModule()
	message =  "Hello! I'm Anik.Study at Daffodil Internationa Universiy"
	print(obj.correct_spell(message)) 
	print(obj.correct_grammar(message)) 

