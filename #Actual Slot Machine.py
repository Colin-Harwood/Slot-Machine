#Actual Slot Machine
import random

money = 100

spinAmnt = 5 

symbols = {1:'🍒', 2:'🍇', 3:'🔔', 4:'🍀', 5:'🍋', 6:'$' ,7:'7'}


#gives three random symbols back as a llist
def spin():
    x = [symbols[random.randint(1,7)], symbols[random.randint(1,7)], symbols[random.randint(1,7)]]
    print(x)
    return x

#checks whether one two or three are the same and gives you money back accordingly
#need to revise the math
def checkBack(lis):
    s1, s2, s3 = lis
    if lis.count(s1) == 3 or lis.count(s2) == 3 or lis.count(s3) == 3:
        print('10X YOUR RICH(now gamble it all away again)')
        return 10
    elif lis.count(s1) == 1 and lis.count(s2) == 1 and lis.count(s3) == 1:
        print('RIP YOUR CASH🪦🪦💀💀')
        return 0
    elif lis.count(s1) == 2 or lis.count(s2) == 2 or lis.count(s3) == 2:
        print('Double')
        return 2
    

def spinAmount():
    global money
    global spinAmnt
    while True:
        value = input('How much money would you like to change your spin to:')
        try:
            value = int(value)
        except ValueError:
            print('Valid number, please')
            continue
        if value <= money:
            spinAmnt = value 

            break
        else:
            print(f'Please enter a valid amount of money. Your money is currently: {money}')
     
def returnMoney(spinAmount, value):
    global money
    global spinAmnt
    money -= int(spinAmount)
    money += int(spinAmount) * int(value)

def moneyAdd(multiplier, bet):
    return int(multiplier) * int(bet)

iby = True

spinAmount()

while True == True:
    print('---------------------------------------------')
    if money == 0:
        print("You're out of money you lose")
        break
    
    
    out = spin()

    winn = checkBack(out)

    print(f'You current spin bet is {spinAmnt}')

    returnMoney(spinAmnt, winn)

    print(f'You currently have: {money}')

    inp = input('Hit enter to spin. Type m to change to change the amount being bet each spin. Enter stop to stop playing.')
    if len(inp) == 0:
        continue
    elif inp.lower() == 'm' :
        spinAmount()
    elif inp.lower() == 'stop':
        break



