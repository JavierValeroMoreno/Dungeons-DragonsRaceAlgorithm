from colorama import Fore
from time import sleep

#VARIABLES
state = 0
user = Fore.WHITE
dm = Fore.GREEN
TIME = 1
#METODOS
def case0():
    global state
    state = 1
    print(user + "I wanna play Dungeons & Dragons!")
    sleep(TIME)

def case1():

    global state

    print(dm+ "Yay! Why do you wanna play High Adventure Pop Fantasy?\n")
    sleep(TIME)
    print(user + "[a] I wanna go on adventures!\n"+
    "[b] Can i be someone from Lord of the Rings or somethings?\n"+
    "[c] I want to be a special snowflake\n"+
    "[d] I don't like fantasy I just wanna do this RPG thing\n")

    while True:
        print(user + "> ", end = "")
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
            print(dm + "Please, select one of the aboves options")
def case2():
    global state

    print(dm+ "Every hero is special. What makes you special?")
    sleep(TIME)
    print(user+ "[a] Uh, I'm an elf or something?\n"+
    "[b] What's on the inside. And my sword. And my magic.\n")
    while True:
        print(user + "> ", end = "")
        choise = input()
        if choise == 'a':
            state = 3
            return
        elif choise == 'b':
            state = 5
            return
        else:
            print(dm + "Please, select one of the aboves options")
def case3():
    global state

    print(dm + "Sure, I like the classic fantasy races anyway")
    sleep(TIME)
    print(user + "[a] Actually Tolkein is a hack. Gimme something DIFFERENT.\n[b] Me too!\n")
    while True:
        print(user + "> ", end = "")
        choise = input()
        if choise == 'a':
            state = 4
            return
        elif choise == 'b':
            state = 6
            return
        else:
            print(dm + "Please, select one of the aboves options")
def case4():
    global state

    print(dm + "Ugh. FINE. What makes you so damn special then?")
    sleep(TIME)
    print(user + "[a] I'm DARK and MISUNDERSTOOD and there's no true RIGHT or WRONG\n[b] I want to be a MOTHERFUCKING dragon\n[c] Uh, I dunno, just make me not an elf, dwarf, angel, devil or something done 100 thimes before okay?\n")
    while True:
        print(user + "> ", end = "")
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
            print(dm + "Please, select one of the aboves options")
def case5():
    global state

    print(dm + "Human its ok for you")
    sleep(TIME)
    print(user + "[a] Yeah!\n[b] WAAAAAAAAAAAAAAIIIIIIIT")
    while True:
        print(user + "> ", end = "")
        choise = input()
        if choise == 'a':
            #Final 2
            final(2)
            state = -1
            return
        elif choise == 'b':
            state = 10
            sleep(TIME)
            print(dm + "Ugh. What is it?")
            sleep(TIME)
            print(user + "100% human is lame. Can i be part fantasy?")
            return
        else:
            print(dm + "Please, select one of the aboves options")
def case6():
    global state

    print(dm + "Nice! Wanna be human sized or tiny?")
    sleep(TIME)
    print(user + "[a] Kid-sized please!\n[b] I ain't pedo\n[c] ... is there a Big size?\n")
    while True:
        print(user + "> ", end = "")
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
            print(dm + "Please, select one of the aboves options")
def case7():
    global state

    print(dm + "Seriously, you could just like, be a dark and brooding white dude")
    sleep(TIME)
    print(user + "[a] Yeah, I guess you're right\n[b] NO. I wear the darkness on mi sleeve for all the world to see\n")
    while True:
        print(user + "> ", end = "")
        choise = input()
        if choise == 'a':
            state = 2
            return
        elif choise == 'b':
            state = 14
            return
        else:
            print(dm + "Please, select one of the aboves options")
def case8():
    global state

    print(dm + "You can't be a dragon")
    sleep(TIME)
    print(user + "[a] UGH\n[b] It's called Dungeons & Dragons you wangrod\n")
    
    while True:
        print(user + "> ", end = "")
        choise = input()
        if choise == 'a':
            print(user + "UGH")
            sleep(TIME)
            print("FIIINE")
            sleep(TIME)
            print("YOU SUCK")
            sleep(TIME)
            print("FUN POLICE")
            sleep(TIME)
            print("SRYSLY")
            state = 2
            return
        elif choise == 'b':
            print(dm + "FINE, PICK YOUR FAVOURITE COLOR")
            sleep(TIME)
            print(user + "YAY")
            state = 15
            return
        else:
            print(dm + "Please, select one of the aboves options")
def case9():
    global state

    print(dm + "Wow. That's helpful. Is Animal Person weird enough for you?")
    sleep(TIME)
    print(user + "[a] Uh, like a furry?\n[b] Gross no, I said SPECIAL\n")
    while True:
        print(user + "> ", end = "")
        choise = input()
        if choise == 'a':
            state = 16
            return
        elif choise == 'b':
            state = 17
            return
        else:
            print(dm + "Please, select one of the aboves options")
def case10():
    global state

    print(dm + "Alright. Are you half monstrous or half magical and pretty?")
    sleep(TIME)
    print(user + "[a] Yeah I still wanna be magical and pretty\n[b] Nah, give me some monster blood!\n")
    while True:
        print(user + "> ", end = "")
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
            print(dm + "Please, select one of the aboves options")
def case11():
    global state

    print(dm + "Alright, are you only a bit silly or extremely silly?")
    sleep(TIME)
    print(user + "[a] I would like to maintain some semblance of gravitas\n[b] EVERYTHINGS IS MAGIC AND GLITTER\n[c] Can i have a bit of dark humor?\n")

    while True:
        print(user + "> ", end = "")
        choise = input()
        if choise == 'a':
            print(dm + "You are a Halfling!")
            sleep(TIME)
            print(user + "Cool, off-brand Hobbit")
            state = 18
            return
        elif choise == 'b':
            print(dm + "You are a Gnome!")
            sleep(TIME)
            print(user + "... is this just a magic hobbit?")
            state = 19
            return
        elif choise == 'c':
            state = 20
            return
        else:
            print(dm + "Please, select one of the aboves options")
def case12():
    global state

    print(dm + "Lithe 'n' Pretty, or Short 'n' Swole?")
    sleep(TIME)
    print(user + "[a] I feel pretty\n[b] Do u even lift bro?\n[c] Uh, I don't like these options\n")
    while True:
        print(user + "> ", end = "")
        choise = input()
        if choise == 'a':
            print(dm + "You are a Elf!")
            sleep(TIME)
            print(user + "Yay, I'm done!")
            sleep(TIME)
            state = 21 
            return
        elif choise == 'b':
            state = 22
            return
        elif choise == 'c':
            state = 23
            return
        else:
            print(dm + "Please, select one of the aboves options")
def case13():
    global state

    print(dm + "... Sure. More of the Gentle Nature Giant or STRONK MEN")
    sleep(TIME)
    print(user + "[a] Pls be gentl\n[b] POOMP DE MOOSCLES\n")
    while True:
        print(user + "> ", end = "")
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
            print(dm + "Please, select one of the aboves options")
def case14():
    global state

    print(dm + "Okay, well we got options. First off, are you actually kind of mostrous or just misunderstood?")
    sleep(TIME)
    print(user + "[a] No one gets me, especially my Mom\n[b] You know what, I was the monster all along\n")
    while True:
        print(user + "> ", end = "")
        choise = input()
        if choise == 'a':
            state = 24
            return
        elif choise == 'b':
            state = 25
            return
        else:
            print(dm + "Please, select one of the aboves options")
def case15():
    global state
    
    print(dm + "It's Dragonborn ok to you?")
    sleep(TIME)
    print(user + "[a] This isn`t a dragon\n[b] Yeah!\n[c] Whait, does this come kid-sized?\n")
    while True:
        print(user + "> ", end = "")
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
            print(dm + "Please, select one of the aboves options")
def case16():
    global state

    print(dm + "Are you a furry?")
    sleep(TIME)
    print(user + "[a] Actually i'm a Scalie\n[b] OwO\n[c] No but birds are cool\n[d] Actually more of a horse thing for me\n")
    while True:
        print(user + "> ", end = "")
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
            print(dm + "Please, select one of the aboves options")
def case17():
    global state
    
    print(dm + "Are you just looking for weird for weird's sake at this point?")
    sleep(TIME)
    print(user + "[a] ... you're right. Let's stick to something at least a bit familiar\n[b] Yeah. Fuck you\n")
    while True:
        print(user + "> ", end = "")
        choise = input()
        if choise == 'a':
            state = 30
            return
        elif choise == 'b':
            state = 31
            return
        else:
            print(dm + "Please, select one of the aboves options")
def case18():
    global state
    
    print(dm + "Not done yet. Want to be slightly dwarfy, or nimble?")
    sleep(TIME)
    print(user + "[a] Make me hardy\n[b] Make me nimble\n")
    while True:
        print(user + "> ", end = "")
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
            print(dm + "Please, select one of the aboves options")
def case19():
    global state
    
    print(dm + "You can be a woodsy trickster or steampunk tinkerer")
    sleep(TIME)
    print(user + "[a] I AM MAGIC MUSHROOM\n[b] LETS MAKE TOYS\n")
    while True:
        print(user + "> ", end = "")
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
            print(dm + "Please, select one of the aboves options")
def case20():
    global state
    
    print(dm + "Fun-sized evil it is. How do you feel about Scales?")
    sleep(TIME)
    print(user + "[a] Yea\n[b] Nay\n")
    while True:
        print(user + "> ", end = "")
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
            print(dm + "Please, select one of the aboves options")
def case21():
    global state
    
    print(dm + "Wait, now it gets complicated. Is magic or nature more important to you?")
    sleep(TIME)
    print(user + "[a] Whait, none of this is right\n[b] Motherfucker I'm MADE of Magic\n[c] Elves are and always will be badass treehuggers\n")
    while True:
        print(user + "> ", end = "")
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
            print(dm + "Please, select one of the aboves options")
def case22():
    global state
    
    print(dm + "You are a Dwarf!")
    sleep(TIME)
    print(user + "[a] By Thorin's beard, time to drink ale and axe things!\n[b] Wait, I dont want to be short\n")
    while True:
        print(user + "> ", end = "")
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
            print(dm + "Please, select one of the aboves options")
def case23():
    global state
    
    print(dm + "Sure, but we're getting less classic now")
    sleep(TIME)
    print(user + "[a] Can I be a Giant?\n[b] No problem, lets move over there\n")
    while True:
        print(user + "> ", end = "")
        choise = input()
        if choise == 'a':
            state = 13
            return
        elif choise == 'b':
            state = 30
            return
        else:
            print(dm + "Please, select one of the aboves options")
def case24():
    global state
    
    print(dm + "Alright, why do people missunderstand you?")
    sleep(TIME)
    print(user + "[a] I'm the DARK AND BADASS version of some poncy elf, dwarf, or other wussy fantasy goody two shoes\n[b] I am actually an emotionless lizard person\n[c] One of my parents is from a species that is thought to be brutish and cruel\n[d] I've got sinister horns and look like the devil\n")
    while True:
        print(user + "> ", end = "")
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
            print(dm + "Please, select one of the aboves options")
def case25():
    global state
    
    print(dm + "Great! First off, how do you feel about comic relief?")
    sleep(TIME)
    print(user + "[a] Can't spell Slaughter without Laughter\n[b] Do you think this is funny?\n")
    while True:
        print(user + "> ", end = "")
        choise = input()
        if choise == 'a':
            state = 20
            return
        elif choise == 'b':
            state = 36
            return
        else:
            print(dm + "Please, select one of the aboves options")
def case26():
    global state
    
    print(dm + "Close enough")
    sleep(TIME)
    print(user + "[a] Okay. Fine\n[b] NOOOOOOOooooooo Lemme be a Dragon!")
    while True:
        print(user + "> ", end = "")
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
            print(dm + "Please, select one of the aboves options")
def case27():
    global state
    
    print(dm + "Like Ted Cruz. Neat. So what kind of scales we talking?")
    sleep(TIME)
    print(user + "[a] A MOTHERFUCKING DRAGON\n[b] I dunno just general reptiles I guess\n[c] Snek\n")
    while True:
        print(user + "> ", end = "")
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
            print(dm + "Please, select one of the aboves options")
def case28():
    global state
    
    print(dm + "*sigh*")
    sleep(TIME)
    print("WHATS YOUR FURSONA")
    sleep(TIME)
    print(user + "[a] Cat! Meow!\n[b] Cow! Moo!\n[c] Elephant... uh...\n[d] ... none of the others?\n")
    while True:
        print(user + "> ", end = "")
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
            print(dm + "Please, select one of the aboves options")
def case29():
    global state
    
    print(dm + "Magestic Eagle or Obnoxious Corvid?")
    sleep(TIME)
    print(user + "[a] I just wanna soar in the air majestic and free\n[b] CAW CAW MOTHERFUCKER\n")
    while True:
        print(user + "> ", end = "")
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
            print(dm + "Please, select one of the aboves options")
def case30():
    global state
    
    print(dm + "Uncommon Races! What sounds appealing to you?")
    sleep(TIME)
    print(user + "[a] We're on a mission from God\n[b] Basically Aquaman is the best DC superhero\n[c] Can I be an animal person?\n[d] Can I be a classic Monster?\n[e] Beep Boop Bop I am a Robot\n[f] ... can I be a doppelganger?")
    while True:
        print(user + "> ", end = "")
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
            final(27)
            state = -1
            return
        else:
            print(dm + "Please, select one of the aboves options")
def case31():
    global state
    
    print(dm + "Ugh fine. One of your parents is a genie")
    sleep(TIME)
    print(user + "[a] Yeah that works\n[b] Genies? Get that Will Smith shit out of my face\n")
    while True:
        print(user + "> ", end = "")
        choise = input()
        if choise == 'a':
            print(dm + "You are a Genasi!")
            sleep(TIME)
            print(user + "Let's Captain Planet this shit")
            state = 39
            return
        elif choise == 'b':
            state = 40
            return
        else:
            print(dm + "Please, select one of the aboves options")
def case32():
    global state

    print(dm + "Is Mountain Gnome ok for you?")
    sleep(1)
    print(user + "[a] Yeah!\n[b] FORGET THE TOYS WE MUST GO DEEPER\n")
    while True:
        print(user + "> ", end = "")
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
            print(dm + "Please, select one of the aboves options")
def case33():
    global state

    print(dm + "What? Fine. What's the problem?")
    sleep(1)
    print(user + "[a] I wanted to be Dark and Brooding\n[b] Aren't Elves Faeries? Make me goddamn weird and Fey\n[c] When i said Elf I meant like Mermaids\n[d] Can i be only KIND OF Elf-y?")
    while True:
        print(user + "> ", end = "")
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
            print(dm + "Please, select one of the aboves options")
def case34():
    global state
    
    print(dm + "So, are you hardier like the hills, or stronger like stone?")
    sleep(1)
    print(user + "[a] Hardy n Hilly!\n[b] Stone is Strength!\n[c] Neither, I'm angry and kind of a asshole\n")
    while True:
        print(user + "> ", end = "")
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
            print(dm + "Please, select one of the aboves options")
def case35():
    global state
    
    print(dm + "Cool, we actually have those if you picked that path earlier in yo edgelord")
    sleep(1)
    print(user + "[a] I'm quick and lithe, like an elf but DARK\n[b] I'm strong but instead of cheery dwarfness you got mean dwarfness\n[c] I was once holly but now I've FALLEN FROM GRACE\n")
    while True:
        print(user + "> ", end = "")
        choise = input()
        if choise == 'a':
            state = 41
            return
        elif choise == 'b':
            #Final 34
            final(34)
            state = -1
            return
        elif choise == 'c':
            #Final 35
            final(35)
            state = -1
            return
        else:
            print(dm + "Please, select one of the aboves options")
def case36():
    global state
    
    print(dm + "Right. Sorry. What is power to you?")
    sleep(1)
    print(user + "[a] Strength\n[b] Intellect\n")
    while True:
        print(user + "> ", end = "")
        choise = input()
        if choise == 'a':
            state = 42
            return
        elif choise == 'b':
            state = 43
            return
        else:
            print(dm + "Please, select one of the aboves options")
def case37():
    global state

    print(dm + "Is Aasimar ok for you?")
    sleep(1)
    print(user + "[a] Fuck off Tieflings!\n[b] Yeah!\n")
    while True:
        print(user + "> ", end = "")
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
            print(dm + "Please, select one of the aboves options")
def case38():
    global state
    
    print(dm + "Is Triton ok for you?")
    sleep(1)
    print(user + "[a] Wait, can I do this but more Elf-y?\n[b] Yeah!\n")
    while True:
        print(user + "> ", end = "")
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
            print(dm + "Please, select one of the aboves options")
def case39():
    global state
    
    print(dm + "Genies are elemental, so pick an element")
    sleep(1)
    print(user + "[a] Well, there's only one REAL choise...\n[b] Rock Hard baby\n[c] We all float down here\n[d] Actually I wanted to be REAL Aquaman")
    while True:
        print(user + "> ", end = "")
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
            print(dm + "Please, select one of the aboves options")
def case40():
    global state
        
    print(dm + "Seriously? How about multiverse dwelling psionic plane hoppers?")
    sleep(1)
    print(user + "[a] Okay, that's pretty fucking out there\n[b] That's just ugly elves with mind powers")
    while True:
        print(user + "> ", end = "")
        choise = input()
        if choise == 'a':
            print(dm + " You are a Gith")
            sleep(1)
            print(user + "Alright so I can explode heads with my mind right?")
            state = 45
            return
        elif choise == 'b':
            state = 46
            return
        else:
            print(dm + "Please, select one of the aboves options")
def case41():
    global state

    print(dm + "Is Drow ok for you?")
    sleep(1)
    print(user + "[a] Yeah!\n[b] I SAID DARK AND BROODING\n")
    while True:
        print(user + "> ", end = "")
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
            print(dm + "Please, select one of the aboves options")
def case42():
    global state

    print(dm + "Surprise attacks, or face the enemy hear on because you're not a coward")
    sleep(1)
    print(user + "[a] Face them head on, I'm not a coward!\n[b] Ambushes aren't cowardly, I'm just lazy\n")
    while True:
        print(user + "> ", end = "")
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
            print(dm + "Please, select one of the aboves options")
def case43():
    global state
    
    print(dm + "But a bit of strength is needed too right? To conquer?")
    sleep(1)
    print(user + "[a] Deception os the ultimate weapon\n[b] Tactical prowess marks a keen mind\n")
    while True:
        print(user + "> ", end = "")
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
            print(dm + "Please, select one of the aboves options")
def case44():
    global state
    
    print(dm + "More choises! What kind of angel?")
    sleep(1)
    print(user + "[a] Oh I wanna ve an angel but not like goody two shoes A BAD ANGEL\n[b] You know, light, goodness, yadda yadda\n[c] The path of the righteous man is beset on all sides by the inequities of the selfish and the tyranny of evil men. Blessed is he, who in the name of charity and good will, shepherds the weak through the valley of darkness, for he is truly his brother's keeper and the finder of lost children. And I will strike down upon thee with great vengeance and furious anger those who would attempt to poison and destroy my brothers. And you will know my name is the Lord when I lay my vengeance upon thee.\n")
    while True:
        print(user + "> ", end = "")
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
            print(dm + "Please, select one of the aboves options")
def case45():
    global state
    
    print(dm + "Not quite. Anyways Gith ccome in two flavors")
    sleep(1)
    print(user + "[a] WE ARE INMORTAL WE ARE CONQUERERS WE ARE GITH\n[b] Zen as fuck Kung Fu as Fuck Forge Chaos into Reallity\n")
    while True:
        print(user + "> ", end = "")
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
            print(dm + "Please, select one of the aboves options")
def case46():
    global state
        
    print(dm + "Blue hairless vulcan perfectionists? Like, this isn't DnD anymore")
    sleep(1)
    print(user + "[a] Fine, you got me\n[b] Vulcans are just spac elves. These fuckers just milktoast af\n")
    while True:
        print(user + "> ", end = "")
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
            print(dm + "Please, select one of the aboves options")
def case47():
    global state
        
    print(dm + "Is Orc ok for you?")
    sleep(1)
    print(user + "[a] Yeah!\n[b] Wait, what's this Intelligene penalty? I don't want to be stupid, can I backpedal a bot and be a bit more heroic?\n")
    while True:
        print(user + "> ", end = "")
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
            print(dm + "Please, select one of the aboves options")
def case48():
    global state
        
    print(dm + "Yup! Do you want to go part of the way, or all the way?")
    sleep(1)
    print(user + "[a] Oh, Lets go 100% monster\n[b] Uh, just give me a touch, just enough to make it nuanced\n")
    while True:
        print(user + "> ", end = "")
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
            print(dm + "Please, select one of the aboves options")
def case49():
    global state
        
    print(dm + "OKAY YOU HAVE TENTACLES AND MUTATIONS AND YOU'RE LITERALLY A MAD SCIENCE EXPERIMENT")
    sleep(1)
    print(user + "[a] This is the shit I'm talking about [b] No, I want to be mysterious")
    while True:
        print(user + "> ", end = "")
        choise = input()
        if choise == 'a':
            #Final 52
            final(52)
            return
        elif choise == 'b':
            #Final 53
            final(53)
            state = -1
            return
        else:
            print(dm + "Please, select one of the aboves options")
def case50():
    global state
        
    print(dm + "Big version or Small Version?")
    sleep(1)
    print(user + "[a] Big\n[b] Small\n")
    while True:
        print(user + "> ", end = "")
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
            print(dm + "Please, select one of the aboves options")

def final(f):
    if f == 1:
        print(dm + "You don't wanna play D&D, you want to play something else")
        sleep(TIME)
        print(user + "Elves are dumb lets be vampires n shit")
        sleep(TIME)
        print(dm + "And now we are playing Vampyre I hope you're happy")
    elif f == 2:
        print(dm + "Congratulations! You are a Human!")
    elif f == 3:
        print(dm + "Congratulations! You are a Half-Elf!")
    elif f == 4:
        print(dm + "Congratulations! You are a Half-Orc!")
    elif f == 5:
        print(dm + "Congratulations! You are a Firbolg!")
    elif f == 6:
        print(dm + "Congratulations! You are a Goliath!")
    elif f == 7:
        print(dm + "Congratulations! You are a Dragonborn!")
    elif f == 8:
        print(dm + "Congratulations! You are a Kobold!")
    elif f == 9:
        print(dm + "Congratulations! You are a Centaur!")
    elif f == 10:
        print(dm + "Congratulations! You are a Stout!")
    elif f == 11:
        print(dm + "Congratulations! You are a Lightfoot!")
    elif f == 12:
        print(dm + "Congratulations! You are a Forest Gnome!")
    elif f == 13:
        print(dm + "Congratulations! You are a Goblin!")
    elif f == 14:
        print(dm + "Congratulations! You are a High Elf!")
    elif f == 15:
        print(dm + "Congratulations! You are a Wood Elf!")
    elif f == 16:
        print(dm + "Congratulations! You are a Tiefling!")
    elif f == 17:
        print(dm + "Ugh, just get out")
    elif f == 18:
        print(dm + "Congratulations! You are a Lizardfork!")
    elif f == 19:
        print(dm + "Congratulations! You are a Yuan-Ti!")
    elif f == 20:
        print(dm + "Congratulations! You are a Tabaxi!")
    elif f == 21:
        print(dm + "Congratulations! You are a Minotaur!")
    elif f == 22:
        print(dm + "Congratulations! You are a Loxadon!")
    elif f == 23:
        print(dm + "Congratulations! You are a Shifter!")
    elif f == 24:
        print(dm + "Congratulations! You are a Aarakocra!")
    elif f == 25:
        print(dm + "Congratulations! You are a Kenku!")
    elif f == 26:
        print(dm + "Congratulations! You are a Warforged!")
    elif f == 27:
        print(dm + "Congratulations! You are a Changelings!")
    elif f == 28:
        print(dm + "Congratulations! You are a Mountain Gnome!")
    elif f == 29:
        print(dm + "Congratulations! You are a Deep Gnome!")
    elif f == 30:
        print(dm + "Congratulations! You are a Eladrin!")
    elif f == 31:
        print(dm + "Congratulations! You are a Sea Elf!")
    elif f == 32:
        print(dm + "Congratulations! You are a Hill Dwarf!")
    elif f == 33:
        print(dm + "Congratulations! You are a Mountain Dwarf!")
    elif f == 34:
        print(dm + "Congratulations! You are a Duegar!")
    elif f == 35:
        print(dm + "Congratulations! You are a Fallen!")
    elif f == 36:
        print(dm + "Congratulations! You are a Aasimar!")
    elif f == 37:
        print(dm + "Congratulations! You are a Triton!")
    elif f == 38:
        print(dm + "Congratulations! You are a Fire Genasi!")
    elif f == 39:
        print(dm + "Congratulations! You are a Eath Genasi!")
    elif f == 40:
        print(dm + "Congratulations! You are a Air Genasi!")
    elif f == 41:
        print(dm + "Congratulations! You are a Water Genasi!")
    elif f == 42:
        print(dm + "Congratulations! You are a Drow!")
    elif f == 43:
        print(dm + "Congratulations! You are a Shadar-Kai!")
    elif f == 44:
        print(dm + "Congratulations! You are a Bugbear!")
    elif f == 45:
        print(dm + "Congratulations! You are a Hobgoblin!")
    elif f == 46:
        print(dm + "Congratulations! You are a Protector!")
    elif f == 47:
        print(dm + "Congratulations! You are a Scourge!")
    elif f == 48:
        print(dm + "Congratulations! You are a Githyanki!")
    elif f == 49:
        print(dm + "Congratulations! You are a Githzerai!")
    elif f == 50:
        print(dm + "Congratulations! You are a Vedalken!")
    elif f == 51:
        print(dm + "Congratulations! You are a Orc!")
    elif f == 52:
        print(dm + "Congratulations! You are a Simic Hybrid!")
    elif f == 53:
        print(dm + "Congratulations! You are a Kalashtar!")
        sleep(1)
        print(user + "... I don't know what this is")
        sleep(1)
        print(dm + "Neither do I. Also I'm banning you from my game")
        
switch = [case0,case1,case2,case3,case4,case5,case6,case7,case8,case9,
case10,case11,case12,case13,case14,case15,case16,case17,case18,case19,
case20,case21,case22,case23,case24,case25,case26,case27,case28,case29,
case30,case31,case32,case33,case34,case35,case36,case37,case38,case39,
case40,case41,case42,case43,case44,case45,case46,case47,case48,case49,
case50]

while state != -1:
    sleep(1)
    print()
    switch[state]()
