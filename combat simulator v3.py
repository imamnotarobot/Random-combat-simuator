import random
import time
skunlock = False
spunlock = False
medkitammnt = 1
cash = 0
health = 50
enemyhealth = 50

def hubworld ():
    global health
    global cash

    print ("welcome to village city")
    print ("you have £",cash)
    print ("where would you like to go?")
    print ("to waitrose")
    print ("to battle")
    print ("to poundland")
    print ("to home")
    print ("please type your answer")
    locationqst = input ()

    if locationqst == "waitrose":
        print ("you walk to waitrose")
        waitrose()
    elif locationqst == "poundland":
        print ("you walk to poundland")
        poundland ()
    elif locationqst == "battle":
        print ("you walk into the forrest to find enemies")
        print ("...")
        time.sleep(2)
        battle()
    elif locationqst == "home":
        print ("you go home and rest")
        if health < 50:
            health = 50
            print ("health restored to 50")
            hubworld()
    else:
        print ("that was not on option.")
        hubworld()


def waitrose ():
    
    global cash
    global spunlock
    global skunlock
    
    print ("what brings you in today")
    print ()
    print ()
    print ("buy")
    print ("exit")
    print ()
    print ("please type your answer")
    waitrosechoice = input ()

    if waitrosechoice == "buy":
        print ()
        if skunlock == False:
            print ("super kick: 150 cashpounds")
            print ("deals 5-20 damage. one use")
        if spunlock == False:
            print ()
            print ("super punch 100 cashpounds")
            print ("deals 0 - 25 damage. one-time purchase")
            print ("what would you like to buy?")
        waitrosebuy = input()

        if waitrosebuy == "super punch":
            if cash >= 100:
                spunlock = True
                cash = cash - 100
                print("you got the super punch")
                waitrose()
            if cash < 100:
                print("you dont have enough cash to buy that")
                print(cash)
                waitrose()

        elif waitrosebuy == "super kick":
            if cash >= 150:
                skunlock = True
                cash = cash - 150
                print("you got the super kick")
                waitrose()
            if cash < 150:
                print("you dont have enough cash to buy that")
                print(cash)
                waitrose()

        else:
            print("that wasn't an option")
            waitrose()
    elif waitrosechoice == "exit":
        print ("thank you for shopping at waitrose")
        hubworld ()
    else:
        print("that was not on option.")
        waitrose()

def poundland ():
    global cash
    global medkitammnt

    print ("what do you want")
    print ()
    print ("buy")
    print ("exit")
    print ("type your answer")
    poundlandchoice1 = input ()

    if poundlandchoice1 == "exit":
        print ("you left poundland")
        print ()
        hubworld ()

    if poundlandchoice1 == "buy":
        print ()
        print ("medkit: 25 cashpounds")
        print ("heals 20 health")
        print ()
        print ("piece of paper: 1000 cashpounds")
        print ("does nothing")
        print ("what would you like to buy")
        poundlandchoice2 = input ()

        if poundlandchoice2 == "medkit":
            if cash >= 25:
                medkitammnt = medkitammnt + 1
                print ("you got the medkit")
                poundland ()

            if cash < 25:
                print ("you don't have enough money for that")
                poundland ()
        elif poundlandchoice2 == "paper":
            if cash < 1000:
                print ("you don't have enough money for that")
            else:
                cash = cash - 1000
                print("you got a piece of paper")
                poundland()


def battle():
    print("combat start")
    print()
    yourattack()


def yourattack():
    global health
    global enemyhealth
    global cash
    global skunlock
    global spunlock
    global medkitammnt

    print ("do you want to punch (5-10 damage) or kick (0-15 damage)")
    if skunlock == True:
        print ("or super kick")
    if spunlock == True:
        print ("or super punch")
    if medkitammnt >= 1:
        print ("or heal")
    attackchoice = input()

    if attackchoice == "punch":
        damage = (random.randint(5, 10))
        enemyhealth = enemyhealth - damage
        print()
        print("you did")
        print(damage)
        print("damage")

    elif attackchoice == "kick":
        damage = (random.randint(0, 15))
        enemyhealth = enemyhealth - damage
        print()
        print("you did")
        print(damage)
        print("damage")

    elif attackchoice == "super punch":
        if spunlock == True:
            damage = (random.randint(0, 25))
            enemyhealth = enemyhealth - damage
            print()
            print("you did")
            print(damage)
            print("damage")
        elif spunlock == False:
            print ("you haven't brought that yet")
            yourattack ()

    elif attackchoice == "super kick":
        if skunlock == True:
            damage = (random.randint(5, 20))
            enemyhealth = enemyhealth - damage
            print()
            print("you did")
            print(damage)
            print("damage")
            skunlock = False
        elif skunlock == False:
            print("you haven't brought that yet")
            yourattack()

    elif attackchoice == "heal":
        if medkitammnt >= 1:
            print ("you recovered  20 hp")
            health = health + 20
            medkitammnt = medkitammnt - 1
        elif medkitammnt < 0:
            print ("you can't do that")
            yourattack()


    print()
    print("the enemy has")
    print(enemyhealth)
    print("health remaining")
    print()

    if enemyhealth < 1:
        print("you win")
        print()
        print("you got 50 cashpounds")
        cash = cash + 50
        hubworld()
    else:
        enemyattack()


def enemyattack():
    global health
    global enemyhealth
    global cashpounds
    enemydamage = (random.randint(5, 10))
    time.sleep(2)
    print("enemy did")
    print(enemydamage)
    print("damage")
    health = health - enemydamage
    print()
    print("you have")
    print(health)
    print("health remaining")

    if health < 1:
        print ("he killed you")
        print ("game over")

    else:
        yourattack()
hubworld ()