# 题目描述
# 小易准备去拜访他的朋友，他的家在0点，但是他的朋友的家在x点(x > 0)，均在一条坐标轴上。小易每一次可以向前走1，2，3，4或者5步。问小易最少走多少次可以到达他的朋友的家。
# 输入描述:
# 一行包含一个数字x(1 <= x <= 1000000)，代表朋友家的位置。
# 输出描述:
# 一个整数，最少的步数。
# 示例1
# 输入
#
# 4
# 输出
#
# 1
# 示例2
# 输入
#
# 10
# 输出
#
# 2
remaining_steps = int(input())
res = 0
for step_unit in reversed(range(1, 6)):  # 迭代对应 5 4 3 2 1
    res += remaining_steps // step_unit  # 累加由商代表的所走的步数
    remaining_steps %= step_unit  # 将剩余的步数更新为余
    if remaining_steps == 0:
        break
print(res)
