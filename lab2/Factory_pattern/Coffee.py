STEP_DELAY = 3

class Coffee:
	def __init__(self, name):
		self.name = name

	def __str__(self):
		return self.name

	def prepare(self, name):
		self.name = name
		# time.sleep(STEP_DELAY)