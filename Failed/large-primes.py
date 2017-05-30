#from gmpy2 import *
from Crypto.Util.number import *

#http://stackoverflow.com/questions/14939953/sum-the-digits-of-a-number-python
def sum_digits3(n):
   r = 0
   while n:
       r, n = r + n % 10, n // 10
   return r

primes = 0
count = pow(10,20)
end = pow(10,400)
while count <= end:
	sum = sum_digits3(count)
	if isPrime(sum):
		primes += 1
		#print "found", sum
	count += 1

print primes