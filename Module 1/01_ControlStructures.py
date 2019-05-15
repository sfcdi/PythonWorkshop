primes = [2, 3, 5, 7, 11, 13]
x = 5

# check what type of number X is
if x in primes:
	print("X is prime")
	
elif x % 2 == 0:
	print("X is even")

else:
	print("X is odd")
	

# let's try some additional logic
# X is not prime
if x not in primes:
	print('X is not prime')
	
# X is not prime, and X is not divisible by two
if x % 2 != 0 and x not in primes:
	print('X is odd')
	
# X is prime or X is odd
if x in primes or x % 2 != 0:
	print('X is prime or odd')

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# iterate through all numbers using a for loop
# check what type of number it is
for n in numbers:

	# is it prime
	if n in primes:
			print(str(n) + " is prime")

	# is it even
	elif (n / 2) == 0:
		print(str(n) + " is even.")

	# is it odd
	elif (n / 2) != 0:
		print(str(n) + " is odd.")


# iterate through all numbers with a while loop
n = 0

# while x is less than zero check what type it is
while n < 100:

	# is it prime
	if n in primes:
			print(str(n) + " is prime")

	# is it even
	elif (n / 2) == 0:
		print(str(n) + " is even.")

	# is it odd
	elif (n / 2) != 0:
		print(str(n) + " is odd.")

	# don't forget to incriment X 
	# otherwise we'll get into an infinite loop
	n += 1
