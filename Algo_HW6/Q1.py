# import heapq
#
#
# def dijkstra(graph, start):
#     n = len(graph)
#     distances = [float('inf')] * n
#     distances[start] = 0
#     heap = [(0, start)]
#
#     while heap:
#         (dist, current) = heapq.heappop(heap)
#         if dist > distances[current]:
#             continue
#         for neighbor, weight in graph[current]:
#             new_dist = dist + weight
#             if new_dist < distances[neighbor]:
#                 distances[neighbor] = new_dist
#                 heapq.heappush(heap, (new_dist, neighbor))
#
#     return distances
#
#
# def min_walk_fatigue(n, L, paths):
#     graph = [[] for _ in range(n)]
#     for start, end in paths:
#         graph[start - 1].append((end - 1, end - start))
#
#     distances = []
#     for i in range(n):
#         distances.append(dijkstra(graph, i))
#
#     min_fatigue = float('inf')
#     for i in range(n):
#         fatigue = 0
#         for j in range(n):
#             fatigue += distances[i][j]
#         min_fatigue = min(min_fatigue, fatigue)
#
#     return min_fatigue
#
#
# # Example usage
# n, L = map(int, input().split())
# paths = [tuple(map(int, input().split())) for _ in range(n)]
# print(min_walk_fatigue(n, L, paths))

def minimum_walk(n, L, trips):
    trips.sort(key=lambda x: x[1])  # مرتب‌سازی مسافران بر اساس ایستگاه مقصد

    total_walk = 0  # مجموع پیاده روی شهروندان

    current_time = 1  # زمان فعلی

    for s, e in trips:
        walk = max(0, e - current_time)  # محاسبه زمان پیاده روی شهروند

        if walk > L:  # اگر زمان پیاده روی بیشتر از حداکثر ظرفیت قطار باشد
            total_walk += walk - L  # زمان اضافی پیاده روی را به مجموع پیاده روی اضافه می‌کنیم
            walk = L  # زمان پیاده روی را برابر حداکثر ظرفیت قطار می‌کنیم

        current_time = e + walk  # زمان فعلی را به زمان پایان پیاده روی این مسافر برابر می‌کنیم

    return total_walk


# خواندن ورودی
n, L = map(int, input().split())
trips = [tuple(map(int, input().split())) for _ in range(n)]

# محاسبه و چاپ کمینه‌ی مجموع پیاده روی
print(minimum_walk(n, L, trips))
