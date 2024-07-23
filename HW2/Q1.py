def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)


input_string = input()
input_list = [int(x) for x in input_string.split()]
sorted_list = quick_sort(input_list)
print(" ".join(str(x) for x in sorted_list))
