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
    i = 1
    prime = 2
    while(i < 10001):
        i += 1
        print(i)
        prime = next_prime(prime)
        print(prime)
    print(prime)

if __name__ == "__main__":
    main()