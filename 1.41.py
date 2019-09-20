# 题目描述
# 已知一个正整数n，(3 <= n <= 15)，将所有n的乘方幂以及所有n的乘方幂（有限个且互不相等）之和组成一个递增序列。例如，当n为4时，该序列为：
# 1, 4, 5, 16, 17, 20, 21……
# (4^0, 4^1, 4^0+4^1, 4^2, 4^0+4^2, 4^1+4^2, 4^0+4^1+4^2……)
# 请求出该序列的第K项(10进制)。
# 输入描述:
# 输入只有1行，为2个正整数，两数之间用一个空格隔开：
# n K
# (n, K的含义与上述描述一致, 且3<=n<=15, 10<=K<=1000)。
# 输出描述:
# 输出为计算结果，为一个正整数（注意在所有测试数据中，结果均不会超过2.1*10^9）。整数前不要有空格或其他任何符号。
# 示例1
# 输入
#
# 3 100
# 输出
#
# 981
import math


def factorial(x):
    f = 1
    for i in range(1, x + 1):
        f *= i
    return f


# n, K = map(int, input().split())
n = 3
K = 12
# fib_list = [1, 1]
# for i in range(K):
#     if i > 1:
#         fib_list.append(fib_list[i - 1] + fib_list[i - 2])
#
# print(fib_list)

exponential = int(math.sqrt(K))
index = K - 2 ** exponential + 1
num_of_ex_sum_numbers_count = 1
# n_factorial = factorial(exponential)
# m_factorial = factorial(num_of_ex_sum_numbers_count)

# while index > factorial(exponential) / (
#         factorial(num_of_ex_sum_numbers_count - 1) * factorial(exponential - (num_of_ex_sum_numbers_count - 1))):
#     num_of_ex_sum_numbers_count += 1

# 思路
# 先找到exponential代表当前最大的指数
# index代表在当前最大指数的范围（C（n m）n是最大指数）内是第几个数
# todo 找到当前index上的和由几个元素组成 并求出这几个特定元素
print(factorial(3) // (factorial(2) * factorial(3 - 2)))

print(exponential)
print(index)
print(num_of_ex_sum_numbers_count)
