# 题目描述
# 把一个32-bit整型转成二进制，其中包含多少个1，比如5的二进制表达是101，其中包含2个1
# 输入描述:
# 输入为整型（十进制），只需兼容32-bit即可，如5、32
# 输出描述:
# 输出为字符串，如“2”、“1”
# 示例1
# 输入
#
# 5
# 输出
#
# 2
# 说明
#
# 5的二进制是101，其中包含2个1

n = int(input())
res = 0
while n > 0:
    if n % 2 == 1:
        res += 1
    n = n // 2
print(res)
