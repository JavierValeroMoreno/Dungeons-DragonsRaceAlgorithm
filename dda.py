from colorama import Fore
from time import sleep

#VARIABLES
state = 0
user = Fore.WHITE
dm = Fore.GREEN
#METODOS
def case0():
    global state
    state = 1
    print(user + 'I wanna play Dungeons & Dragons!')
    sleep(1)

def case1():

    global state

    print(dm+ 'Yay! Why do you wanna play High Adventure Pop Fantasy?\n')
    sleep(1)
    print(user + '[a] I wanna go on adventures!\n'+
    '[b] Can i be someone from Lord of the Rings or somethings?\n'+
    '[c] I want to be a special snowflake\n'+
    '[d] I don\'t like fantasy I just wanna do this RPG thing\n')

    while True:
        print(user + '> ', end = "")
        choise = input()
        if choise == 'a':
            state = 2
            return
        elif choise == 'b':
            state = 3
            return
        elif choise == 'c':
            state = 4
            return
        elif choise == 'd':
            #Final 1
            final(1)
            state = -1
            return
        else:
            print(dm + 'Please, select one of the aboves options')
def case2():
    global state

    print(dm+ 'Every hero is special. What makes you special?')
    sleep(1)
    print(user+ '[a] Uh, I\'m an elf or something?\n'+
    '[b] What\'s on the inside. And my sword. And my magic.\n')
    while True:
        print(user + '> ', end = "")
        choise = input()
        if choise == 'a':
            state = 3
            return
        elif choise == 'b':
            state = 5
            return
        else:
            print(dm + 'Please, select one of the aboves options')
def case3():
    global state

    print(dm + 'Sure, I like the classic fantasy races anyway')
    sleep(1)
    print(user + '[a] Actually Tolkein is a hack. Gimme something DIFFERENT.\n[b] Me too!\n')
    while True:
        print(user + '> ', end = "")
        choise = input()
        if choise == 'a':
            state = 4
            return
        elif choise == 'b':
            state = 6
            return
        else:
            print(dm + 'Please, select one of the aboves options')
def case4():
    global state

    print(dm + 'Ugh. FINE. What makes you so damn special then?')
    sleep(1)
    print(user + '[a] I\'m DARK and MISUNDERSTOOD and there\'s no true RIGHT or WRONG\n'+
    '[b] I want to be a MOTHERFUCKING dragon\n[c] Uh, I dunno, just make me not an elf, dwarf, angel, devil or something done 100 thimes before okay?\n')
    while True:
        print(user + '> ', end = "")
        choise = input()
        if choise == 'a':
            state = 7
            return
        elif choise == 'b':
            state = 8
            return
        elif choise == 'c':
            state = 9
            return
        else:
            print(dm + 'Please, select one of the aboves options')
def case5():
    global state
    while True:
        print(user + '> ', end = "")
        choise = input()
        if choise == 'a':
            #Final 2
            final(2)
            state = -1
            return
        elif choise == 'b':
            state = 10
            return
        else:
            print(dm + 'Please, select one of the aboves options')
def case6():
    global state
    while True:
        print(user + '> ', end = "")
        choise = input()
        if choise == 'a':
            state = 11
            return
        elif choise == 'b':
            state = 12
            return
        elif choise == 'c':
            state = 13
            return
        else:
            print(dm + 'Please, select one of the aboves options')
def case7():
    global state
    while True:
        print(user + '> ', end = "")
        choise = input()
        if choise == 'a':
            state = 2
            return
        elif choise == 'b':
            state = 14
            return
        else:
            print(dm + 'Please, select one of the aboves options')
def case8():
    global state
    while True:
        print(user + '> ', end = "")
        choise = input()
        if choise == 'a':
            state = 2
            return
        elif choise == 'b':
            state = 15
            return
        else:
            print(dm + 'Please, select one of the aboves options')
def case9():
    global state
    while True:
        print(user + '> ', end = "")
        choise = input()
        if choise == 'a':
            state = 16
            return
        elif choise == 'b':
            state = 17
            return
        else:
            print(dm + 'Please, select one of the aboves options')
def case10():
    global state
    while True:
        print(user + '> ', end = "")
        choise = input()
        if choise == 'a':
            #Final 3
            final(3)
            state = -1
            return
        elif choise == 'b':
            #Final 4
            final(4)
            state = -1
            return
        else:
            print(dm + 'Please, select one of the aboves options')
def case11():
    global state
    while True:
        print(user + '> ', end = "")
        choise = input()
        if choise == 'a':
            state = 18
            return
        elif choise == 'b':
            state = 19
            return
        elif choise == 'c':
            state = 20
            return
        else:
            print(dm + 'Please, select one of the aboves options')
def case12():
    global state
    while True:
        print(user + '> ', end = "")
        choise = input()
        if choise == 'a':
            state = 21 
            return
        elif choise == 'b':
            state = 22
            return
        elif choise == 'c':
            state = 23
            return
        else:
            print(dm + 'Please, select one of the aboves options')
def case13():
    global state
    while True:
        print(user + '> ', end = "")
        choise = input()
        if choise == 'a':
            #Final 5
            final(5)
            state = -1
            return
        elif choise == 'b':
            #Final 6
            final(6)
            state = -1
            return
        else:
            print(dm + 'Please, select one of the aboves options')
def case14():
    global state
    while True:
        print(user + '> ', end = "")
        choise = input()
        if choise == 'a':
            state = 24
            return
        elif choise == 'b':
            state = 25
            return
        else:
            print(dm + 'Please, select one of the aboves options')
def case15():
    global state
    while True:
        print(user + '> ', end = "")
        choise = input()
        if choise == 'a':
            state = 26
            return
        elif choise == 'b':
            #Final 7
            final(7)
            state = -1
            return
        elif choise == 'c':
            #Final 8
            final(8)
            state = -1
            return
        else:
            print(dm + 'Please, select one of the aboves options')
def case16():
    global state
    while True:
        print(user + '> ', end = "")
        choise = input()
        if choise == 'a':
            state = 27 
            return
        elif choise == 'b':
            state = 28
            return
        elif choise == 'c':
            state = 29
            return
        elif choise == 'd':
            #Final 9
            final(9)
            state = -1
            return
        else:
            print(dm + 'Please, select one of the aboves options')
def case17():
    global state
    while True:
        print(user + '> ', end = "")
        choise = input()
        if choise == 'a':
            state = 30
            return
        elif choise == 'b':
            state = 31
            return
        else:
            print(dm + 'Please, select one of the aboves options')
def case18():
    global state
    while True:
        print(user + '> ', end = "")
        choise = input()
        if choise == 'a':
            #Final 10
            final(10)
            state = -1
            return
        elif choise == 'b':
            #Final 11
            final(11)
            state = -1
            return
        else:
            print(dm + 'Please, select one of the aboves options')
def case19():
    global state
    while True:
        print(user + '> ', end = "")
        choise = input()
        if choise == 'a':
            state = 32
            return
        elif choise == 'b':
            #Final 12
            final(12)
            state = -1
            return
        else:
            print(dm + 'Please, select one of the aboves options')
def case20():
    global state
    while True:
        print(user + '> ', end = "")
        choise = input()
        if choise == 'a':
            #Final 8
            final(8)
            state = -1
            return
        elif choise == 'b':
            #Final 13
            final(13)
            state = -1
            return
        else:
            print(dm + 'Please, select one of the aboves options')
def case21():
    global state
    while True:
        print(user + '> ', end = "")
        choise = input()
        if choise == 'a':
            state = 33
            return
        elif choise == 'b':
            #Final 14
            final(14)
            state = -1
            return
        elif choise == 'c':
            #Final 15
            final(15)
            state = -1
            return
        else:
            print(dm + 'Please, select one of the aboves options')
def case22():
    global state
    while True:
        print(user + '> ', end = "")
        choise = input()
        if choise == 'a':
            state = 34
            return
        elif choise == 'b':
            #Final 6
            final(6)
            state = -1
            return
        else:
            print(dm + 'Please, select one of the aboves options')
def case23():
    global state
    while True:
        print(user + '> ', end = "")
        choise = input()
        if choise == 'a':
            state = 13
            return
        elif choise == 'b':
            state = 30
            return
        else:
            print(dm + 'Please, select one of the aboves options')
def case24():
    global state
    while True:
        print(user + '> ', end = "")
        choise = input()
        if choise == 'a':
            state = 35
            return
        elif choise == 'b':
            state = 27
            return
        elif choise == 'c':
            #Final 4
            final(4)
            state = -1
            return
        elif choise == 'd':
            #Final 16
            final(16)
            state = -1
            return
        else:
            print(dm + 'Please, select one of the aboves options')
def case25():
    global state
    while True:
        print(user + '> ', end = "")
        choise = input()
        if choise == 'a':
            state = 20
            return
        elif choise == 'b':
            state = 36
            return
        else:
            print(dm + 'Please, select one of the aboves options')
def case26():
    global state
    while True:
        print(user + '> ', end = "")
        choise = input()
        if choise == 'a':
            state = 15
            return
        elif choise == 'b':
            #Final 17
            final(17)
            state = -1
            return
        else:
            print(dm + 'Please, select one of the aboves options')
def case27():
    global state
    while True:
        print(user + '> ', end = "")
        choise = input()
        if choise == 'a':
            state = 15
            return
        elif choise == 'b':
            #Final 18
            final(18)
            state = -1
            return
        elif choise == 'c':
            #Final 19
            final(19)
            state = -1
            return
        else:
            print(dm + 'Please, select one of the aboves options')
def case28():
    global state
    while True:
        print(user + '> ', end = "")
        choise = input()
        if choise == 'a':
            #Final 20
            final(20)
            state = -1
            return
        elif choise == 'b':
            #Final 21
            final(21)
            state = -1
            return
        elif choise == 'c':
            #Final 22
            final(22)
            state = -1
            return
        elif choise == 'd':
            #Final 23
            final(23)
            state = -1
            return
        else:
            print(dm + 'Please, select one of the aboves options')
def case29():
    global state
    while True:
        print(user + '> ', end = "")
        choise = input()
        if choise == 'a':
            #Final 24
            final(24)
            state = -1
            return
        elif choise == 'b':
            #Final 25
            final(25)
            state = -1
            return
        else:
            print(dm + 'Please, select one of the aboves options')
def case30():
    global state
    while True:
        print(user + '> ', end = "")
        choise = input()
        if choise == 'a':
            state = 37
            return
        elif choise == 'b':
            state = 38
            return
        elif choise == 'c':
            state = 16
            return
        elif choise == 'd':
            state = 48
            return
        elif choise == 'e':
            #Final 26
            final(26)
            state = -1
            return
        elif choise == 'f':
            #Final 27
            finL(27)
            state = -1
            return
        else:
            print(dm + 'Please, select one of the aboves options')
def case31():
    global state
    while True:
        print(user + '> ', end = "")
        choise = input()
        if choise == 'a':
            state = 39
            return
        elif choise == 'b':
            state = 40
            return
        else:
            print(dm + 'Please, select one of the aboves options')
def case32():
    global state
    while True:
        print(user + '> ', end = "")
        choise = input()
        if choise == 'a':
            #Final 28
            final(28)
            state = -1
            return
        elif choise == 'b':
            #Final 29
            final(29)
            state = -1
            return
        else:
            print(dm + 'Please, select one of the aboves options')
def case33():
    global state
    while True:
        print(user + '> ', end = "")
        choise = input()
        if choise == 'a':
            state = 41
            return
        elif choise == 'b':
            #Final 30
            final(30)
            state = -1
            return
        elif choise == 'c':
            #Final 31
            final(31)
            state = -1
            return
        elif choise == 'd':
            #Final 3
            final(3)
            state = -1
            return
        else:
            print(dm + 'Please, select one of the aboves options')
def case34():
    global state
    while True:
        print(user + '> ', end = "")
        choise = input()
        if choise == 'a':
            #Final 32
            final(32)
            state = -1
            return
        elif choise == 'b':
            #Final 33
            final(33)
            state = -1
            return
        elif choise == 'c':
            #Final 34
            final(34)
            state = -1
            return
        else:
            print(dm + 'Please, select one of the aboves options')
def case35():
    global state
    while True:
        print(user + '> ', end = "")
        choise = input()
        if choise == 'a':
            state = 41
            return
        elif choise == 'b':
            #Final 35
            final(35)
            state = -1
            return
        else:
            print(dm + 'Please, select one of the aboves options')
def case36():
    global state
    while True:
        print(user + '> ', end = "")
        choise = input()
        if choise == 'a':
            state = 42
            return
        elif choise == 'b':
            state = 43
            return
        else:
            print(dm + 'Please, select one of the aboves options')
def case37():
    global state
    while True:
        print(user + '> ', end = "")
        choise = input()
        if choise == 'a':
            state = 44
            return
        elif choise == 'b':
            #Final 36
            final(36)
            state = -1
            return
        else:
            print(dm + 'Please, select one of the aboves options')
def case38():
    global state
    while True:
        print(user + '> ', end = "")
        choise = input()
        if choise == 'a':
            #Final 31
            final(31)
            state = -1
            return
        elif choise == 'b':
            #Final 37
            final(37)
            state = -1
            return
        else:
            print(dm + 'Please, select one of the aboves options')
def case39():
    global state
    while True:
        print(user + '> ', end = "")
        choise = input()
        if choise == 'a':
            #Final 38
            final(38)
            state = -1
            return
        elif choise == 'b':
            #Final 39
            final(39)
            state = -1
            return
        elif choise == 'c':
            #Final 40
            final(40)
            state = -1
            return
        elif choise == 'd':
            #Final 41
            final(41)
            state = -1
            return
        else:
            print(dm + 'Please, select one of the aboves options')
def case40():
    global state
    while True:
        print(user + '> ', end = "")
        choise = input()
        if choise == 'a':
            state = 45
            return
        elif choise == 'b':
            state = 46
            return
        else:
            print(dm + 'Please, select one of the aboves options')
def case41():
    global state
    while True:
        print(user + '> ', end = "")
        choise = input()
        if choise == 'a':
            #Final 42
            final(42)
            state = -1
            return
        elif choise == 'b':
            #Final 43
            final(43)
            state = -1
            return
        else:
            print(dm + 'Please, select one of the aboves options')
def case42():
    global state
    while True:
        print(user + '> ', end = "")
        choise = input()
        if choise == 'a':
            state = 47
            return
        elif choise == 'b':
            #Final 44
            final(44)
            state = -1
            return
        else:
            print(dm + 'Please, select one of the aboves options')
def case43():
    global state
    while True:
        print(user + '> ', end = "")
        choise = input()
        if choise == 'a':
            #Final 19
            final(19)
            state = -1
            return
        elif choise == 'b':
            #Final 45
            final(45)
            state = -1
            return
        else:
            print(dm + 'Please, select one of the aboves options')
def case44():
    global state
    while True:
        print(user + '> ', end = "")
        choise = input()
        if choise == 'a':
            #Final 35
            final(35)
            state = -1
            return
        elif choise == 'b':
            #Final 46
            final(46)
            state = -1
            return
        elif choise == 'c':
            #Final 47
            final(47)
            state = -1
            return
        else:
            print(dm + 'Please, select one of the aboves options')
def case45():
    global state
    while True:
        print(user + '> ', end = "")
        choise = input()
        if choise == 'a':
            #Final 48
            final(48)
            state = -1
            return
        elif choise == 'b':
            #Final 49
            final(49)
            state = -1
            return
        else:
            print(dm + 'Please, select one of the aboves options')
def case46():
    global state
    while True:
        print(user + '> ', end = "")
        choise = input()
        if choise == 'a':
            state = 49
            return
        elif choise == 'b':
            #Final 50
            final(50)
            state = -1
            return
        else:
            print(dm + 'Please, select one of the aboves options')
def case47():
    global state
    while True:
        print(user + '> ', end = "")
        choise = input()
        if choise == 'a':
            #Final 51
            final(51)
            state = -1
            return
        elif choise == 'b':
            #Final 4
            final(4)
            state = -1
            return
        else:
            print(dm + 'Please, select one of the aboves options')
def case48():
    global state
    while True:
        print(user + '> ', end = "")
        choise = input()
        if choise == 'a':
            state = 50
            return
        elif choise == 'b':
            #Final 4
            final(4)
            state = -1
            return
        else:
            print(dm + 'Please, select one of the aboves options')
def case49():
    global state
    while True:
        print(user + '> ', end = "")
        choise = input()
        if choise == 'a':
            state = 51
            return
        elif choise == 'b':
            #Final 52
            final(52)
            state = -1
            return
        else:
            print(dm + 'Please, select one of the aboves options')
def case50():
    global state
    while True:
        print(user + '> ', end = "")
        choise = input()
        if choise == 'a':
            state = 47
            return
        elif choise == 'b':
            #Final 13
            final(13)
            state = -1
            return
        else:
            print(dm + 'Please, select one of the aboves options')
def case51():   
    global state
    while True:
        print(user + '> ', end = "")
        choise = input()
        if choise == 'a':
            #Final 53
            final(53)
            state = -1
            return
        elif choise == 'b':
            #Final 54
            final(54)
            state = -1
            return
        else:
            print(dm + 'Please, select one of the aboves options')    

def final(f):
    if f == 1:
        print(dm + 'You don\'t wanna play D&D, you want to play something else')
        sleep(1)
        print(user + 'Elves are dumb lets be vampires n shit')
        sleep(1)
        print(dm + 'And now we are playing Vampyre I hope you\'re happy')
    elif f == 2:
        print(dm + 'Congratulations! You are a Human!')
    elif f == 3:
        print(dm + 'Congratulations! You are a Half-Elf!')
    elif f == 4:
        print(dm + 'Congratulations! You are a Half-Orc!')
    elif f == 5:
        print(dm + 'Congratulations! You are a Firbolg!')
    elif f == 6:
        print(dm + 'Congratulations! You are a Goliath!')
    elif f == 7:
        print(dm + 'Congratulations! You are a Dragonborn!')
    elif f == 8:
        print(dm + 'Congratulations! You are a Kobold!')
    elif f == 9:
        print(dm + 'Congratulations! You are a Centaur!')
    elif f == 10:
        print(dm + 'Congratulations! You are a Stout!')
    elif f == 11:
        print(dm + 'Congratulations! You are a Lightfoot!')
    elif f == 12:
        print(dm + 'Congratulations! You are a Forest Gnome!')
    elif f == 13:
        print(dm + 'Congratulations! You are a Goblin!')
    elif f == 14:
        print(dm + 'Congratulations! You are a High Elf!')
    elif f == 15:
        print(dm + 'Congratulations! You are a Wood Elf!')
    elif f == 16:
        print(dm + 'Congratulations! You are a Tiefling!')
    elif f == 17:
        print(dm + 'Ugh, just get out')
    elif f == 18:
        print(dm + 'Congratulations! You are a Lizardfork!')
    elif f == 19:
        print(dm + 'Congratulations! You are a Yuan-Ti!')
    elif f == 20:
        print(dm + 'Congratulations! You are a Tabaxi!')
    elif f == 21:
        print(dm + 'Congratulations! You are a Minotaur!')
    elif f == 22:
        print(dm + 'Congratulations! You are a Loxadon!')
    elif f == 23:
        print(dm + 'Congratulations! You are a Shifter!')
    elif f == 24:
        print(dm + 'Congratulations! You are a Aarakocra!')
    elif f == 25:
        print(dm + 'Congratulations! You are a Kenku!')
    elif f == 26:
        print(dm + 'Congratulations! You are a Warforged!')
    elif f == 27:
        print(dm + 'Congratulations! You are a Changelings!')
    elif f == 28:
        print(dm + 'Congratulations! You are a Mountain Gnome!')
    elif f == 29:
        print(dm + 'Congratulations! You are a Deep Gnome!')
    elif f == 30:
        print(dm + 'Congratulations! You are a Eladrin!')
    elif f == 31:
        print(dm + 'Congratulations! You are a Sea Elf!')
    elif f == 32:
        print(dm + 'Congratulations! You are a Hill Dwarf!')
    elif f == 33:
        print(dm + 'Congratulations! You are a Mountain Dwarf!')
    elif f == 34:
        print(dm + 'Congratulations! You are a Duegar!')
    elif f == 35:
        print(dm + 'Congratulations! You are a Fallen!')
    elif f == 36:
        print(dm + 'Congratulations! You are a Aasimar!')
    elif f == 37:
        print(dm + 'Congratulations! You are a Triton!')
    elif f == 38:
        print(dm + 'Congratulations! You are a Fire Genasi!')
    elif f == 39:
        print(dm + 'Congratulations! You are a Eath Genasi!')
    elif f == 40:
        print(dm + 'Congratulations! You are a Air Genasi!')
    elif f == 41:
        print(dm + 'Congratulations! You are a Water Genasi!')
    elif f == 42:
        print(dm + 'Congratulations! You are a Drow!')
    elif f == 43:
        print(dm + 'Congratulations! You are a Shadar-Kai!')
    elif f == 44:
        print(dm + 'Congratulations! You are a Bugbear!')
    elif f == 45:
        print(dm + 'Congratulations! You are a Hobgoblin!')
    elif f == 46:
        print(dm + 'Congratulations! You are a Protector!')
    elif f == 47:
        print(dm + 'Congratulations! You are a Scourge!')
    elif f == 48:
        print(dm + 'Congratulations! You are a Githyanki!')
    elif f == 49:
        print(dm + 'Congratulations! You are a Githzerai!')
    elif f == 50:
        print(dm + 'Congratulations! You are a Vedalken!')
    elif f == 51:
        print(dm + 'Congratulations! You are a Orc!')
    elif f == 52:
        print(dm + 'Congratulations! You are a Simic Hybrid!')
    elif f == 53:
        print(dm + 'Congratulations! You are a Kalashtar!')
    elif f == 54:
        print(dm + 'Neither do I. Also I\'m banning you from my game')
        
switch = [case0,case1,case2,case3,case4,case5,case6,case7,case8,case9,
case10,case11,case12,case13,case14,case15,case16,case17,case18,case19,
case20,case21,case22,case23,case24,case25,case26,case27,case28,case29,
case30,case31,case32,case33,case34,case35,case36,case37,case38,case39,
case40,case41,case42,case43,case44,case45,case46,case47,case48,case49,
case50,case51]

while state != -1:
    switch[state]()