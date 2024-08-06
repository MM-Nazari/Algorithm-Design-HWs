def quicksort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quicksort(left) + middle + quicksort(right)


def main():
    n = int(input())
    arr = list(map(int, input().split()))

    # اعمال الگوریتم مرتب‌سازی سریع با شرط خاص
    sorted_array = quicksort(arr)

    # چاپ نتیجه
    print(" ".join(map(str, sorted_array)))


if __name__ == "__main__":
    main()
