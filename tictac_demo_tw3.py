import random
import os

def draw():
    if turn == 9:
        print ("DRAW!")
        print("\n")
        rexit()
        
def rexit():
    global field, board, turn, player, aionoff
    rexit = str(input("Press -r- to restart or -x- to exit: "))
    if not rexit == "r":
        while 1==1:
            if rexit == "x":
                break
            print("\nWhat are u doing??? I said -r- or -x- \nAnd how dare you call me stupid? \nIf i would be stupid i wouldn't ask questions like this.. \n ")
            rexit = str(input("Press -r- to restart or -x- to exit: "))
            if rexit == "r" or rexit == "x":
                break
    if rexit == "x":
        exit()
    elif rexit == "r":
        aionoff = str(input("2 Player game? (y/n): "))
        if not aionoff == "y":
            while 1==1:
                if aionoff == "n":
                    break
                print("\nJust press -y- or -n- and stop insulting me. I hate you so much\n ")
                aionoff = str(input("2 Player game? (y/n): "))
                if aionoff == "y" or aionoff == "n":
                    break
        field = ["_-_","_-_","_-_","_-_","_-_","_-_","_-_","_-_","_-_"]
        turn = 0
        player = 1
        os.system("clear")
        board()

def xcheck():
    if field[0] == " X " and field[1] == " X " and field[2] == " X ":
        print("X PLAYER WON!")
        rexit()
    if field[3] == " X " and field[4] == " X " and field[5] == " X ":
        print("X PLAYER WON!")
        rexit()
    if field[6] == " X " and field[7] == " X " and field[8] == " X ":
        print("X PLAYER WON!")
        rexit()
    if field[0] == " X " and field[3] == " X " and field[6] == " X ":
        print("X PLAYER WON!")
        rexit()
    if field[1] == " X " and field[4] == " X " and field[7] == " X ":
        print("X PLAYER WON!")
        rexit()
    if field[2] == " X " and field[5] == " X " and field[8] == " X ":
        print("X PLAYER WON!")
        rexit()
    if field[0] == " X " and field[4] == " X " and field[8] == " X ":
        print("X PLAYER WON!")
        rexit()
    if field[2] == " X " and field[4] == " X " and field[6] == " X ":
        print("X PLAYER WON!")
        rexit()

def ocheck():
    if field[0] == " O " and field[1] == " O " and field[2] == " O ":
        print("O PLAYER WON!")
        rexit()
    if field[3] == " O " and field[4] == " O " and field[5] == " O ":
        print("O PLAYER WON!")
        rexit()
    if field[6] == " O " and field[7] == " O " and field[8] == " O ":
        print("O PLAYER WON!")
        rexit()
    if field[0] == " O " and field[3] == " O " and field[6] == " O ":
        print("O PLAYER WON!")
        rexit()
    if field[1] == " O " and field[4] == " O " and field[7] == " O ":
        print("O PLAYER WON!")
        rexit()
    if field[2] == " O " and field[5] == " O " and field[8] == " O ":
        print("O PLAYER WON!")
        rexit()
    if field[0] == " O " and field[4] == " O " and field[8] == " O ":
        print("O PLAYER WON!")
        rexit()
    if field[2] == " O " and field[4] == " O " and field[6] == " O ":
        print("O PLAYER WON!")
        rexit()

def board():
    f = open('logo.txt','rt')
    print(f.read())

    print("\n")
    print("                           |"+field[6]+"|"+field[7]+"|"+field[8]+"|")
    print("                           |"+field[3]+"|"+field[4]+"|"+field[5]+"|")
    print("                           |"+field[0]+"|"+field[1]+"|"+field[2]+"|")
    print("\n")

def firstplayer():
    global turn, player
    if field[a-1] == "_-_":
        field[a-1] = " X "
        if aionoff == "y":
            player = 2
        if aionoff == "n":
            player = 3
    else:
        print("\nChoose another place! \n")
        turn -= 1
        player = 1
    os.system("clear")
    board()
    
def secondplayer():
    global turn, player
    if field[a-1] == "_-_":
        field[a-1] = " O "
        player = 1
    else:
        print("\nChoose another place!\n ")
        turn -= 1
        player = 2
    os.system("clear")
    board()

#ACTION @@@
field = ["_-_","_-_","_-_","_-_","_-_","_-_","_-_","_-_","_-_"]
player = 1
turn = 0 
aionoff = str(input("2 Player game? (y/n): "))
if not aionoff == "y":
    while 1==1:
        if aionoff == "n":
            break
        print("\n-y- or -x- PLEASE! I believe in you! \n ")
        aionoff = str(input("2 Player game? (y/n): "))
        if aionoff == "y" or aionoff == "n":
            break
os.system("clear")
f = open('logo.txt','rt')
print(f.read())
print("\n")
print("                           |_7_|_8_|_9_|")
print("           TUTORIAL:       |_4_|_5_|_6_|")
print("                           |_1_|_2_|_3_|")
print("\n")

#STEPS @@@
while turn <= 9:
    try:
        #PLAYER 1 @@@
        if player == 1:
            a = int(input("num: "))
            if a < 1 or a > 9:
                while 1==1:
                    print("\nPress(1-9) What kind of num pad do you have??? Who is stupid now?\n ") 
                    a = int(input("num: "))
                if a > 0 and a < 10:
                    break
            firstplayer()
            turn += 1
            xcheck()
            draw()
    except ValueError:
        print("\nStop making mistakes! It's so borring.\n ")
        continue
    #AI PLAYER @@@
    if player == 3 and aionoff == "n" :
        while 1 == 1:
            rand = random.randint(0,8)
            if field[rand] == "_-_":
                field[rand] = " O "
                break
        player = 1
        turn += 1
        os.system("clear")
        board()
        ocheck()
        draw()
    #PLAYER 2 @@@
    try:
        if player == 2 and aionoff == "y":
            a = int(input("num: "))
            if a < 1 or a > 9:
                while 1==1:
                    print("\nDo you want to play with me?<3 THAN PRESS (1-9)!!!!\n ")
                    a = int(input("num: "))
                if a > 0 and a < 10:
                    break
            secondplayer()
            turn += 1
            ocheck()
            draw()
    except ValueError:
        print("\nStop making mistakes! It's so borring..\n ")
        continue