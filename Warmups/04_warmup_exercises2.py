### Warm-up exercises set 2 ###

### Given a string and an integer n, return a string that is n copies ###

def string_times(str, n):
	return str*n

### Given a string and integer n, return n copies of the first 3 characters ###

def front_times(str,n):
	return str[:3]*n

### Return a string with every other character ###

def string_bits(str):
	return str[::2]

### Given a non-empty string of length n, return a string 
#made up of copies each with 1,2...n characters ###

def string_splosion(str):
	new_str = ''
	for i in range(len(str)):
		new_str +=  str[:i+1]
	return new_str
