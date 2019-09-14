# 题目描述
# 现给定n个整数，并定义一个非负整数m，且令f(m) = (m%a1)+(m%a2)+...+(m%an)。
# 此处的X % Y的结果为X除以Y的余数。
# 现请你找出一个m，求出f(m)的最大值。
#
# 输入描述:
# 输入包含两行，第一行为一正整数n，(1<n<=3000)
# 第二行为n个整数a1,a2,...,an ，其中(2<=ai<=10^5)
# 输出描述:
# 输出仅包含一行，输出f(m)的最大值
# 示例1
# 输入
#
# 3
# 3 4 6
# 输出
#
# 10
# 说明
#
# 就样例而言，当m取11时可取得最大值。
# m 与 x 最大的余数为 x - 1，则 m + 1 为 x 的整数倍
# 故当 m + 1 为所有数的整数倍时，m 能够与所有数取到最大的余数
n = int(input())
a_list = list(map(int, input().split()))
print(sum(a_list) - n)
# todo 为什么所有数的和就是公倍数？
