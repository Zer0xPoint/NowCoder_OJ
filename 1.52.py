# 题目描述
# 给定一个正整数数组，它的第 i 个元素是比特币第 i 天的价格。
# 如果你最多只允许完成一笔交易（即买入和卖出一次），设计一个算法来计算你所能获取的最大利润。
# 注意你不能在买入比特币前卖出。
# 输入描述:
# 正整数数组，为以空格分隔的n个正整数
# 输出描述:
# 最大利润
# 示例1
# 输入
#
# 7 1 5 3 6 4
# 输出
#
# 5

n_list = list(map(int, input().split()))
n = max(n_list)
min_n = n
max_res = 0
for n in n_list:
    max_res = max(n - min_n, max_res)
    min_n = min(n, min_n)
print(max_res)
