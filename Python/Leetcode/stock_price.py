# def stock(price):
#
#     n = len(price)
#     if len(price) <= 1:
#         return
#
#     i = 0
#
#     while i < (n-1):
#
#         print(f" First while {i} < {n-1}, {price[i+1]} <= {price[i]} ")
#         while i < (n-1) and price[i + 1] <= price[i]:
#             print(f" Comparing inside first while {price[i+1]} and {price[i]}")
#             i += 1
#
#         print(f" i value: {i} ")
#         if i == n-1:
#             break
#
#         buy = i
#         i += 1
#
#         print(f" Buy: {buy}")
#         print(f" Second While {i} < {n}")
#         while i < n and price[i] >= price[i-1]:
#             print(f" Comparing inside second while {price[i]} and {price[i-1]}")
#             i += 1
#
#         sell = i - 1
#         print(f" Sell: {sell}")
#
#         print(f" Buy on day {buy} and sell on day {sell}")





def stock(prices):

    n = len(prices)

    if n <= 1:
        return

    i = 0

    while i < n-1:

        while i < n - 1 and prices[i + 1] <= prices[i]:
            i += 1

        buy = i
        i += 1

        while i < n and prices[i] > prices[i - 1]:
            i += 1

        sell = i-1

        print(f" Buy on day {buy}, sell on day {sell}")



stock([100, 18, 260, 310, 40, 535, 695])
