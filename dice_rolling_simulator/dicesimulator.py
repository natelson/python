import random


def print_dice(x:int):
    if x == 1:
        dice_1()
    elif x == 2:
        dice_2()
    elif x == 3:
        dice_3()
    elif x == 4:
        dice_4()
    elif x == 5:
        dice_5()
    elif x == 6:
       dice_6()
    else:
        print('Invalid')

def dice_1():
    print("____________")
    print("|           |")
    print("|     0     |")
    print("|           |")
    print("____________")

def dice_2():
    print("____________")
    print("|           |")
    print("|  0      0 |")
    print("|           |")
    print("____________")


def dice_3():
    print("____________")
    print("|     0     |")
    print("|     0     |")
    print("|     0     |")
    print("____________")

def dice_4():
    print("____________")
    print("| 0        0|")
    print("|           |")
    print("| 0        0|")
    print("____________")

def dice_5():
    print("____________")
    print("| 0        0|")
    print("|      0    |")
    print("| 0        0|")
    print("____________")


def dice_6():
    print("____________")
    print("| 0        0|")
    print("| 0        0|")
    print("| 0        0|")
    print("____________")


while True:
    choice = input('Rollout the dice? Y/N\n')
    if choice.upper() == 'Y':
        x = random.randint(1,6)
        print_dice(x)
    else:
        break
