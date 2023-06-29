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

