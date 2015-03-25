class Hashtabell():

	def __init__(self, n, tabell = {}):
		self.size = n
		self.tabell = tabell

	def put(self, key, value):
		self.tabell[key] = value
		
	def get(self, key):
		return self.tabell[key]