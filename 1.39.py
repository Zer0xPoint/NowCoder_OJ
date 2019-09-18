# 题目描述
# 给定两个字符串，已知可以使用三种方式进行变换
# 1. 插入一个字符
# 2. 删除一个字符
# 3. 更改一个字符
# 请设计一个算法，找到两个字符串之间的经历几次最小变换，可以字符串1转换成字符串2
# 输入描述:
# 输入两个字符串，字符串的长度<=1000
# 输出描述:
# 最小变换次数
# 示例1
# 输入
#
# hello
# helle
# 输出
#
# 1

# https://blog.csdn.net/weixin_42564710/article/details/97034924

str1 = input()
str2 = input()

n = len(str1) + 1  # 在两个str前添加相同字符 使得dp[0][0]恒为0
m = len(str2) + 1

dp = [[0 for _ in range(m)] for _ in range(n)]

for i in range(n):
    dp[i][0] = i

for j in range(m):
    dp[0][j] = j

for j in range(1, m):
    for i in range(1, n):
        if str1[i - 1] == str2[j - 1]:  # 减去初始化时加上的相同字符
            dp[i][j] = dp[i - 1][j - 1]  # 不用替换 直接取上一次的值
        else:
            dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1

print(dp[-1][-1])
