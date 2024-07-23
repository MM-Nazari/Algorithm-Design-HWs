def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = key

# Reading input
n = int(input())
arr = list(map(int, input().split()))

# Calling insertion sort function
insertion_sort(arr)

# Printing sorted array
print(*arr)
