# 题目描述
# 给定一个 n y n 矩阵，其中每行和每列元素均按升序排序，找到矩阵中第k小的元素。
# 请注意，它是排序后的第k小元素，而不是第k个元素。
#
# 示例:
#
# matrix = [
#    [ 1,  5,  9],
#    [10, 11, 13],
#    [12, 13, 15]
# ],
# k = 8,
#
# 返回 13。
# 说明:
# 你可以假设 k 的值永远是有效的, 1 ≤ k ≤ n2 。
# 输入描述:
# 第一行为k的值和矩阵的n的值
#
# 后续为n*n矩阵的数字，以空格分割
# 输出描述:
# 矩阵中第k小的元素
# 示例1
# 输入
#
# 8 3
# 1 5 9
# 10 11 13
# 12 13 15
# 输出
#
# 13

k, n = list(map(int, input().split()))
n_matrix = [list(map(int, input().split())) for i in range(n)]
n_list = []
for i in range(n):
    n_list += n_matrix[i]
n_list.sort()
print(n_list[k - 1])