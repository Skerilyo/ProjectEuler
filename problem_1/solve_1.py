
def main():
    i = 0

    for j in range(0, 1000):
        if j%3 == 0 or j%5 == 0:
            i += j

    print(i) # 233168

if __name__ == "__main__":
    main()