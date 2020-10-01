## TODO: complete the function "lowest_terms" below

def lowest_terms(x):
	"""This is a function that accept a string in form of a fraction, calculate and return the lowest
	possible term of the string in form of a fraction.

	input parameter:
	x(string): a fraction in the form of numerator(n) and denominator(d)

	 Return:
	 	type: string
	 	the lowest form of fraction in the form of indicatin, (n/hcf) ,(d/hcf)
	 	"""
	#split the fraction into a list and assign the first element to n(numerator)
	#and the second element to d(denominator)
	x = x.split("/")
	n = int(x[0])
	d = int(x[1])
	#indicate the sign of the final answe
	indication = ""
	if n<0 and d<0:
		indication = ""
	elif n<0 or d<0:
		indication = "-"
	#check for 0 and "undefined"
	if n == 0 and d !=0:
		return "0"
	if d == 0:
		return "Undefined"
	#get the absolute value of numerator and denominator
	n = abs(n)
	d = abs(d)
	#store the value of numerator and denominator in hcf and d respectively
	#to find the highest common factor
	hcf = n
	d_copy = d
	#find the highest common factor
	while d_copy !=0:
		i = d_copy
		d_copy = hcf%d_copy
		hcf = i
	#return the value of indication, numerator, denominator and hcf in the format
	#below
	return "{}{}/{}".format(indication,int(n/hcf),int(d/hcf))
