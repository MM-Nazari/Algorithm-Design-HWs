# def count_edges_not_in_shortest_paths(n, edges):
#     # ایجاد یک دیکشنری برای نگهداری تعداد یال‌هایی که در کوتاه‌ترین مسیر بین دو راس حضور ندارند
#     edge_counts = {}
#
#     # ایجاد ماتریس فاصله برای ذخیره کوتاه‌ترین فاصله بین هر جفت راس
#     distances = [[float('inf')] * n for _ in range(n)]
#
#     # پر کردن ماتریس فاصله براساس یال‌ها
#     for u, v, w in edges:
#         distances[u - 1][v - 1] = w
#         distances[v - 1][u - 1] = w
#
#     # الگوریتم فلوید وارشال برای محاسبه کوتاه‌ترین مسیرها
#     for k in range(n):
#         for i in range(n):
#             for j in range(n):
#                 distances[i][j] = min(distances[i][j], distances[i][k] + distances[k][j])
#
#     # بررسی هر یال
#     for u, v, w in edges:
#         count = 0
#         # بررسی تمام جفت‌های راس‌ها
#         for i in range(n):
#             for j in range(n):
#                 # اگر یال در کوتاه‌ترین مسیر بین دو راس حضور نداشته باشد
#                 if distances[i][j] == distances[i][u - 1] + w + distances[v - 1][j]:
#                     count += 1
#         edge_counts[(u, v)] = count
#
#     # شمارش یال‌هایی که در هیچ کوتاه‌ترین مسیری حضور ندارند
#     result = sum(1 for count in edge_counts.values() if count == n - 2)
#     return result
#
#
# # خواندن ورودی
# n, m = map(int, input().split())
# edges = []
# for _ in range(m):
#     A, B, C = map(int, input().split())
#     edges.append((A, B, C))
#
# # محاسبه و چاپ تعداد یال‌هایی که در هیچ کوتاه‌ترین مسیری حضور ندارند
# print(count_edges_not_in_shortest_paths(n, edges))

def count_edges_not_in_shortest_paths(n, edges):
    # ایجاد یک دیکشنری برای نگهداری تعداد یال‌هایی که در کوتاه‌ترین مسیر بین دو راس حضور ندارند
    edge_counts = {}

    # ایجاد ماتریس فاصله برای ذخیره کوتاه‌ترین فاصله بین هر جفت راس
    distances = [[float('inf')] * n for _ in range(n)]

    # پر کردن ماتریس فاصله براساس یال‌ها
    for u, v, w in edges:
        distances[u - 1][v - 1] = w
        distances[v - 1][u - 1] = w

    # چاپ ماتریس فاصله برای بررسی درستی محاسبات
    print("Initial Distance Matrix:")
    for row in distances:
        print(row)
    print()

    # الگوریتم فلوید وارشال برای محاسبه کوتاه‌ترین مسیرها
    for k in range(n):
        for i in range(n):
            for j in range(n):
                distances[i][j] = min(distances[i][j], distances[i][k] + distances[k][j])

    # چاپ ماتریس فاصله بعد از اعمال الگوریتم فلوید وارشال
    print("Distance Matrix After Floyd-Warshall Algorithm:")
    for row in distances:
        print(row)
    print()

    # بررسی هر یال
    for u, v, w in edges:
        count = 0
        # بررسی تمام جفت‌های راس‌ها
        for i in range(n):
            for j in range(n):
                # اگر یال در کوتاه‌ترین مسیر بین دو راس حضور نداشته باشد
                if distances[i][j] == distances[i][u - 1] + w + distances[v - 1][j]:
                    count += 1
        edge_counts[(u, v)] = count

    # شمارش یال‌هایی که در هیچ کوتاه‌ترین مسیری حضور ندارند
    result = sum(1 for count in edge_counts.values() if count == n - 2)
    return result


# خواندن ورودی
n, m = map(int, input().split())
edges = []
for _ in range(m):
    A, B, C = map(int, input().split())
    edges.append((A, B, C))

# محاسبه و چاپ تعداد یال‌هایی که در هیچ کوتاه‌ترین مسیری حضور ندارند
print(count_edges_not_in_shortest_paths(n, edges))
