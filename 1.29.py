# 题目描述
# 假设你正在玩跳格子（所有格子排成一个纵列）游戏。需要 跳完n 个格子你才能抵达终点。
# 每次你可以跳 1 或 2 个格子。你有多少种不同的方法可以到达终点呢？
# 注意：给定 n 是一个正整数。
# 输入描述:
# 格子数n
# 输出描述:
# 跳完n个格子到达终点的方法
# 示例1
# 输入
#
# 2
# 输出
#
# 2

# 阶乘
def factorial(x):
    f = 1
    for i in range(1, x + 1):
        f *= i
    return f


elements = int(input())
quotient = elements // 2
n = elements - quotient
res = 0
for n in range(n, elements):
    m = elements - n
    res += factorial(n) // (factorial(m) * factorial(n - m))
print(res + 1)
