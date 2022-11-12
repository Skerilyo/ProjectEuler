import math

def getDivisors(n) :
    divisors = []
    i = 1
    while i <= math.sqrt(n):
        if (n % i == 0) :
            if (n / i == i) :
                divisors.append(i)
            else :
                divisors.append(i)
                divisors.append(int(n/i))
        i = i + 1
    return len(divisors)
i = 1
j = 2
while j:
    i += j
    if getDivisors(i) >= 500:
        print("result:", i)
        break
    j += 1