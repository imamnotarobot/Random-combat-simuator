from tkinter import *
from tkinter import messagebox
import random
import time

playerstarthealth = 60
enemystarthealth = 50
cash = 0
spunlock = False
skunlock = False
paperbuy = False
exp = False
expoints = 0
level = 0
medkitammnt = 0




def horsearmour():
    horse = messagebox.showinfo("error", "why do you want this?")

def poundland():
    poundlandwindow = Toplevel()
    moneycount = Message(poundlandwindow, text="you have " + str(cash) + " cash")
    poundlandmessage = Message(poundlandwindow, text="what do you want")
    poundlandbuybutton = Button(poundlandwindow, text="buy", command=poundlandbuyclick)
    poundlandexitbutton = Button(poundlandwindow, text="exit")
    poundlandmessage.grid(column=0, row=0)
    poundlandbuybutton.grid(column=0, row=2)
    poundlandexitbutton.grid(column=0, row=3)
    moneycount.grid(column=0, row=1)


def medkitbuy():
    global cash
    global medkitammnt

    if cash < 25:
        notenoughmk = messagebox.showinfo("error", "you don't have enough money to buy that")
    else:
        cash = cash - 25
        medkitammnt = medkitammnt + 1

def paperbuy():
    global playerstarthealth
    global cash
    global paperbuy
    global exp

    if cash < 1000:
        nocashpaper = messagebox.showinfo("error", "you don't have enough cash for that")
    else:
        playerstarthealth = playerstarthealth + 20
        cash = cash - 1000
        paperbuy = True
        exhealth = messagebox.showinfo("you unlocked extra armour", "health up by 20")
        if exp == False:
            time.sleep(1)
            expunlock = messagebox.showinfo("", "you unlocked the progression system")
            exp = True






def poundlandbuyclick():
    global medkitammnt
    global cash

    poundlandbuywindow = Toplevel()
    medkitbuybutton = Button(poundlandbuywindow, text="medkit", command=medkitbuy)
    paperbuybutton = Button(poundlandbuywindow, text="peice of paper", command=paperbuy)
    medkitcost = Message (poundlandbuywindow, text="heals 20 hp, costs £25")
    papercost = Message (poundlandbuywindow, text="does nothing, costs £1000")
    medkitbuybutton.grid(column=0, row=1)
    paperbuybutton.grid(column=0, row=2)
    medkitcost.grid(column=2, row=1)
    papercost.grid(column=2, row=2)

    if cash < 25:
        medkitbuybutton.config(state=DISABLED)
    else:
        medkitbuybutton.config(state=NORMAL)

    if cash < 1000:
        paperbuybutton.config(state=DISABLED)
    else:
        paperbuybutton.config(state=NORMAL)


def waitrose():
    waitrosewindow = Toplevel()
    moneycount = Message(waitrosewindow, text="you have " + str(cash) + " cash")
    waitrosemessage = Message(waitrosewindow, text="what brings you in today")
    waitrosebuybutton = Button(waitrosewindow, text="buy", command=waitrosebuyclick)
    waitroseexitbutton = Button(waitrosewindow, text="exit")
    waitrosemessage.grid(column=0, row=0)
    waitrosebuybutton.grid(column=0, row=2)
    waitroseexitbutton.grid(column=0, row=3)
    moneycount.grid(column=0, row=1, columnspan=3)


def skbuyclick():
    global skunlock
    global cash

    if cash < 150:
        notenoughsk = messagebox.showinfo("error", "you don't have enough money to buy that")

    elif skunlock == True:
        alreadysk = messagebox.showinfo("error", "you already have that")

    else:
        cash = cash - 150
        skunlock = True


def spbuyclick():
    global spunlock
    global cash

    if cash < 100:
        notenoughsp = messagebox.showinfo("error", "you don't have enough money to buy that")

    elif spunlock == True:
        alreadysk = messagebox.showinfo("error", "you already have that")

    else:
        cash = cash - 100
        spunlock = True


def waitrosebuyclick():
    global cash
    global spunlock
    global skunlock
    waitrosebuywindow = Toplevel()
    skbuy = Button(waitrosebuywindow, text="buy super kick", command=skbuyclick)
    spbuy = Button(waitrosebuywindow, text="buy super punch", command=spbuyclick)
    skcost = Message (waitrosebuywindow, text="deals 5-20 damage, costs £150")
    spcost = Message(waitrosebuywindow, text="deals 0-25 damage, costs £100")
    skbuy.grid(column=0, row=0)
    spbuy.grid(column=0, row=1)
    skcost.grid(column=1, row=0)
    spcost.grid(column=1, row=1)
    if cash < 100:
        spbuy.config(state=DISABLED)
    else:
        spbuy.config(state=NORMAL)

    if cash < 150:
        skbuy.config(state=DISABLED)
    else:
        skbuy.config(state=NORMAL)



def battlewincreate():
    global health
    global enemyhealth
    health = playerstarthealth
    enemyhealth = enemystarthealth
    root = Toplevel()

    def punch():
        global health
        global enemyhealth
        global cash
        global exp
        global expoints
        global level
        global enemystarthealth
        global playerstarthealth
        
        damage = (random.randint(5, 10))
        damagemessage = Message(root, text="you did " + str(damage) + " damage")
        damagemessage.grid(column=0, row=30)
        punchbutton.config(state=DISABLED)
        kickbutton.config(state=DISABLED)
        superkickbutton.config(state=DISABLED)
        superpunchbutton.config(state=DISABLED)
        enemyhealth = enemyhealth - damage
        if enemyhealth <= 0:
            youwinmesg = Message(root, text="you win")
            youwinmesg.grid(column=0, row=40)
            cash = cash + 50
            print(cash)
            punchbutton.config(state=DISABLED)
            kickbutton.config(state=DISABLED)
            superkickbutton.config(state=DISABLED)
            superpunchbutton.config(state=DISABLED)
            if exp == True:
                expoints = expoints + 50
                if expoints == 100:
                    levelup = messagebox.showinfo("", "level up")
                    level = level + 1
                    enemystarthealth = enemystarthealth + 25
                    playerstarthealth = playerstarthealth + 24
        else:
            enemydamagemsg()

    def kick():
        global health
        global enemyhealth
        global cash
        global exp
        global expoints
        global level
        global enemystarthealth
        global playerstarthealth
        
        damage = (random.randint(0, 15))
        damagemessage = Message(root, text="you did " + str(damage) + " damage")
        damagemessage.grid(column=0, row=30)
        punchbutton.config(state=DISABLED)
        kickbutton.config(state=DISABLED)
        superkickbutton.config(state=DISABLED)
        superpunchbutton.config(state=DISABLED)
        enemyhealth = enemyhealth - damage
        enemydamagemsg()
        if enemyhealth <= 0:
            youwinmesg = Message(root, text="you win")
            youwinmesg.grid(column=0, row=5)
            cash = cash + 50
            punchbutton.config(state=DISABLED)
            kickbutton.config(state=DISABLED)
            superkickbutton.config(state=DISABLED)
            superpunchbutton.config(state=DISABLED)
            if exp == True:
                expoints = expoints + 50
                if expoints == 100:
                    levelup = messagebox.showinfo("", "level up")
                    level = level + 1
                    enemystarthealth = enemystarthealth + 25
                    playerstarthealth = playerstarthealth + 24
        else:
            enemydamagemsg()

    def superkick():
        global health
        global enemyhealth
        global skunlock
        global cash
        global health
        global enemyhealth
        global cash
        global exp
        global expoints
        global level
        global enemystarthealth
        global playerstarthealth
        
        damage = (random.randint(5, 20))
        damagemessage = Message(root, text="you did " + str(damage) + " damage")
        damagemessage.grid(column=0, row=30)
        punchbutton.config(state=DISABLED)
        kickbutton.config(state=DISABLED)
        superkickbutton.config(state=DISABLED)
        superpunchbutton.config(state=DISABLED)
        skunlock = False
        enemyhealth = enemyhealth - damage
        enemydamagemsg()
        if enemyhealth <= 0:
            youwinmesg = Message(root, text="you win")
            youwinmesg.grid(column=0, row=5)
            cash = cash + 50
            punchbutton.config(state=DISABLED)
            kickbutton.config(state=DISABLED)
            superkickbutton.config(state=DISABLED)
            superpunchbutton.config(state=DISABLED)
            if exp == True:
                expoints = expoints + 50
                if expoints == 100:
                    levelup = messagebox.showinfo("", "level up")
                    level = level + 1
                    enemystarthealth = enemystarthealth + 25
                    playerstarthealth = playerstarthealth + 24
                    expoints = 0
        else:
            enemydamagemsg()

    def superpunch():
        global health
        global enemyhealth
        global spunlock
        global cash
        global health
        global enemyhealth
        global cash
        global exp
        global expoints
        global level
        global enemystarthealth
        global playerstarthealth
        
        damage = (random.randint(5, 20))
        damagemessage = Message(root, text="you did " + str(damage) + " damage")
        damagemessage.grid(column=0, row=30)
        punchbutton.config(state=DISABLED)
        kickbutton.config(state=DISABLED)
        superkickbutton.config(state=DISABLED)
        superpunchbutton.config(state=DISABLED)
        enemyhealth = enemyhealth - damage
        enemydamagemsg()
        if enemyhealth <= 0:
            youwinmesg = Message(root, text="you win")
            youwinmesg.grid(column=0, row=5)
            cash = cash + 50
            punchbutton.config(state=DISABLED)
            kickbutton.config(state=DISABLED)
            superkickbutton.config(state=DISABLED)
            superpunchbutton.config(state=DISABLED)
            if exp == True:
                expoints = expoints + 50
                if expoints == 100:
                    levelup = messagebox.showinfo("", "level up")
                    level = level + 1
                    enemystarthealth = enemystarthealth + 25
                    playerstarthealth = playerstarthealth + 24
                    expoints = 0
        else:
            enemydamagemsg()

    def heal():
        global medkitammnt
        global health

        if medkitammnt >= 1:
            medkitammnt = medkitammnt - 1
            health = health + 20
            medkituse = Message(root, text="you used a medkit and restored 20 health")
            medkituse.grid(column=0, row=30)
            enemydamagemsg()
        else:
            medkitzero = Message(root, text="you don't have any medkits")
            medkitzero.grid(column=0, row=30)
            enemydamagemsg()



    def enemydamagemsg():
        enmyhlthammntmsg = Message(root, text="enemy has " + str(enemyhealth) + " health remaining")
        enmyhlthammntmsg.grid(column=0, row=31)
        enemyattack()

    def enemyattack():
        global health
        global enemyhealth
        global medkitammnt
        youloosemsg = Message(root, text="you loose")
        enemydamage = (random.randint(0, 15))
        health = health - enemydamage
        enemydamagemessage = Message(root, text="enemy did " + str(enemydamage) + " damage")
        youhealthmsg = Message(root, text="you have " + str(health) + " remaining")
        enemydamagemessage.grid(column=1, row=30)
        youhealthmsg.grid(column=1, row=31)
        if health <= 0:
            youloosemsg.grid(row=10, column=0)
            punchbutton.config(state=DISABLED)
            kickbutton.config(state=DISABLED)
            superkickbutton.config(state=DISABLED)
            superpunchbutton.config(state=DISABLED)
        else:
            punchbutton.config(state=NORMAL)
            kickbutton.config(state=NORMAL)

            if skunlock == True:
                superkickbutton.config(state=NORMAL)
            else:
                superkickbutton.config(state=DISABLED)

            if spunlock == True:
                superpunchbutton.config(state=NORMAL)
            else:
                superpunchbutton.config(state=DISABLED)

    punchbutton = Button(root, text="punch", command=punch)
    kickbutton = Button(root, text="kick", command=kick)
    superpunchbutton = Button(root, text="super punch", command=superpunch)
    superkickbutton = Button(root, text="super kick", command=superkick)
    medkitbutton =  Button(root, text="heal", command=heal)
    kickbutton.grid(column=1, row=0)
    punchbutton.grid(column=0, row=0)
    superkickbutton.grid(column=1, row=1)
    superpunchbutton.grid(column=0, row=1)
    medkitbutton.grid(column=0, row=2)

    if skunlock == False:
        superkickbutton.config(state=DISABLED)
    else:
        superkickbutton.config(state=NORMAL)

    if spunlock == False:
        superpunchbutton.config(state=DISABLED)
    else:
        superpunchbutton.config(state=NORMAL)

    if medkitammnt < 1:
        medkitbutton.config(state=DISABLED)


hubworld = Tk()
welcome = Message(hubworld, text="welcome to village city")
combatbutton = Button(hubworld, text="to battle", command=battlewincreate)
waitrosebutton = Button(hubworld, text="to waitrose", command=waitrose)
poundlandbutton = Button(hubworld, text="to poundland", command=poundland)
horsebutton = Button(hubworld, text="horse armour", command= horsearmour)
combatbutton.grid(column=0, row=2)
waitrosebutton.grid(column=0, row=3)
poundlandbutton.grid(column=0, row=4)
horsebutton.grid(column=0, row=5)
welcome.grid(column=0, row=0)


                       
hubworld.mainloop()
