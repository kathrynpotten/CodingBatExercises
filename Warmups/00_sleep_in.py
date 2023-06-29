### Parameter weekday true if weekday,
# vacation True if on vacation. 
# We sleep in if it's not a weekday or we're on vacation ###




def sleep_in(weekday,vacation):
	return not(weekday == True and vacation != True)
