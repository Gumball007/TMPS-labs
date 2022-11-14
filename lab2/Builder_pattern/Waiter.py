class Waiter:

	def __init__(self):
		self.builder1 = None
		self.builder2 = None

	def construct_pizza(self, builder1):
		self.builder1 = builder1
		[step() for step in (builder1.prepare_dough,
							 builder1.add_sauce, builder1.add_topping, builder1.bake)]
	
	def construct_coffee(self, builder2):				 
		self.builder2 = builder2
		
	@property
	def pizza(self):
		return self.builder1.pizza
	
	@property
	def coffee(self):
		return self.builder2.coffee