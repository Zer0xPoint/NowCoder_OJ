# 题目描述
# 小易觉得高数课太无聊了，决定睡觉。不过他对课上的一些内容挺感兴趣，所以希望你在老师讲到有趣的部分的时候叫醒他一下。你知道了小易对一堂课每分钟知识点的感兴趣程度，并以分数量化，以及他在这堂课上每分钟是否会睡着，你可以叫醒他一次，这会使得他在接下来的k分钟内保持清醒。你需要选择一种方案最大化小易这堂课听到的知识点分值。
# 输入描述:
# 第一行 n, k (1 <= n, k <= 10**5) ，表示这堂课持续多少分钟，以及叫醒小易一次使他能够保持清醒的时间。
# 第二行 n 个数，a1, a2, ... , an(1 <= ai <= 10**4) 表示小易对每分钟知识点的感兴趣评分。
# 第三行 n 个数，t1, t2, ... , tn 表示每分钟小易是否清醒, 1表示清醒。
# 输出描述:
# 小易这堂课听到的知识点的最大兴趣值。
# 示例1
# 输入
#
# 6 3
# 1 3 5 2 5 4
# 1 1 0 1 0 0
# 输出
#
# 16

n, k = list(map(int, input().split()))
a = list(map(int, input().split()))
t = list(map(int, input().split()))

pre_sum = 0  # 一定可以得到的分值
for i in range(n):
    if t[i] == 1:
        pre_sum += a[i]
        a[i] = 0
    # else:
    #     t[i] = a[i]
max_sum = 0
for i in range(n):
    if a[i] != 0:
        temp_sum = sum(a[i:i + k])
        max_sum = max(temp_sum, max_sum)
    if i > n - k + 1:
        break
print(max_sum + pre_sum)
