# Funktion von "gauss_trapezformel.py" wird benötigt
def gauss_trapezformel(v: list) -> float:
	F = 0

	for k in range(len(v)):
		F += (v[k - 1][1] + v[k][1]) * (v[k - 1][0] - v[k][0])
	
	return F / 2

# Funktion von "euklid_ggT.py" wird benötigt
def euklid_ggT(a: int, b: int) -> int:
	if b == 0:
		return abs(a) # Fakt 1: ggT(a, 0) = 0
	
	return euklid_ggT( b, a % b ) # Fakt 2: ggT(a, b) = ggT(a mod b, b)

# Funktion von "randpunkte.py" wird benötigt
def randpunkte(v: list) -> int:
	r = 0

	for k in range(len(v)): # Summe der ggT
		r += euklid_ggT(v[k][0] - v[k - 1][0], v[k][1] - v[k - 1][1])
	
	return r


# Hauptfunktion
def innenpunkte(v: list) -> int:
	F = gauss_trapezformel(v) # Flächeninhalt
	r = randpunkte(v) # Randpunkte

	return int(F - r / 2 + 1) # Innenpunkte nach Satz von Pick