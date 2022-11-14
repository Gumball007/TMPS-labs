from Factory_pattern.Coffee import Coffee

class Latte(Coffee):
	def __init__(self):
		self.prepare()
		self.coffee = Coffee('latte')
		
	def prepare(self):
		Coffee.prepare(self, "latte")
		print('Heat milk')
		print('Put coffee powder inside filter')
		print('Place big cup on holder')
		print('Brew hot water throught filter to cup')
		print('Pour hot milk into cup')