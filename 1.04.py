# 题目描述
# 小Q得到一个神奇的数列: 1, 12, 123,...12345678910,1234567891011...。
# 并且小Q对于能否被3整除这个性质很感兴趣。
# 小Q现在希望你能帮他计算一下从数列的第l个到第r个(包含端点)有多少个数可以被3整除。
# 输入描述:
# 输入包括两个整数l和r(1 <= l <= r <= 1e9), 表示要求解的区间两端。
# 输出描述:
# 输出一个整数, 表示区间内能被3整除的数字个数。
# 示例1
# 输入
#
# 2 5
# 输出
#
# 3
# 说明
#
# 12, 123, 1234, 12345...
# 其中12, 123, 12345能被3整除。
# import sys
#
# line = sys.stdin.readline()
# if line is "":
#     print('')
# else:
#     l, r = list(map(int, line.split()))
#     # nums = [str(i) for i in range(1, r + 1)]
#     # for i in range(1, len(nums)):
#     #     nums[i] = nums[i - 1] + nums[i]
#     # nums = nums[l - 1:r]
#     # count = 0
#     # for i in nums:
#     #     if int(i) % 3 == 0:
#     #         count += 1
#     # print(count)
#
#     # l, r = 2, 5
#     # nums = [str(r)]
#
#     nums = []
#     # i = 1
#     for i in range(l, r + 1):
#         # nums.append(str(i) + nums[i - 1])
#         # i += 1
#         nums.append(str(i))
#     pre_num = ''
#     for i in range(1, l):
#         pre_num += str(i)
#     # print(pre_num)
#     nums_list = [pre_num]
#     for i in range(len(nums) - 1, -1, -1):
#         # print(nums_list[i])
#         # print(nums[i])
#         nums_list.append(nums_list[-1] + nums[i])
#     print(nums)
#     # print(nums_list[1:])
#     count = 0
#     for i in nums_list[1:]:
#         if int(i) % 3 == 0:
#             count += 1
#     print(count)

import sys


def func(x):
    return (x + 2) // 3


line = sys.stdin.readline()
if line.strip() is not "":
    l, r = list(map(float, line.split()))
    print(l, r)
    print(r - l + 1 - (func(r) - func(l - 1)))
else:
    print(0)
