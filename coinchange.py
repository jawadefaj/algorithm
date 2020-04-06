

def CoinChange(d, N):
    NumberOfCoins = len(d)
    PosINF = 1000000000
    arr = [[0 for i in range(N + 1)] for j in range(NumberOfCoins)]
    for j in range(1, N + 1, 1):
        for i in range(NumberOfCoins):
            q = j - d[i]
            p = i - 1
            a = 0
            b = 0
            if p < 0 and q < 0:
                arr[i][j] = PosINF
            elif p < 0 or q < 0:
                if p < 0:
                    a = PosINF
                    b = arr[i][q]
                if q < 0:
                    b = PosINF
                    a = arr[p][j]
                arr[i][j] = min(a, b + 1)
            else:
                arr[i][j] = min(arr[p][j], arr[i][q] + 1)
    return arr[NumberOfCoins-1][N]


d = [1, 2, 3]
c = [3, 3, 1]
N = 4
print(CoinChange(d, N))