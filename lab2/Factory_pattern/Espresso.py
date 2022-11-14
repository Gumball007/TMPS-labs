from Factory_pattern.Coffee import Coffee

class Espresso(Coffee):
	def __init__(self):
		self.prepare()
		self.coffee = Coffee('espresso')
		
	def prepare(self):
		Coffee.prepare(self, "espresso")
		print('Pressurize water')
		print('Compact coffee powder inside capsule')
		print('Place small cup on holder')
		print('Jet hot water throught capsule grid to cup')