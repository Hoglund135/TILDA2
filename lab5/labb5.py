from hashtest import skapaAtomlista, lagraHashtabell

def main():
	atomlista = skapaAtomlista()
	hashtabell = lagraHashtabell(atomlista)
	while True:
		atomnamn = input('Ange ett atomnamn (t.ex. Au): ')
		try:
			 atom = hashtabell.get(atomnamn)
			 print(atom)
		except:
			print('\nAtomen finns inte i tabellen!\n')

main()