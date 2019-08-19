# 题目描述
# 输入一个整形数组（可能有正数和负数），求数组中连续子数组（最少有一个元素）的最大和。要求时间复杂度为O(n)。
# 输入描述:
# 【重要】第一行为数组的长度N（N>=1）
#
# 接下来N行，每行一个数，代表数组的N个元素
# 输出描述:
# 最大和的结果
# 示例1
# 输入
#
# 8
# 1
# -2
# 3
# 10
# -4
# 7
# 2
# -5
# 输出
#
# 18
# 说明
#
# 最大子数组为 3, 10, -4, 7, 2
import sys

i = int(input())

n_list = [int(input()) for i in range(i)]
for i in range(1, len(n_list)):
    if n_list[i - 1] > 0:
        n_list[i] += n_list[i - 1]

print(max(n_list))
