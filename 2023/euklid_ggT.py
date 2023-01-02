def euklid_ggT(a: int, b: int) -> int:
	if b == 0:
		return abs(a) # Fakt 1: ggT(a, 0) = 0
	
	return euklid_ggT( b, a % b ) # Fakt 2: ggT(a, b) = ggT(a mod b, b)