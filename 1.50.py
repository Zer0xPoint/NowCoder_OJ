# 题目描述
# 猛兽侠中精灵鼠在利剑飞船的追逐下逃到一个n*n的建筑群中，精灵鼠从（0,0）的位置进入建筑群，建筑群的出口位置为（n-1,n-1），建筑群的每个位置都有阻碍，
# 每个位置上都会相当于给了精灵鼠一个固定值减速，因为精灵鼠正在逃命所以不能回头只能向前或者向下逃跑，现在问精灵鼠最少在减速多少的情况下逃出迷宫？
# 输入描述:
# 第一行迷宫的大小: n >=2 & n <= 10000；
# 第2到n+1行，每行输入为以','分割的该位置的减速,减速f >=1 & f < 10。
# 输出描述:
# 精灵鼠从入口到出口的最少减少速度？
# 示例1
# 输入
#
# 3
# 5,5,7
# 6,7,8
# 2,2,4
# 输出
#
# 19
n = int(input())
f_matrix = [list(map(int, input().split(','))) for _ in range(n)]

# arr = [[f_matrix[j][i] for i in range(n)] for j in range(n)]
for i in range(1, n):
    f_matrix[i][0] += f_matrix[i - 1][0]
    f_matrix[0][i] += f_matrix[0][i - 1]

for i in range(1, n):
    for j in range(1, n):
        f_matrix[i][j] += min(f_matrix[i - 1][j], f_matrix[i][j - 1])
print(f_matrix[-1][-1])
