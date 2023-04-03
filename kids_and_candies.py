def gcd(a, b): return gcd(b, a%b) if b else a

def lcm(a, b): return a*b//gcd(a, b)

def candies_to_buy(n):
    result = 1
    for i in range(1, n+1):
        result = lcm(result, i)
        
    return result

print(candies_to_buy(10))


