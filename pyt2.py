print("2222222")
print("111111", end="")

print("6"*10)
print("=============================")
# 分支语句 if
a = 10
if a > 0:
    print("a是正数")
else:
    print("a不是正数")

# age = input("请输入年龄：")
# if int(age) > 12 and age < 30:
#     print("青年")
# score = input("请输入成绩：")
# score = int(score)
# if 90 <= score < 100:
#     print("成绩为A")
# elif 80 <= score < 90:
#     print("成绩为B")
# elif 70 <= score < 80:
#     print("成绩为C")
# elif 0 <= score < 60:
#     print("成绩为E")
# else:
#     print("非法输入")
print("=============================")
# 产生随机数

import random
while True:

    num = input("输入：剪刀（0） 石头（1） 布（2）")
    num = int(num)
    computer = random.randint(0,2)
    if ((num == 0) and (computer ==2)) or ((num == 1) and (computer ==0)) or ((num == 2) and (computer ==1)) :
        print("你赢了！")
    elif num == computer:
        print("平局")
    else:
        print("你输了，洗洗手再来吧！")
