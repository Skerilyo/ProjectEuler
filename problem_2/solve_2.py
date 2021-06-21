
def main():
    i = 0
    prev = 0
    next = 1

    while prev + next < 4000000: #4 millions
        tmp = next + prev
        if tmp % 2 == 0:
            i += tmp
        prev = next
        next = tmp

    print(i)

if __name__ == "__main__":
    main()