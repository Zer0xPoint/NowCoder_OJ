# 题目描述
# 输入参数为字符串型的n维数组，数组的每一项值为数组 或 int型数字。请实现一个函数，可以获取列表嵌套列表的最大深度为多少。
# 输入描述:
# 输入参数为字符串型的 n维数组，列表的每一项值为数组 或 int型数字。数组内的数组，每一项值，也可以是数组 或 int型数字。
# 输出描述:
# int型数字，表示数组嵌套的深度。
# 示例1
# 输入
#
# [[1], [2,3,4], [5,[2,3]], [7], [0,[1,2,3,4],3,5], [1,3], [3,2,4]]
# 输出
#
# 3
# 说明
#
# n维数组的深度为3

# 数到 [ count+1 数到 ] count-1

str_list = str(input())
count = 0
res = 0
for i in str_list:
    if i == '[':
        count += 1
    elif i == ']':
        res = max(count, res)
        count -= 1
print(res)
