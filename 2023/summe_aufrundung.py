from math import ceil # Aufrundungsfunktion

# Funktion von "euklid_ggT.py" wird benötigt
def euklid_ggT(a: int, b: int) -> int:
	if b == 0:
		return abs(a) # Fakt 1: ggT(a, 0) = 0
	
	return euklid_ggT( b, a % b ) # Fakt 2: ggT(a, b) = ggT(a mod b, b)


# Hauptfunktion (naiv)
def summe_aufrundung_naiv(b: int, n: int) -> int:
	s = 0

	for k in range(1, n + 1):
		s += ceil( k / n * b ) # einzelnen Summand hinzuaddieren

	return s


# Hauptfunktion (Formel)
def summe_aufrundung_formel(b: int, n: int) -> int:
	return ( n * b + n + b - euklid_ggT(n, b) ) // 2