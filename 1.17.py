# 题目描述
# 小易在学校中学习了关于字符串的理论, 于是他基于此完成了一个字典的项目。
# 小易的这个字典很奇特, 字典内的每个单词都包含n个'a'和m个'z', 并且所有单词按照字典序排列。
# 小易现在希望你能帮他找出第k个单词是什么。
# 输入描述:
# 输入包括一行三个整数n, m, k(1 <= n, m <= 100, 1 <= k <= 10**9), 以空格分割。
# 输出描述:
# 输出第k个字典中的字符串，如果无解，输出-1。
# 示例1
# 输入
#
# 2 2 6
# 输出
#
# zzaa
# 说明
#
# 字典中的字符串依次为aazz azaz azza zaaz zaza zzaa
n, m, k = list(map(int, input().split()))
# todo
