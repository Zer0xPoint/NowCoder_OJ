# 题目描述
# 有一个X*Y的网格，小团要在此网格上从左上角到右下角，只能走格点且只能向右或向下走。请设计一个算法，计算小团有多少种走法。给定两个正整数int y,int y，请返回小团的走法数目。
#
# 输入描述:
# 输入包括一行，空格隔开的两个正整数x和y，取值范围[1,10]。
# 输出描述:
# 输出一行，表示走法的数目
# 示例1
# 输入
#
# 3 2
# 输出
#
# 10


def rec_step(x, y):
    if x == 0 or y == 0:
        if x == y:
            return 0
        else:
            return 1
    else:
        A = rec_step(x, y - 1)
        B = rec_step(x - 1, y)
        return A + B


def dp_step(x, y):
    # 动态规划 用arr储存计算过的距离
    arr = [[1 for _ in range(y + 1)] for _ in range(x + 1)]
    for i in range(1, x + 1):
        for j in range(1, y + 1):
            A = arr[i - 1][j]
            B = arr[i][j - 1]
            arr[i][j] = A + B
    return arr[- 1][- 1]


x, y = map(int, input().split())

print(rec_step(x, y))
print(dp_step(x, y))
