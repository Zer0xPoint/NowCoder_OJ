# 题目描述
# 你有3个需要完成的任务，完成这3个任务是需要付出代价的。
# 首先，你可以不花任何代价的完成一个任务；然后，在完成了第i个任务之后，你可以花费|Ai - Aj|的代价完成第j个任务。|y|代表x的绝对值。
# 计算出完成所有任务的最小代价。
# 输入描述:
# 一行3个整数A1,A2,A3，每个数字之间用一个空格分隔。所有数字都是整数，并且在[1,100]范围内。
# 输出描述:
# 一个整数，代表最小的代价。
# 示例1
# 输入
#
# 1 6 3
# 输出
#
# 5
# 示例2
# 输入
#
# 10 10 10
# 输出
#
# 0

a_list = list(map(int, input().split()))
avg = sum(a_list) / len(a_list)
minimum_difference = a_list[0]
a_closest_to_avg = a_list[0]
for i in range(len(a_list)):
    difference = abs(a_list[i] - avg)
    if difference < minimum_difference:
        minimum_difference = difference
        a_closest_to_avg = a_list[i]
res = 0
for a in a_list:
    res += abs(a - a_closest_to_avg)
print(res)
