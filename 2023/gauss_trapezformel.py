def gauss_trapezformel(v: list) -> float:
	F = 0

	for k in range(len(v)):
		F += (v[k - 1][1] + v[k][1]) * (v[k - 1][0] - v[k][0])
	
	return F / 2