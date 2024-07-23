# def partition(arr, low, high):
#     i = low - 1
#     pivot = arr[high]
#
#     for j in range(low, high):
#         if arr[j] >= pivot:
#             i += 1
#             arr[i], arr[j] = arr[j], arr[i]
#
#     arr[i + 1], arr[high] = arr[high], arr[i + 1]
#     return i + 1
#
#
# def quicksort(arr, low, high):
#     if low < high:
#         pi = partition(arr, low, high)
#         quicksort(arr, low, pi - 1)
#         quicksort(arr, pi + 1, high)
#
#
# def main():
#     n = int(input())
#     arr = list(map(int, input().split()))
#
#     # اعمال الگوریتم مرتب‌سازی سریع
#     quicksort(arr, 0, n - 1)
#
#     # چاپ تعداد حرکت‌ها
#     print(n - 1)
#
#     # چاپ مراحل بینی
#     for i in range(n - 1):
#         print(" ".join(map(str, arr[n - i - 1:] + arr[:n - i - 1])))
#
#     # چاپ جایگشت‌های مرتب شده
#     print(" ".join(map(str, arr)))
#
#
# if __name__ == "__main__":
#     main()


# def count_sort(arr, exp):
#     n = len(arr)
#     output = [0] * n
#     count = [0] * 10
#
#     for i in range(n):
#         index = arr[i] // exp
#         count[index % 10] += 1
#
#     for i in range(1, 10):
#         count[i] += count[i - 1]
#
#     i = n - 1
#     while i >= 0:
#         index = arr[i] // exp
#         output[count[index % 10] - 1] = arr[i]
#         count[index % 10] -= 1
#         i -= 1
#
#     for i in range(n):
#         arr[i] = output[i]
#
#
# def radix_sort(arr):
#     max_num = max(arr)
#     exp = 1
#     while max_num // exp > 0:
#         count_sort(arr, exp)
#         exp *= 10
#
#
# def minimum_moves_to_sort(n, arr):
#     # Applying radix sort
#     radix_sort(arr)
#     # Counting the number of moves (swaps)
#     moves = 0
#     for i in range(n):
#         if arr[i] != i:
#             moves += 1
#             arr[i], arr[arr[i]] = arr[arr[i]], arr[i]  # Swap elements
#     return moves
#
#
# # Example usage
# n = 8
# arr = [7, 6, 5, 4, 3, 2, 1, 0]
# moves = minimum_moves_to_sort(n, arr)
# print(moves)
# print(*arr)

# def radix_sort_permutation(n, p):
#     # We can use a radix sort to convert the descending permutation `p` into ascending order
#     max_val = n - 1
#     num_digits = max_val.bit_length()  # Number of bits to represent the max value
#
#     # Perform radix sort on the permutation `p`
#     for digit in range(num_digits):
#         # Create buckets for each possible digit (0 or 1 in this case)
#         zero_bucket = []
#         one_bucket = []
#
#         # Distribute elements into buckets based on the current bit (from LSD to MSD)
#         for value in p:
#             if (value >> digit) & 1:
#                 one_bucket.append(value)
#             else:
#                 zero_bucket.append(value)
#
#         # Combine buckets to form the next version of `p`
#         p = zero_bucket + one_bucket
#
#     return p
#
#
# # Read input
# import sys
#
# input = sys.stdin.read
# data = input().split()
# n = int(data[0])
# p = list(map(int, data[1:]))
#
# # Perform radix sort on the descending permutation `p`
# sorted_permutation = radix_sort_permutation(n, p)
#
# # Calculate the number of moves needed (which is equal to the number of bit positions)
# num_moves = sorted_permutation[0].bit_length()
#
# # Print the number of moves
# print(num_moves)
#
# # Print the sequence of permutations after each move
# current_permutation = sorted_permutation
# for i in range(num_moves + 1):
#     print(" ".join(map(str, current_permutation)))
#     if i < num_moves:
#         current_permutation = radix_sort_permutation(n, current_permutation)


def count_sort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(n):
        arr[i] = output[i]


def radix_sort(arr):
    max_num = max(arr)
    exp = 1
    while max_num // exp > 0:
        count_sort(arr, exp)
        exp *= 10


def minimum_moves_to_sort(n, arr):
    moves = 0
    sorted_arr = sorted(arr)
    for i in range(n):
        if arr[i] != sorted_arr[i]:
            moves += 1
    return moves

# Example usage
n = int(input())
arr = list(map(int, input().split()))

moves = minimum_moves_to_sort(n, arr)
print(moves)

# Print the initial permutation
print(*arr)

# Perform the moves and print each resulting permutation
for _ in range(moves):
    i = 0
    while i < n - 1:
        if arr[i] > arr[i + 1]:
            j = i + 1
            while j < n and arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
                j += 1
            print(*arr)
            i = j
        else:
            i += 1
