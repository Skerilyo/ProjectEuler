def main():
    maxi = 0
    for a in range(100,1000):
        for b in range(100, 1000):
            if a * b == (int)(((str)(a * b))[::-1]) and a*b > maxi:
                maxi = a*b
    print(maxi)


if __name__ == "__main__":
    main()