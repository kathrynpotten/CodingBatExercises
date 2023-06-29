### Warm-up exercises set 1 ###

### Given integer, return absolute difference with 21, but return double difference if n > 21 ###

def diff21(n):
	if n > 21 :
		return 2*(n-21)
	else:
		return 21-n


### If talking and hour is before 7 or after 20, return True ###

def parrot_trouble(talking, hour):
	return talking == True and (hour < 7 or hour > 20)


### Given 2 integers, return true if one of them is 10 or their sum is 10 ###

def makes10(a,b):
	return a == 10 or b == 10 or a+b==10



### Given an integer, return True if within 10 of 100 or 200 ###

def near_hundred(n):
	return abs(100-n) <= 10 or abs(200-n) <= 10


### Given 2 integers, return True if one negative and one positive, 
#unless negative==True, when return only if both are negative ###

def pos_neg(a,b,negative):
	if negative == True:
		return a < 0 and b < 0
	else:
		return a*b < 0 

### Given a string, return the same string with 'not' added in front. 
#If it already begins with 'not', leave unchanged ### 

def not_string(str):
	if str[:3] == 'not':
		return str
	else:
		return 'not ' + str

### Given a non-empty string and an integer n, return string with character n removed ###

def missing_char(str,n):
	return str[:n] + str[n+1:]


### Return a new string where first and last characters have been exchanged ###

def front_back(str):
	if len(str) <=1:
		return str
	return str[-1] + str[1:-1] + str[0]

### Given a string, return a string which is three copies of the first 3 characters ###

def front3(str):
	if len(str) < 3:
		return str + str + str
	return str[:3] + str[:3] + str[:3]