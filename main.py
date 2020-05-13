import math
max_num = 2000000
prime_sum = 0
for numbers in range(2, max_num):
	if any(numbers % i == 0 for i in range(2, int(math.sqrt(numbers))+1)):
		pass
	else:
		prime_sum += numbers
solution = f"The sum of all primes below {max_num} is {prime_sum}"
print(solution)



		