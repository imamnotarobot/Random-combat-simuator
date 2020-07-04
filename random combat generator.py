import random
health = 15
enemyhealth = 10

def start ():
    print ("combat start")
    print ()
    yourattack()

def yourattack ():
    global health
    global enemyhealth
    damage = (random.randint(1, 5))
    enemyhealth = enemyhealth - damage
    print()
    print("you did")
    print(damage)
    print("damage")

    print()
    print("the enemy has")
    print(enemyhealth)
    print("health remaining")
    print()
    
    if enemyhealth < 1:
        print("you win")
    else:
        enemyattack()

def enemyattack ():
    global health
    global enemyhealth
    enemydamage = (random.randint(1, 5))
    print("enemy did")
    print(enemydamage)
    print("damage")
    health = health - enemydamage
    print()
    print("you have")
    print(health)
    print("health remaining")

    if health < 1:
        print("you killed him")
    else:
        yourattack()

start()