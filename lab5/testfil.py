a = 'HEJ'
hashValue = 0
for char in a:
	hashValue += ord(char)
hashValue = hashValue % 100
print(hashValue)