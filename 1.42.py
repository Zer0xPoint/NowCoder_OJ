# 题目描述
# 幼儿园里有有M个小朋友在课件玩耍，每个人手中现有ni个玩具。为了公平起见，老师需要让每个小朋友手中有相同数量的玩具。假设老师每次只能从一个人手中拿走两个玩具并给另一个小朋友。求老师最少需要做多少次这样的玩具转移。如果不存在可行的方案则输出-1。
# 输入描述:
# 每个输入包含一个测试用例。每个测试用例的第一行包含一个整数M（1 <= M<= 100），接下来的一行包含M个整数ni（1 <= ni <= 100）。
# 输出描述:
# 输出一行表示最少需要移动多少次可以平分苹果，如果方案不存在则输出-1。
# 示例1
# 输入
#
# 4
# 7 15 9 5
# 输出
#
# 3
# 示例2
# 输入
#
# 2
# 3 6
# 输出
# 2
# -1

# 思路
# 找到list中比平均值小的那部分，与平均作差并累加
# 因为一次操作 = 高于平均的某个数 - 1 and 低于平均的某个数 + 1
# 故仅计算低于平均值的部分与平均值的差即可
M = int(input())
ni = list(map(int, input().split()))
sum_n = sum(ni)  # ni 中苹果的总数
avg_n = sum_n // M  # ni 中苹果的平均数
ni.sort()  # 使 ni 有序，便于之后只选择小于平均数的部分计算需要的移动次数

if sum_n % M is not 0:  # 总的苹果数若不能被平分 则不存在可以平分的方法
    print(-1)
else:
    res = 0
    i = 0
    while ni[i] < avg_n:  # 取比平均苹果数量小的部分，累加计算与平均值的差
        res += avg_n - ni[i]
        i += 1
    # 上面是按照移动一个苹果来计算的 因为一次只能拿两个苹果 故如果结果不能被2整除 则不存在可以平分的方法
    # 最后结果 res 也需要除以2
    print(res // 2) if res % 2 == 0 else print(-1)
