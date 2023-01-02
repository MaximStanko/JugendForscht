# Funktion von "punkt_in_polygon.py" wird benötigt
def punkt_in_polygon(v: list, p: tuple) -> int:
	''' der Ausgabewert entspricht folgenden Fällen:
		0 -> Punkt außerhalb des Polygons
		1 -> Punkt innerhalb des Polygons
		2 -> Punkt auf dem Rand des Polygons
	'''
	c = 0 # Zähler für Schnittpunkte

	for k in range(len(v)): # jede Kante auf Schnittpunkte testen
		q, r = v[k-1], v[k] # Variablen erstellen
		if q[1] > r[1]:
			q, r = r, q # Q soll niedrigeren y-Wert haben
		
		dxr, dyr = (r[0] - q[0]), (r[1] - q[1]) # Abstände zwischen R und Q
		dxp, dyp = (p[0] - q[0]), (p[1] - q[1]) # Abstände zwischen P und Q

		if p[0] > max(q[0], r[0]):
			continue # Strahl liegt rechts von Kante

		if dxp * dyr - dyp * dxr == 0 and p[0] >= min(q[0], r[0]):
			return 2 # Punkt liegt auf Kante

		epsilon = 1e-5 if p[1] == q[1] or p[1] == r[1] else 0 # Grenzfälle vermeiden

		if p[1] + epsilon < q[1] or p[1] + epsilon > r[1]:
			continue # Strahl liegt über oder unter Kante
		
		if (dxr == 0 or dxp == 0 or # Kante parallel zur y-Achse
			p[0] <= min(q[0], r[0]) or # Strahl links von Kante
			(dyp + epsilon) / dxp > dyr / dxr): # Anstieg zu P größer
			c += 1 # Strahl verläuft durch Kante
	
	return c % 2 # Parität entscheidet, ob innerhalb oder außerhalb


# Hauptfunktion
def pick_flaeche(v: list) -> float:
	i = 0 # Innenpunkt-Zähler
	r = 0 # Randpunkt-Zähler

	# Eckpunkte des minimal umgebenden Rechtecks berechnen
	punkt_links_unten = [min(p[0] for p in v), min(p[1] for p in v)]
	punkt_rechts_oben = [max(p[0] for p in v), max(p[1] for p in v)]

	# Schleife über alle Gitterpunkte des Rechtecks
	for x in range(punkt_links_unten[0], punkt_rechts_oben[0] + 1):
		for y in range(punkt_links_unten[1], punkt_rechts_oben[1] + 1):
			in_polygon = punkt_in_polygon(v, (x, y)) # Ray-Casting
			if in_polygon == 1:
				i += 1 # Punkt ist ein Innenpunkt
			elif in_polygon == 2:
				r += 1 # Punkt ist ein Randpunkt
	
	return i + r / 2 - 1 # Satz von Pick anwenden