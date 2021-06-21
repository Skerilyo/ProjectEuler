function main() {
    i = 0

    for (j = 0; j < 1000; j++) {
        if (j%3 == 0 || j%5 == 0)
            i += j
    }

    console.log(i)
}

main()