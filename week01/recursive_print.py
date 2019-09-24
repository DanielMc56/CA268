def rprint(a, b):

	if a == b:
		return 0
	else:
	    print(a)
	    return rprint(a + 1, b)