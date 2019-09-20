# 题目描述
#
# 通过键盘输入一串小写字母(a~z)组成的字符串。
# 请编写一个字符串归一化程序，统计字符串中相同字符出现的次数，并按字典序输出字符及其出现次数。
# 例如字符串"babcc"归一化后为"a1b2c2"
#
#
#
# 输入描述:
# 每个测试用例每行为一个字符串，以'\n'结尾，例如cccddecca
# 输出描述:
# 输出压缩后的字符串ac5d2e
# 示例1
# 输入
#
# dabcab
# 输出
#
# a2b2c1d1
n = input()
n_dict = {}
for i in n:
    if i not in n_dict:  # 若dict中不包含此元素
        n_dict.update({i: 1})  # 将元素以 {元素:出现次数} 的格式，添加到dict中
    else:
        n_dict[i] += 1  # 若存在元素，则将对应元素的出现次数+1

# 格式化输出
res_list = []
for i in n_dict:
    res_list.append(str(i) + str(n_dict[i]))
res_list.sort()
for i in res_list:
    print(i, end='')  # 输出不换行
