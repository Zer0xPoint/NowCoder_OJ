# 题目描述
# 牛牛和妞妞在一天晚上决定一起去看一场情人节演唱会，可是由于这场演唱会实在太出名了，有很多情侣都来观看，牛牛和妞妞不小心被人流冲散了！
# 维持秩序的人决定，让大家排成一列，相邻两个进去的人（2k-1和2k，k为正整数）坐在相邻座位。但是现在的队伍乱糟糟的，有很多情侣都不在相邻位置。维持秩序的人同意让情侣们跟相邻的人交换位置，直到所有情侣都在2k-1和2k位置上为止。
# 但是维持秩序的人很没有耐心，所以需要最少的交换次数，你能帮情侣们算出这个次数吗？
# 输入描述:
# 第一行一个整数n，表示一共有n对情侣，编号从1到n。同一对情侣编号相同。1<=n<=100
# 第二行2n个整数ai，表示编号为ai的情侣在第i个位置。1<=ai<=n
# 输出描述:
# 一个整数，代表最少交换次数。
# 示例1
# 输入
#
# 3
# 3 3 2 2 1 1
# 输出
#
# 0
# 示例2
# 输入
#
# 4
# 1 2 3 4 1 2 3 4
# 输出
#
# 6

# 思路
# 以数组第一个元素ai[0]为基准，保存其值为first_item
# 在ai中找到第二个与first_item相等的数，记录其坐标为 second_item_index
# 在数组中删除这两个相等的元素
# 因为每次都会删除首部元素，删除之后迭代前的第二个元素就会成为首个元素
# 而且每次都以第一个元素ai[0]为基准，故 second_item_index 就是两个相同元素的距离
# 结果为 res 累加上 second_item_index

n = int(input())
ai = list(map(int, input().split()))
res = 0
while len(ai) > 0:
    first_item = ai[0]
    del ai[0]  # 从list中删除首个元素
    second_item_index = ai.index(first_item)  # 找到第二个元素的位置（也就是与首个元素的距离）
    res += second_item_index  # 累加距离
    del ai[second_item_index]  # 从list中删除第二个元素
print(res)
