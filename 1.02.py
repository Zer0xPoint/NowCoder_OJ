# 题目描述
# Shopee物流会有很多个中转站。在选址的过程中，会选择离用户最近的地方建一个物流中转站。
# 假设给你一个二维平面网格，每个格子是房子则为1，或者是空地则为0。找到一个空地修建一个物流中转站，使得这个物流中转站到所有的房子的距离之和最小。 能修建，则返回最小的距离和。如果无法修建，则返回 -1。
#
# 若范围限制在100*100以内的网格，如何计算出最小的距离和？
# 当平面网格非常大的情况下，如何避免不必要的计算？
# 输入描述:
# 4
# 0 1 1 0
# 1 1 0 1
# 0 0 1 0
# 0 0 0 0
#
# 先输入方阵阶数，然后逐行输入房子和空地的数据，以空格分隔。
# 输出描述:
# 8
#
# 能修建，则返回最小的距离和。如果无法修建，则返回 -1。
# 示例1
# 输入
#
# 4
# 0 1 1 0
# 1 1 0 1
# 0 0 1 0
# 0 0 0 0
# 输出
#
# 8

# 示例2
# 输入
#
# 4
# 1 1 1 1
# 1 1 1 1
# 1 1 1 1
# 1 1 1 1
# 输出
#
# -1
def cal_distance(matrix, x_center, y_center):
    real_x_center, real_y_center = 0, 0
    max_distance = n * 2  # 矩阵两点间的最大距离
    for i in range(n):  # 求在理想中心点附近最近的真实中心点
        for j in range(n):
            if matrix[i][j] == 0:  # 当点空时
                temp_distance = abs(x_center - i) + abs(y_center - j)
                if temp_distance < max_distance:  # 替换最大距离
                    max_distance = temp_distance
                    real_x_center, real_y_center = i, j  # 替换真实中心点坐标
    distance_sum = 0
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 1:  # 当点有房屋时
                distance_sum += abs(real_x_center - i) + abs(real_y_center - j)  # 计算距离总和
    return distance_sum


n = int(input())

matrix = [list(map(int, input().split())) for i in range(n)]

x_sum = 0
y_sum = 0
total_house_count = 0
for i in range(n):
    for j in range(n):
        if matrix[i][j] == 1:
            x_sum += i
            y_sum += j
            total_house_count += 1
if total_house_count == n * n:
    print(-1)
else:
    x_center = x_sum / total_house_count  # 利用平均值计算出理想中心点
    y_center = y_sum / total_house_count
    print(cal_distance(matrix, x_center, y_center))
