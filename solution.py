# Rustom Ichhaporia

def solution(i):
    result = ''.join(str(x) for x in genPrimeString(500))
    print(result[i:i+5])
    
def genPrimeString(n):
    odds = range(3, n+1, 2)
    sieve = set(sum([list(range(q * q, n + 1, q + q)) for q in odds],[]))
    return [2] + [p for p in odds if p not in sieve]

solution(0)

# Credit to stack overflow for genPrimeString