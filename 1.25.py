# 题目描述
# 给定一个字符串来代表一个员工的考勤纪录，这个纪录仅包含以下两个字符：
# 'A' : Absent，缺勤
# 'P' : Present，到场
# 如果一个员工的考勤纪录中不超过两个'A'(缺勤),那么这个员工会被奖赏。
# 如果你作为一个员工，想在连续N天的考勤周期中获得奖赏，请问有多少种考勤的组合能够满足要求
# 输入描述:
# 考勤周期的天数N（正整数）
# 输出描述:
# 这N天里能获得奖赏的考勤组合数
# 示例1
# 输入
#
# 3
# 输出
#
# 7


def factorial(x):
    f = 1
    for i in range(1, x + 1):
        f *= i
    return f


n = int(input())
factorial_n = factorial(n)
# 组合问题 C(n,0) + C(n,1) + C(n,2)
res = 1 + factorial_n // factorial(n - 1) + factorial_n // (2 * factorial(n - 2))

print(res)
