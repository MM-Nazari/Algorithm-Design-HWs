import heapq


def min_cost_to_connect_ropes(n, lengths):
    heapq.heapify(lengths)
    total_cost = 0

    while len(lengths) > 1:
        min1 = heapq.heappop(lengths)
        min2 = heapq.heappop(lengths)
        total_cost += min1 + min2
        heapq.heappush(lengths, min1 + min2)

    return total_cost


n = int(input())
lengths = list(map(int, input().split()))

print(min_cost_to_connect_ropes(n, lengths))
