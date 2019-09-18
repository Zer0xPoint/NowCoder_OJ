# 题目描述
# 给定一个字符串，你的任务是计算这个字符串中有多少个回文子串。
# ("回文串”是一个正读和反读都一样的字符串，比如“level”或者“noon”等等就是回文串。)
# 具有不同开始位置或结束位置的子串，即使是由相同的字符组成，也会被计为是不同的子串。
# 可用C++,Java,C#实现相关代码逻辑
# 输入描述:
# 输入一个字符串S 例如“aabcb”(1 <= |S| <= 50), |S|表示字符串S的长度。
# 输出描述:
# 符合条件的字符串有"a","a","aa","b","c","b","bcb"
#
# 所以答案:7
# 示例1
# 输入
#
# aabcb
# 输出
#
# 7

str = input()


def is_palindrome(str):
    is_palindrome_flag = True
    for i in range(len(str) // 2):
        if str[i] is not str[-i - 1]:
            is_palindrome_flag = False
    return is_palindrome_flag


# res_list = []
#
#
# def rec_palindrome(str, i, j, res_list):
#     if j - i <= 0:
#         return 0
#     elif is_palindrome(str[i:j]):
#         # print(str[i:j])
#         res_list.append(str[i:j])
#         # return 1
#     A = rec_palindrome(str, i, j - 1, res_list)
#     B = rec_palindrome(str, i + 1, j, res_list)
#     # return A + B
#
#
# rec_palindrome(str, 0, len(str), res_list)
# print(len(set(res_list)) + len(str))
# input 'aaa'
# output 5 instead of 6
# cause by set(res_list)

# DP
# 用数组储存 str[x,y] 是否是回文，若是则 arr[x][y] 为1，否则为0
# 因为一个字母必然是回文，故 arr 对角线为1
# 也可以将对角线置为0，在最后加上 str 的字符个数即可
# 又因为字符串长度大于0，所以 x 必须小于 y，故arr只用填写一半，可以忽略 x 大于 y 的情况
res = 0
# arr = [[0 for _ in range(len(str))] for _ in range(len(str))]
for x in range(0, len(str)):
    for y in range(x, len(str)):
        if is_palindrome(str[x:y + 1]):
            # arr[x][y] = 1
            res += 1

print(res)
# print(arr)
