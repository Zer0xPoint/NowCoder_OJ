# 题目描述
# 给定一个长度为偶数的数组arr，将该数组中的数字两两配对并求和，在这些和中选出最大和最小值，请问该如何两两配对，才能让最大值和最小值的差值最小？
# 输入描述:
# 一共2行输入。
# 第一行为一个整数n，2<=n<=10000, 第二行为n个数，组成目标数组，每个数大于等于2，小于等于100。
# 输出描述:
# 输出最小的差值。
# 示例1
# 输入
#
# 4
# 2 6 4 3
# 输出
#
# 1
# 示例2
# 输入
#
# 6
# 11 4 3 5 7 1
# 输出
#
# 3
n = int(input())
arr = list(map(int, input().split()))
arr.sort()

sum_list = []

for i in range(n // 2):
    sum_list.append(arr[i] + arr[-i - 1])
res = max(sum_list) - min(sum_list)
print(res)
