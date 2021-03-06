function next_prime() {
    prime = n + 1
    good = true
    while (true) {
        good = true
        for (x = 2; x <= prime / 2; x++) {
            if (prime % x == 0) {
                good = false
                prime += 1
                break
            }
        }
        if (good)
            return prime
    }
}

function main() {
    i = 600851475143;
    prime = 2

    while (i > prime) {
        if (i % prime == 0) { 
            i /= prime
        } else {
            prime = next_prime(prime)       
        }
    }
    console.log(prime)
}

main()