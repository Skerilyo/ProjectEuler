def next_prime(n):
    prime = n + 1
    while (True):
        for x in range(2,prime-1):
            if prime % x == 0:
                prime += 1
                break
        return prime

def main():
    i = 600851475143;
    prime = 2

    while i > prime:
        if not i % prime:
            i /= prime
        else:
            prime = next_prime(prime)

    print(prime)

if __name__ == "__main__":
    main()