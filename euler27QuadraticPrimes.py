#Euler discovered the remarkable quadratic formula:

#n2+n+41
#It turns out that the formula will produce 40 primes for the consecutive integer values 0≤n≤39. However, when n=40,402+40+41=40(40+1)+41 is divisible by 41, and certainly when n=41,412+41+41 is clearly divisible by 41.

#The incredible formula n2−79n+1601 was discovered, which produces 80 primes for the consecutive values 0≤n≤79. The product of the coefficients, −79 and 1601, is −126479.

#Considering quadratics of the form:

#n2+an+b, where |a|<1000 and |b|≤1000

#where |n| is the modulus/absolute value of n
#e.g. |11|=11 and |−4|=4
#Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n=0.


def IsPrime(n):
    if n < 1:
        result = False
        return
    result = True
    for i in range(2, int(n**0.5) +1):
        if n % i == 0:
            result = False
            break
    return result

def QuadraticPrimes(a, b):
    new_prime_nos = 0
    first_final = 0
    second_final = 0
    for first in range(-abs(a)+1, abs(a)):
        for second in range(-abs(b), abs(b)+1):
            no_of_primes = 0
            n = 1
            while n - no_of_primes == 1:
                prime_number = n**2 + first*n + second
                if IsPrime(prime_number):
                    n += 1
                    no_of_primes += 1
                else:
                    break
            if new_prime_nos < no_of_primes:
                new_prime_nos = no_of_primes
                first_final = first
                second_final = second
    return first_final*second_final

final = QuadraticPrimes(1000, 1000)
print(final)

