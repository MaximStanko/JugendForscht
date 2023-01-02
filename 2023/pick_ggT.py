from math import ceil # Aufrundungsfunktion

def pick_ggT(a: int, b: int) -> int:
	a, b = min(abs(a), abs(b)), max(abs(a), abs(b))
	s = 0
	
	for k in range(1, a + 1): # Summe mittels Schleife berechnen
		s += ceil( b / a * k ) # Aufrundungsfunktion anwenden
	
	return a * b + a + b - 2 * s # finale Berechnung