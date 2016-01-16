# needs random
import random

def instructions():
    print('You have just entered a large old house')

def setup():
    global mon_list
    mon_list= ['Troll', 'Ghost', 'Imp', 'Bat', 'Giant', 'Zombie', 'Grockle', 'Hound']
    global mon_react_list
    mon_react_list= [ -8, -9, -5, -50, -2, -50, 3, -50 ]
    global desc_list
    desc_list = ['Hall','Door Locked','Door Open','Staircase','Desk','Cupboard','Clock','Piano','Chair','Statue','Fireplace','Bookcase']
    global treas_list
    treas_list = ['Trap','Key','Lamp','Trigger','Cellar','Nothing','Nothing','Treasure']
    # start pos
    global x,y,z
    x=3
    y=6
    z=1
    # start attribs
    global strength, m_kill, treas, keys, lamps, charisma, clues, time, end_game
    keys = 0
    lamps = 0
    treas = 0
    strength = 100
    m_kill =0
    clues = 0
    charisma = random.randint(1,10)+5
    # 1d10+5
    end_game = False
    time = '000000'
    # setup m (x,y,z)
    

    # setup t (x,y,z)
    

def look():
    show('North',0,-1)
    show('West',-1,0)
    show('South',-1,0)
    show('East',0,-1)
    show('by the side',0,0)

def show(dir,x_mod,y_mod):
    print(dir, 'of you is a')
    # show desc of m

def command():
    c=int(input('[1] Move, [2] Explore, [3] Open, [4] Status: '))
    if c == 1:
        move()
    elif c == 2:
        explore()
    elif c == 3:
        open_it()
    elif c==4:
        status()
    else:
        print ('Huh?')

def move():
    b=2
    while b==2:
        dir = input('[N]orth, [S]outh, [E]ast, [W]est: ')
        if dir == 'N':
            c= -1
            b=0
        elif dir == 'S':
            c=1
            b=0
        elif dir =='E':
            c=0
            b=1
        elif dir == 'W':
            c=0
            b= -1
        else:
            print('Huh?')
    # check new loc
    # if new loc value = 0, can't move there inc row/col 0 and 7
    # check for locked dorr -no move


def status():
    print('Your status is')
    print('Strength:', strength)
    print('Monsters killed:', m_kill)
    print('Treasure:', treas)
    print('Keys:', keys)
    print('Lamps:', lamps)
    print('Charisma:', charisma)
    print('Clues:', clues)
    print('Position:', x, y)
    print('Level:', z)
    print('Time:', time)
    score = m_kill*100+treas+10*(keys+lamps)+10*strength
    # - time(4)
    print('Score:', score)
    
    

def debug():
    for n in mon_list:
        print (n)
    print (mon_list)

    print (mon_react_list)
    for n in mon_react_list:
        print (n)
    for n in treas_list:
        print (n)
    print(x,y,z)
    

print('Treasure House')
instructions()
setup()

debug()

while end_game == False:
    look()
    command()
    end_game = True
# end of game
print('Final Score')
status()


