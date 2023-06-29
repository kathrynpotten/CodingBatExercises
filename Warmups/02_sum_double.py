### For two integer values return sum, unless equal, then return double their sum ###

def sum_double(a,b):
	if a == b:
		return 2*(a+b)
	else:
		return a+b