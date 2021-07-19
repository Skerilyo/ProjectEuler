S = [1,2,5,10,20,50,100,200]

def calc(N, m):
    global S
    if m <= 0 or N < 0:
        return 0
    if N == 0:
        return 1
    return calc(N - S[m - 1], m) + calc(N, m - 1)

if __name__ == "__main__":
    print(calc(200, len(S)))

