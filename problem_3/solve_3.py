def next_prime(n):
    prime = n + 1
    good = True
    while (True):
        good = True
        for x in range(2,(prime//2) + 1):
            if prime % x == 0:
                good = False
                prime += 1
                break
        if (good):
            return prime

def main():
    i = 600851475143;
    prime = 2

    while i > prime:
        if i % prime == 0:
            i /= prime
        else:
            prime = next_prime(prime)

    print(prime)

if __name__ == "__main__":
    main()