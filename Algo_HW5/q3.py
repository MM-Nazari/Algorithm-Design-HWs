def count_ways(n):
    # تعداد راه های پوشاندن جدول 3xn را باز می گرداند
    if n % 2 != 0:
        return 0  # اگر n فرد باشد، نمی‌توان جدول را کامل پوشاند

    dp = [0] * (n + 1)
    dp[0] = 1
    dp[2] = 3

    for i in range(4, n + 1, 2):
        dp[i] = 4 * dp[i - 2] - dp[i - 4]

    return dp[n]


# ورودی
n = int(input().strip())

# محاسبه و خروجی
print(2 * count_ways(n))
