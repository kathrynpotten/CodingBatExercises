### Monkeys a and b. In trouble when both or neither are smiling. Return True when we are in trouble ###

def monkey_trouble(a_smile, b_smile):
	if a_smile == True and b_smile == True or a_smile == False and b_smile == False:
		return True
	else:
		return False