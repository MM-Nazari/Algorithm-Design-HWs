# import heapq
# import sys
#
# input = sys.stdin.read
#
#
# def shortest_path():
#     # خواندن ورودی
#     data = input().split()
#     n = int(data[0])
#     m = int(data[1])
#
#     # ساختن گراف
#     graph = [[] for _ in range(n + 1)]
#     index = 2
#     for _ in range(m):
#         u = int(data[index])
#         v = int(data[index + 1])
#         w = int(data[index + 2])
#         graph[u].append((v, w))
#         graph[v].append((u, w))
#         index += 3
#
#     # پیاده‌سازی الگوریتم دایجسترا
#     def dijkstra(start):
#         distances = [float('inf')] * (n + 1)
#         distances[start] = 0
#         priority_queue = [(0, start)]
#         while priority_queue:
#             current_distance, current_vertex = heapq.heappop(priority_queue)
#             if current_distance > distances[current_vertex]:
#                 continue
#             for neighbor, weight in graph[current_vertex]:
#                 distance = current_distance + weight
#                 if distance < distances[neighbor]:
#                     distances[neighbor] = distance
#                     heapq.heappush(priority_queue, (distance, neighbor))
#         return distances
#
#     # پیدا کردن کوتاه‌ترین مسیر از راس ۱
#     distances = dijkstra(1)
#
#     # چاپ خروجی
#     for i in range(1, n + 1):
#         if distances[i] == float('inf'):
#             print(-1)
#         else:
#             print(distances[i])
#
#
# # فراخوانی تابع
# shortest_path()

import heapq

def shortest_path():
    # خواندن ورودی
    n, m = map(int, input().split())

    # ساختن گراف
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v, w = map(int, input().split())
        graph[u].append((v, w))
        graph[v].append((u, w))

    # پیاده‌سازی الگوریتم دایجسترا
    def dijkstra(start):
        distances = [float('inf')] * (n + 1)
        distances[start] = 0
        priority_queue = [(0, start)]
        while priority_queue:
            current_distance, current_vertex = heapq.heappop(priority_queue)
            if current_distance > distances[current_vertex]:
                continue
            for neighbor, weight in graph[current_vertex]:
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))
        return distances

    # پیدا کردن کوتاه‌ترین مسیر از راس ۱
    distances = dijkstra(1)

    # چاپ خروجی
    for i in range(1, n + 1):
        if distances[i] == float('inf'):
            print(-1)
        else:
            print(distances[i])

# فراخوانی تابع
shortest_path()
