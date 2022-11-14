STEP_DELAY = 3

class Pizza:
	def __init__(self, name):
		self.name = name
		self.dough = None
		self.sauce = None
		self.topping = []

	def __str__(self):
		return self.name

	def prepare_dough(self, dough):
		self.dough = dough
		print('preparing the {} dough of your {}...'.format(self.dough.name, self))
		# time.sleep(STEP_DELAY)
		print('done with the {} dough'.format(self.dough.name))
