def main():
    start = 2520
    good = True

    a = list(range(1,21))
    for i in range(2, 21):
        for j in a:
            if j < i and i % j == 0:
                a.pop(a.index(j))

    while True:
        good = True
        for i in a:
            if start % i != 0:
                good = False
                break
        if good:
            break
        else:
            start += 1;
    print(start)
        

if __name__ == "__main__":
    main()