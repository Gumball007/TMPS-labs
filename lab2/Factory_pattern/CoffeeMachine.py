from Factory_pattern.Espresso import Espresso
from Factory_pattern.Latte import Latte

class CoffeeMachine(object): 
	def make(self, coffee_name):
		if coffee_name == 'Espresso': return Espresso()
		if coffee_name == 'Latte':    return Latte()
		assert 0, 'Bad shape creation: ' + type