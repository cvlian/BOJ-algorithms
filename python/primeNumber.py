"""
    Prime Number
"""

import random

MAX = 2**18
m = [0, 1] + [0]*MAX
soe = [0, 0] + [1]*MAX

def cal_mu():
    for i in range(1, MAX+1):
        for j in range(2*i, MAX+1, i):
            m[j] -= m[i]

def cal_eratos():
    global soe, MAX

    for i in range(2, MAX) :
        if soe[i] == 1 :
            for j in range(i*i, MAX, i) :
                soe[j] = 0

def gcd(a, b):

    while b != 0 :
        r = a%b
        a = b
        b = r
    
    return a

# Mobius function (in Inclusion–Exclusion Principle)
def mobius(n):
    global m

    i = 1; s = 0
    while i*i <= n :
        s += m[i]*(n//(i**2))
        i += 1
    
    return s

def powmod(x, y, m):
    x %= m; r = 1

    while y > 0:
        if y & 1 != 0:
            r = (r*x)%m
        
        x = (x**2)%m
        y //= 2

    return r

# True for prime, False for composite
def miller_rabin(n, a):
    d = n - 1; r = 0

    while d%2 == 0 :
        r += 1
        d //= 2
    
    p = powmod(a, d, n)

    if p == n - 1 or p == 1:
        return True

    for _ in range(r-1):
        p = (p**2)%n

        if p == n - 1:
            return True

    return False

def is_prime(n):
    global soe, MAX

    if n < MAX:
        return soe[n] == 1

    if n%2 == 0 :
        return False

    for a in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]:
        if not miller_rabin(n, a) :
            return False

    return True

def rho_f(x, c, m):
    return ((x**2)%m + c)%m

def pollard_rho(n, x=2):

    if n == 1:
        return 1

    if n%2 == 0:
        return 2

    if is_prime(n):
        return n

    d = 1
    y = x
    c = random.randint(1, 10)

    for c in range(1, 10):
        d = 1
        x = 2; y = x

        while d == 1 :
            if d == n :
                break

            x = rho_f(x, c, n)
            y = rho_f(y, c, n)
            y = rho_f(y, c, n)
            d = gcd(abs(x-y), n)

        if d != n :
            break
    
    return d if is_prime(d) else pollard_rho(d)

def factorize(n):
    r = []

    while n > 1 :
        d = pollard_rho(n)
        r.append(d)
        n //= d
    
    return sorted(r)