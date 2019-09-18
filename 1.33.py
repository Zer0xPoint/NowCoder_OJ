# 题目描述
# 有一只地鼠不小心跑进了一个m*n的矩形田地里，假设地鼠在这块田地的初始位置为（x,y），并且每次只能向相邻的上下左右四个方向移动一步，那么在最多移动K次的情况下，有多少条路径可以逃出这片田地（一旦出去田地的边界就不能再往回走）？
# 下面是样例示意图：
#
# 输入描述:
# 输入数据包括五个参数：m,n,x,y,K
# 其中m和n的范围均为是[1,10]，K的范围是[0,10]。
# 0<=x<m,0<=y<n。
# 输出描述:
# 输出成功逃跑的路径数量。
# 示例1
# 输入
#
# 2
# 3
# 0
# 1
# 2
# 输出
#
# 6


def rec_ham(i, j, left_steps):
    if i < 0 or j < 0 or i >= m or j >= n:  # 走出田地范围
        return 1
    if left_steps == 0:  # 步数耗尽 未走出田地
        return 0
    return rec_ham(i + 1, j, left_steps - 1) + \
           rec_ham(i - 1, j, left_steps - 1) + \
           rec_ham(i, j + 1, left_steps - 1) + \
           rec_ham(i, j - 1, left_steps - 1)


m, n, x, y, K = [int(input()) for _ in range(5)]

print(rec_ham(x, y, K))
# todo DP
