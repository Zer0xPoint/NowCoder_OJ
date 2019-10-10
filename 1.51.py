# 题目描述
# 请写一个整数计算器，支持加减乘三种运算和括号。
# 输入描述:
# 一个待计算的表达式，包含0到9、+、-、*等符号。
# 输出描述:
# 输入计算结果
# 示例1
# 输入
#
# 复制
# 1+1
# 输出
#
# 复制
# 2
# 示例2
# 输入
#
# 复制
# 3+2*3*4-1
# 输出
#
# 复制
# 26
# 示例3
# 输入
#
# 复制
# (2*(3-4))*5
# 输出
#
# 复制
# -10
input_str = str(input())
operator_list = ['+', '-', '0', '*', '/']
num_stack = []
operator_stack = []
for i in input_str:
    if i.isdigit():
        num_stack.append(i)
    else:
        if len(operator_stack) > 0:
            last_opt_in_stack = operator_stack.pop()
            if operator_list.index(i) - operator_list.index(last_opt_in_stack) > 1:
                operator_stack.append(last_opt_in_stack)
                operator_stack.append(i)
            else:
                pass
print(operator_list.index('+'))
print(operator_list.index('*'))
# todo stack calculator
