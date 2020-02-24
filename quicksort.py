

arr = [10, 12, 2, 1, -1, 5, -6, 8, 8, 2]

def partition(a, p, q):
    x = a[q]
    j = p - 1
    for i in range(p, q, 1):
        if a[i] <= x:
            j = j + 1
            temp = a[j]
            a[j] = a[i]
            a[i] = temp
    temp = a[j + 1]
    a[j + 1] = a[q]
    a[q] = temp
    return j + 1




def quicksort(a, p, q):
    if p < q:
        y = partition(a, p, q)
        quicksort(a, p, y - 1)
        quicksort(a, y + 1, q)
    else:
        return 0
    return a
        


        

print(quicksort(arr, 0, len(arr) - 1))
