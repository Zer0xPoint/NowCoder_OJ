# 题目描述
# 小明在越南旅游，参加了当地的娱乐活动。小明运气很好，拿到了大奖， 到了最后的拿奖金环节。小明发现桌子上放着一列红包，每个红包上写着奖金数额。
# 现在主持人给要求小明在这一列红包之间“切”2刀，将这一列红包“切”成3组，并且第一组的奖金之和等于最后一组奖金和（允许任意一组的红包集合是空）。
# 最终第一组红包的奖金之和就是小明能拿到的总奖金。小明想知道最多能拿到的奖金是多少，你能帮他算算吗。
# 举例解释：桌子上放了红包  1, 2, 3, 4, 7, 10。小明在“4,7”之间、“7,10” 之间各切一刀，将红包分成3组 [1, 2, 3, 4]   [7]   [10]
# 其中第一组奖金之和=第三组奖金之和=10，所以小明可以拿到10越南盾。
# 输入描述:
# 第一行包含一个正整数n，(1<=n<= 200 000)，表示有多少个红包。
#
# 第二行包含n个正整数d[i]，表示每个红包包含的奖金数额。其中1<= d[i] <= 1000 000 000
# 输出描述:
# 小明可以拿到的总奖金
# 示例1
# 输入
#
# 5
# 1 3 1 1 4
# 输出
#
# 5
# 说明
#
# [1,3,1]  [ ]   [1,4] ，其中第一组奖金和是5，等于第三组奖金和。所以小明可以拿到5越南盾

n = int(input())
di = list(map(int, input().split()))
# di_rev = []
# for i in reversed(di):
#     di_rev.append(i)
# sum_di = [di[0]]
# sum_di_rev = [di_rev[0]]
# for i in range(1, n):
#     sum_di.append(sum_di[i - 1] + di[i])
#     sum_di_rev.append(sum_di_rev[i - 1] + di_rev[i])
# res = 0
# for i in range(n):
#     i_rev = sum_di_rev.index(sum_di[i]) if sum_di[i] in sum_di_rev else -1
#     if i + i_rev < n and i_rev != -1:
#         res = max(res, sum_di[i])
# print(res)
# 复杂度n*log n，超时

# 改进
# 不保存sum为数组 直接在原数组上用双指针遍历
# 头尾index分别代表正/逆向遍历sum
# 当头sum大于尾sum时，尾sum的index - 1，即在尾sum上按照逆序叠加一个元素
# 相反 头sum的index + 1
# 当头尾index相遇时，结束遍历，输出所找到的最大值

i = 0
i_rev = n - 1
di_sum = di[i]
di_rev_sum = di[i_rev]
max_sum = 0
while i < i_rev:
    if di_sum == di_rev_sum:
        max_sum = max(di_sum, max_sum)
        i += 1
        di_sum += di[i]

        i_rev -= 1
        di_rev_sum += di[i_rev]

    elif di_sum < di_rev_sum:
        i += 1
        di_sum += di[i]
    else:
        i_rev -= 1
        di_rev_sum += di[i_rev]
print(max_sum)

