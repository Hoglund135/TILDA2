class Node():

	def __init__(self, key, value):
		self.key = key
		self.value = value

	def __str__(self):
		return str(self.key) + ', ' + str(self.value)

class Hashtabell():

	def __init__(self, size):
		# Skapar en tom hashtabell av lämplig storlek
		self.size = n
		self.table = [None]*n

	def hasKey(self, key):
		h = self.hashFunc(key)
		p = self.table[h]
		n = 1

		while p is not None and p.key != key:
			h = self.rehashFunc(h,n)
			p = self.table[h]
			n += 1
		
		if p is not None and p.key == key:
			return True
		
		else:
			return False

	def hashFunc(self, key):
		hashValue = ''

		for char in key:
			hashValue = hashValue + str(ord(char))
		
		hashValue = int(hashValue) % self.size
		
		return hashValue

	def rehashFunc(self, hashedKey, n):
		return hashedKey + n^2

	def put(self, key, value):
		node = Node(key, value)
		h = hashFunc(key)
		
		if self.table[h] is None:
			self.table[h] = node
		
		else:
			while True:
				n = 1
				h = self.rehashFunc(h,n)
				
				if self.table[h] is None:
					self.table[h] = node
					break
				
				n += 1

	def get(self, key):
		if hasKey(key):

class KeyError(Exception):

	def __init__(self,key):
		self.key = key

	def __str__(self):
		return self.key + ' finns inte i hashtabellen!'