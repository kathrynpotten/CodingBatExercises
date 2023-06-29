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

###Return a count of the number of times
# a substring of length 2 appears in the
#  string and as the last 2 characters ###

def last2(str):
	if len(str) <= 2:
		count = 0 
	else: 
		last = str[-2:]
		count = -1
		while len(str) >= 2:
			if str.find(last) != -1:
				count +=1
				str = str[str.find(last)+1:]
	return count

### Return the number of 9s in an array ###

def array_count9(nums):
	return nums.count(9)

### Return True if one of first 4 elements is a 9 ###

def array_front9(nums):
	return nums[:4].count(9) > 0

### Return True if sequence 1,2,3 appears in array ###

def array123(nums):
	is1 = nums.count(1)
	is2 = nums.count(2)
	is3 = nums.count(3)
	if is1 or is2 or is3 == 0:
		return False
	for i in range(is1):
		idx1 = nums.index(1)
		nums = nums[idx1+1:]
		idx2 = nums.index(2)
		idx3 = nums.index(3)
		if idx2 - idx1 != 1 or idx3 - idx2 != 1:
			return False
		return True
	


