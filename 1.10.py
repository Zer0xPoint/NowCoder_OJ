# 题目描述
# 牛牛准备参加学校组织的春游, 出发前牛牛准备往背包里装入一些零食, 牛牛的背包容量为w。
# 牛牛家里一共有n袋零食, 第i袋零食体积为v[i]。
# 牛牛想知道在总体积不超过背包容量的情况下,他一共有多少种零食放法(总体积为0也算一种放法)。
# 输入描述:
# 输入包括两行
# 第一行为两个正整数n和w(1 <= n <= 30, 1 <= w <= 2 * 10^9),表示零食的数量和背包的容量。
# 第二行n个正整数v[i](0 <= v[i] <= 10^9),表示每袋零食的体积。
# 输出描述:;
# 示例1
# 输入
#
# 3 10
# 1 2 4
# 输出
#
# 8
# 说明
#
# 三种零食总体积小于10,于是每种零食有放入和不放入两种情况，一共有2*2*2 = 8种情况。
# todo

n, w = list(map(int, input().split()))
v_list = list(map(int, input().split()))
v_list.sort()
v_sum_list = [v_list[0] for _ in range(n)]  # 累加数组 每一位分别对应sum(v_list[:i - 1])
for i in range(len(v_list)):
    if i > 0:
        v_sum_list[i] = v_sum_list[i - 1] + v_list[i]


def rec_count_solutions(i, last_cap):
    if v_sum_list[i] <= last_cap:  # 剩下的容量大于剩下元素的总和
        return 2 ** (i + 1)
    if last_cap < 0:  # 剩下的容量为负数
        return 0
    if i == 0:  # 剩下一个元素
        if v_list[i] <= last_cap:  # 可以选择放或者不放
            return 2
        else:  # 只能选择不放
            return 1
    return rec_count_solutions(i - 1, last_cap - v_list[i]) + rec_count_solutions(i - 1, last_cap)


if v_sum_list[-1] <= w:
    print(2 ** n)
else:
    print(rec_count_solutions(n - 1, w))
