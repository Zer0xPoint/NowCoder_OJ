# 题目描述
# 牛牛总是睡过头，所以他定了很多闹钟，只有在闹钟响的时候他才会醒过来并且决定起不起床。从他起床算起他需要X分钟到达教室，上课时间为当天的A时B分，请问他最晚可以什么时间起床
# 输入描述:
# 每个输入包含一个测试用例。
# 每个测试用例的第一行包含一个正整数，表示闹钟的数量N(N<=100)。
# 接下来的N行每行包含两个整数，表示这个闹钟响起的时间为Hi(0<=A<24)时Mi(0<=B<60)分。
# 接下来的一行包含一个整数，表示从起床算起他需要X(0<=X<=100)分钟到达教室。
# 接下来的一行包含两个整数，表示上课时间为A(0<=A<24)时B(0<=B<60)分。
# 数据保证至少有一个闹钟可以让牛牛及时到达教室。
# 输出描述:
# 输出两个整数表示牛牛最晚起床时间。
# 示例1
# 输入
#
# 3
# 5 0
# 6 0
# 7 0
# 59
# 6 59
# 输出
#
# 6 0
n = int(input())
alarms = [list(map(int, input().split())) for i in range(n)]
x = int(input())
a, b = list(map(int, input().split()))
acceptable_wakeup_minutes = alarms[0][0] * 60 + alarms[0][1]
acceptable_arrive_minutes = a * 60 + b
for alarm in alarms:
    alarm_minuets = alarm[0] * 60 + alarm[1]
    arrive_minuets = alarm_minuets + x
    if arrive_minuets <= acceptable_arrive_minutes and acceptable_wakeup_minutes < alarm_minuets:
        acceptable_wakeup_minutes = alarm_minuets
print(acceptable_wakeup_minutes // 60, acceptable_wakeup_minutes % 60)
