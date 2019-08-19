# 题目描述
# 小易有一些立方体，每个立方体的边长为1，他用这些立方体搭了一些塔。
# 现在小易定义：这些塔的不稳定值为它们之中最高的塔与最低的塔的高度差。
# 小易想让这些塔尽量稳定，所以他进行了如下操作：每次从某座塔上取下一块立方体，并把它放到另一座塔上。
# 注意，小易不会把立方体放到它原本的那座塔上，因为他认为这样毫无意义。
# 现在小易想要知道，他进行了不超过k次操作之后，不稳定值最小是多少。
# 输入描述:
# 第一行两个数n,k (1 <= n <= 100, 0 <= k <= 1000)表示塔的数量以及最多操作的次数。
# 第二行n个数，ai(1 <= ai <= 10**4)表示第i座塔的初始高度。
# 输出描述:
# 第一行两个数s, m，表示最小的不稳定值和操作次数(m <= k)
# 接下来m行，每行两个数x,y表示从第x座塔上取下一块立方体放到第y座塔上。
# 示例1
# 输入
#
# 3 2
# 5 8 5
# 输出
#
# 0 2
# 2 1
# 2 3
n, k = list(map(int, input().split()))
ai = list(map(int, input().split()))
# 找到数组中的最大值与最小值，最大值-1，最小值+1，循环直到最大值等于最小值或是循环次数超过k时停止
swap_count = 0
res = []
for i in range(k):
    max_ai = max(ai)
    min_ai = min(ai)
    if max_ai == min_ai:
        break
    # 用ai_index记录下标，储存在res中
    max_ai_index = ai.index(max_ai)
    min_ai_index = ai.index(min_ai)
    ai[max_ai_index] -= 1
    ai[min_ai_index] += 1
    swap_count += 1
    res.append(str(max_ai_index + 1) + ' ' + str(min_ai_index + 1))
print(str(max(ai) - min(ai)) + ' ' + str(swap_count))
for i in res:
    print(i)
