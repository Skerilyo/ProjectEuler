function main() {
    i = 0
    prev = 0
    next = 1
    tmp = 0

    while (prev + next < 4000000) {
        tmp = next + prev
        if (tmp % 2 == 0)
            i += tmp
        prev = next
        next = tmp
    }

    console.log(i)
}

main()