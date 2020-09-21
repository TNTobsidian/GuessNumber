import time,random
number = int(random.randint(1,100))
round = int(0)
min = int(1)
max = int(100)

def guess():
    global min
    global max
    global round
    round = round + 1
    print('现在是第'+str(round)+'次！')
    time.sleep(1.5)
    print('=============\n最小值为'+str(min)+'\n最大值为'+str(max)+'\n=============')
    guess = int(input('您的猜测是：'))
    if guess == number:
        print('BOOM!!! 你中奖啦~~\n你猜到了程序随机生成的数字，快去兑现惩罚吧！\n若无操作，程序将会在2分钟后退出。')
        time.sleep(117)
        print('Bye')
        time.sleep(3)
        exit()
    elif guess < number:
        min = guess
        print('你猜小了！现在的最小值缩小为'+str(min))
        time.sleep(1.5)
    elif guess > number:
        max = guess
        print('你猜大了！现在的最大值缩小为'+str(max))
        time.sleep(1.5)
    else:
        print('请输入有效的数字。')

print('欢迎来到本游戏！\n在本游戏中，程序将会随机生成一个数字。\n数字在1~100范围内。\n输入一个数字，程序将会判断其范围。\n若猜中会提示你，\n若没猜中会缩小范围至你猜的数字。')
confirm = input('输入1继续程序，若输入其他则会退出游戏。')
if confirm == '1':
    print('好的！继续游戏~')
    while guess != number:
        guess()
else:
    exit()
