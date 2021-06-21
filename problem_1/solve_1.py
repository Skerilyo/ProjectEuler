
def main():
    i = 0

    for j in range(0, 1000):
        if not j%3 or not j%5:
            i += j

    print(i) # 233168

if __name__ == "__main__":
    main()