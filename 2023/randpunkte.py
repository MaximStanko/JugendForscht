# Funktion von "euklid_ggT.py" wird benötigt
def euklid_ggT(a: int, b: int) -> int:
	if b == 0:
		return abs(a) # Fakt 1: ggT(a, 0) = 0
	
	return euklid_ggT( b, a % b ) # Fakt 2: ggT(a, b) = ggT(a mod b, b)


# Hauptfunktion
def randpunkte(v: list) -> int:
	r = 0

	for k in range(len(v)): # Summe der ggT
		r += euklid_ggT(v[k][0] - v[k - 1][0], v[k][1] - v[k - 1][1])
	
	return r