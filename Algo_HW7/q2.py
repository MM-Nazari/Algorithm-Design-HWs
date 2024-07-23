# import heapq
#
#
# def minimum_spanning_tree_weight(n, edges):
#     # مجموعه‌ای برای رئوس درخت پوشا
#     tree_set = set()
#     # لیستی برای یال‌های درخت
#     tree_edges = []
#
#     # انتخاب یک راس به عنوان شروع الگوریتم
#     start_vertex = edges[0][0]
#     tree_set.add(start_vertex)
#
#     # اضافه کردن یال‌های مرتبط با راس شروع به لیست یال‌های درخت
#     for edge in edges:
#         if edge[0] == start_vertex:
#             heapq.heappush(tree_edges, edge)
#
#     total_weight = 0
#
#     while len(tree_set) < n:
#         # یافتن یال با کمترین وزن متصل به درخت
#         min_edge = heapq.heappop(tree_edges)
#         # استخراج راس‌های یال
#         u, v, weight = min_edge
#
#         # اضافه کردن راس متصل به درخت
#         if v not in tree_set:
#             tree_set.add(v)
#             total_weight += weight
#             # اضافه کردن یال‌های مرتبط با راس جدید به لیست یال‌های درخت
#             for edge in edges:
#                 if edge[0] == v and edge[1] not in tree_set:
#                     heapq.heappush(tree_edges, edge)
#         elif u not in tree_set:
#             tree_set.add(u)
#             total_weight += weight
#             for edge in edges:
#                 if edge[0] == u and edge[1] not in tree_set:
#                     heapq.heappush(tree_edges, edge)
#
#     return total_weight
#
#
# # خواندن ورودی
# n, m = map(int, input().split())
# edges = []
# for _ in range(m):
#     A, B, C = map(int, input().split())
#     edges.append((A, B, C))
#
# # محاسبه و چاپ وزن درخت پوشای کمینه
# print(minimum_spanning_tree_weight(n, edges))


def minimum_spanning_tree_weight(n, edges):
    # تابع برای پیدا کردن پدر هر راس با استفاده از روش جستجوی پدر (پدر یک راس، راسی است که به آن وصل شده است)
    def find(parent, vertex):
        if parent[vertex] == vertex:
            return vertex
        return find(parent, parent[vertex])

    # تابع برای ادغام دو درخت با استفاده از روش جستجوی پدر
    def union(parent, rank, x, y):
        x_root = find(parent, x)
        y_root = find(parent, y)

        # ادغام دو درخت بر اساس رتبه (تعداد راس‌ها)
        if rank[x_root] < rank[y_root]:
            parent[x_root] = y_root
        elif rank[x_root] > rank[y_root]:
            parent[y_root] = x_root
        else:
            parent[y_root] = x_root
            rank[x_root] += 1

    # مرتب‌سازی یال‌ها بر اساس وزن آن‌ها
    edges.sort(key=lambda x: x[2])

    parent = [i for i in range(n + 1)]  # پدر هر راس را خود راس فرض می‌کنیم
    rank = [0] * (n + 1)  # رتبه هر راس را صفر می‌گذاریم

    total_weight = 0
    for u, v, weight in edges:
        # اگر دو راس متصل توسط این یال در یک درخت نباشند، آن را به درخت اضافه کرده و وزنش را به وزن درخت اضافه می‌کنیم
        if find(parent, u) != find(parent, v):
            total_weight += weight
            union(parent, rank, u, v)

    return total_weight


# خواندن ورودی
n, m = map(int, input().split())
edges = []
for _ in range(m):
    A, B, C = map(int, input().split())
    edges.append((A, B, C))

# محاسبه و چاپ وزن درخت پوشای کمینه
print(minimum_spanning_tree_weight(n, edges))
