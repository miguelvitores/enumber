import math
import numpy
from fractions import Fraction
from decimal import Decimal

max_n_digs = 12000
max_cons_zeros_allowed = 10
num_primes_cons = 10
n_iter = 2000
primes = (
    2,
    3,
    5,
    7,
)
e_digs = numpy.zeros((1, max_n_digs))
solution = numpy.zeros((1, num_primes_cons))
iteration = 0
e = 0
found = False
max_cons_primes_found = 0

while iteration < n_iter:
    e += Fraction(1, math.factorial(iteration))
    iteration += 1
print("e done!")

prev_num = 0
zeros = 0
n_digs = max_n_digs
for j in range(max_n_digs):
    factor = Fraction(10 ** j, 1)
    num = math.floor(e * factor)
    dig = - (prev_num * 10 - num)
    if dig == 0:
        zeros += 1
        if zeros == max_cons_zeros_allowed:
            n_digs = j - max_cons_zeros_allowed
            break
    else:
        zeros = 0
    e_digs[:, j] = dig
    prev_num = num
print("separate digits done!")

n_pr = 0
for i in range(n_digs):
    if e_digs[:, i] in primes:
        n_pr += 1
        max_cons_primes_found = max(max_cons_primes_found, n_pr)
    else:
        n_pr = 0
    if n_pr == num_primes_cons:
        solution = e_digs[:, i-num_primes_cons: i]
        found = True
        break
print("Calcs done!")
if found:
    print("Solution reached! {0} prime numbers consecutives in number e. Decimals: {1}".format(num_primes_cons,
                                                                                               solution))
else:
    print("Solution not reached. Max consecutive primes found: {0}".format(max_cons_primes_found))
