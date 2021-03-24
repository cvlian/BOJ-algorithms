# Mobius function (in Inclusion–Exclusion Principle)

INF = 200001
m = [0, 1] + [0]*INF

for i in range(1, INF+1):
    for j in range(2*i, INF+1, i):
        m[j] -= m[i]

def mobius(n):
    global m

    i = 1; s = 0
    while i*i <= n :
        s += m[i]*(n//(i**2))
        i += 1
    
    return s