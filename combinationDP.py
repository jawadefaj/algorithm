

def combination(n, k):
    if k == 0 or k == n:
        return 1
    else:
        return combination(n - 1, k - 1) + combination(n - 1, k)

#print(combination(3, 1))

def combinationDP(n, k):
    arr = [[0 for i in range(n + 1)] for j in range(k + 1)]
    for i in range(n + 1):
        for j in range(k + 1):
            if j == 0 or j == i:
                arr[j][i] = 1
            elif j > i:
                arr[j][i] = 0
            else:
                arr[j][i] = arr[j - 1][i - 1] + arr[j][i - 1]
    return arr



print(combinationDP(4, 3))