def main():
    sum = 0
    square_sum = 0
    for i in range(1, 101):
        sum += i
        square_sum += i**2
    sum_squared = sum ** 2
    print(sum_squared - square_sum)

if __name__ == "__main__":
    main()