# 题目描述
# 对于一个长度为n的整数序列，你需要检查这个序列是否可以是非递减序列，假如你最多可以改变其中的一个数。
# 非递减序列的定义是：array[i]<=array[i+1], for 1<=i<n;
# 输入描述:
# 输入是一个长度为n的整数序列。
# 输出描述:
# 输出为； 是为1； 否为0
# 示例1
# 输入
#
# 3 4 6 5 5 7 8
# 输出
#
# 1
# 说明
#
# 将6变成4， 序列变成 [3 4 4 5 5 7 8]，符合非递减序列，因此输出1
# 示例2
# 输入
#
# 3 4 6 5 4 7 8
# 输出
#
# 0
# 备注:
# n的取值范围为： [2, 1000]
num_list = list(map(int, input().split()))
count = 0
# for i in range(len(num_list)):
#     if i > 0:
#         if not num_list[i - 1] <= num_list[i]:
#             count += 1
# print(1) if count <= 1 else print(0)
for i in range(len(num_list)):
    if i > 0:
        if not num_list[i - 1] <= num_list[i]:
            count += 1
    if count > 1:
        print(0)
        break
if count <= 1:
    print(1)
