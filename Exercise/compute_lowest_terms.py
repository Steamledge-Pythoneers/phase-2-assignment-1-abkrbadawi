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
	x = x.split("/")
	n = int(x[0])
	d = int(x[1])
	indication = ""
	if n<0 and d<0:
		indication = ""
	elif n<0 or d<0:
		indication = "-"
	if n == 0 and d !=0:
		return "0"
	if d == 0:
		return "Undefined"
	n = abs(n)
	d = abs(d)
	hcf = n
	d_copy = d
	while d_copy !=0:
		i = d_copy
		d_copy = hcf%d_copy
		hcf = i
	return "{}{}/{}".format(indication,int(n/hcf),int(d/hcf))
