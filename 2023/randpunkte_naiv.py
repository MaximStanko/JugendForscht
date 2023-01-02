def randpunkte_naiv(v: list) -> int:
	r = 0

	for k in range(len(v)): # über jede Kante iterieren
		dx, dy = v[k][0] - v[k - 1][0], v[k][1] - v[k - 1][1]
		
		if dx == 0: # achsenparallele Seite
			r += abs(dy)
			continue

		for x in range(abs(dx)): # überprüfe alle möglichen Punkte auf Gerade
			if (x * dy / dx).is_integer():
				r += 1
	
	return r