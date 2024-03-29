# 题目描述
# 平面内有n个矩形, 第i个矩形的左下角坐标为(x1[i], y1[i]), 右上角坐标为(x2[i], y2[i])。
# 如果两个或者多个矩形有公共区域则认为它们是相互重叠的(不考虑边界和角落)。
# 请你计算出平面内重叠矩形数量最多的地方,有多少个矩形相互重叠。
# 输入描述:
# 输入包括五行。
# 第一行包括一个整数n(2 <= n <= 50), 表示矩形的个数。
# 第二行包括n个整数x1[i](-10^9 <= x1[i] <= 10^9),表示左下角的横坐标。
# 第三行包括n个整数y1[i](-10^9 <= y1[i] <= 10^9),表示左下角的纵坐标。
# 第四行包括n个整数x2[i](-10^9 <= x2[i] <= 10^9),表示右上角的横坐标。
# 第五行包括n个整数y2[i](-10^9 <= y2[i] <= 10^9),表示右上角的纵坐标。
# 输出描述:
# 输出一个正整数, 表示最多的地方有多少个矩形相互重叠,如果矩形都不互相重叠,输出1。
# 示例1
# 输入
#
# 2
# 0 90
# 0 90
# 100 200
# 100 200
# 输出
#
# 2
n = int(input())
matrix = [list(map(int, input().split())) for i in range(4)]
res = 0
for x in matrix[0] + matrix[2]:  # 所有x轴的坐标
    for y in matrix[1] + matrix[3]:  # 所有y轴坐标
        count = 0
        for i in range(n):
            if matrix[0][i] <= x <= matrix[2][i] and matrix[1][i] <= y <= matrix[3][i]:
                # 若存在两个坐标满足条件，则证明两个矩形在（y，y）有交点
                # 两个相交矩形的交点坐标肯定在它们x轴，y轴的集合之中
                count += 1
        res = max(count, res)  # 若count超过之前记录的res，则替换res
print(res)
