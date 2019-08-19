# 题目描述
# 为了找到自己满意的工作，牛牛收集了每种工作的难度和报酬。牛牛选工作的标准是在难度不超过自身能力值的情况下，牛牛选择报酬最高的工作。在牛牛选定了自己的工作后，牛牛的小伙伴们来找牛牛帮忙选工作，牛牛依然使用自己的标准来帮助小伙伴们。牛牛的小伙伴太多了，于是他只好把这个任务交给了你。
# 输入描述:
# 每个输入包含一个测试用例。
# 每个测试用例的第一行包含两个正整数，分别表示工作的数量N(N<=100000)和小伙伴的数量M(M<=100000)。
# 接下来的N行每行包含两个正整数，分别表示该项工作的难度Di(Di<=1000000000)和报酬Pi(Pi<=1000000000)。
# 接下来的一行包含M个正整数，分别表示M个小伙伴的能力值Ai(Ai<=1000000000)。
# 保证不存在两项工作的报酬相同。
# 输出描述:
# 对于每个小伙伴，在单独的一行输出一个正整数表示他能得到的最高报酬。一个工作可以被多个人选择。
# 示例1
# 输入
#
# 3 3
# 1 100
# 10 1000
# 1000000000 1001
# 9 10 1000000000
# 输出
#
# 100
# 1000
# 1001

# n, m = list(map(int, input().split()))
# works = []
# for i in range(n):
#     works.append(list(map(int, input().split())))
#
# friends_ai = list(map(int, input().split()))
#
# best_payment = []
# for i in range(m):
#     personal_best_payment = 0
#     for j in range(n):
#         if friends_ai[i] > works[j][0]:
#             if personal_best_payment < works[j][1]:
#                 personal_best_payment = works[j][1]
#     best_payment.append(personal_best_payment)
# for i in best_payment:
#     print(i)
# print(best_payment)

import sys
import bisect

tasks = {}
lines = sys.stdin.readlines()
for line in lines[1:-1]:  # 数据有空行 故第一行输入可忽略
    if not line.strip().split():
        continue
    require_skill, payment = map(int, line.strip().split())
    tasks[require_skill] = max(tasks.get(require_skill, 0), payment)
sorted_require_skill = sorted(tasks.keys())  # 按照require_skill排序

for i in range(1, len(sorted_require_skill)):
    if tasks[sorted_require_skill[i]] < tasks[sorted_require_skill[i - 1]]:  # 使require_skill越高payment越多
        tasks[sorted_require_skill[i]] = tasks[sorted_require_skill[i - 1]]  # 高payment覆盖低payment

skills = map(int, lines[-1].strip().split())
for skill in skills:
    if skill in tasks:
        print(tasks[skill])  # 找到符合skill的task输出payment
    else:
        index = bisect.bisect(sorted_require_skill, skill)  # index为skill在sorted_require_skill之中的位置
        print(tasks[sorted_require_skill[index - 1]]) if index != 0 else print(0)  # 若index不为0则有相对应的task
