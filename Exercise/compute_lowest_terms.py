## TODO: complete the function "lowest_terms" below

def lowest_terms(x):
	"""this is a function that accept a string in form of a fraction calculate and returns the lowest
    possible term of the string in form of a fraction.

    Input parameter:
        x (str): a fraction in the form 'numerator/denomenator'

    Returns:
        type: str
        the lowest form of the fraction in the form 'numerator/denomenator'
    """
	# split the fraction into a list and assign the elements to
	# numerator and denomenator
	x = x.split('/')
	numerator = int(x[0])
	denomenator = int(x[1])
	# define the sign of the final answer
	sign = ''
	if numerator < 0 and denomenator < 0:
		sign = ''
	elif numerator < 0 or denomenator < 0:
		sign = '-'
	# check for invalid inputs
	if numerator == 0 and denomenator !=0:
		return '0'
	if denomenator == 0:
		return 'Undefined'
	# make numerator and denomenator positive
	numerator = abs(numerator)
	denomenator = abs(denomenator)
	# store the values of numerator and denomenator to use in finding hcf
	hcf = numerator
	denum_copy = denomenator
	# find the highest common factor for numerator and denominator
	while denum_copy != 0:
		i = denum_copy
		denum_copy = hcf % denum_copy
		hcf = i
	return '{}{}/{}'.format(sign, int(numerator / hcf), int(denomenator / hcf))