from tkinter import *
import random
import time

health = 50
enemyhealth = 50


def punch():
    global health
    global enemyhealth
    damage = (random.randint(5, 10))
    damagemessage = Message(root, text="you did " + str(damage) + " damage")
    damagemessage.grid(column=0, row=1)
    punchbutton.config(state=DISABLED)
    kickbutton.config(state=DISABLED)
    enemyhealth = enemyhealth - damage
    if enemyhealth <= 0:
        youwinmesg= Message(root, text="you win")
        youwinmesg.grid (column=0, row=5)
    else:
        enemydamagemsg()


def kick():
    global health
    global enemyhealth
    damage = (random.randint(0, 15))
    damagemessage = Message(root, text="you did " + str(damage) + " damage")
    damagemessage.grid(column=0, row=1)
    punchbutton.config(state=DISABLED)
    kickbutton.config(state=DISABLED)
    enemyhealth = enemyhealth - damage
    enemydamagemsg()

def enemydamagemsg():
    enmyhlthammntmsg= Message(root, text="enemy has " + str(enemyhealth) + " health remaining")
    enmyhlthammntmsg.grid(column=0, row=2)
    enemyattack()

def enemyattack():
    global health
    global enemyhealth
    youloosemsg = Message(root, text="you loose")
    enemydamage = (random.randint(0,15))
    health = health - enemydamage
    enemydamagemessage = Message(root, text="enemy did " + str(enemydamage) + " damage")
    youhealthmsg = Message(root, text="you have " + str(health) + " remaining")
    enemydamagemessage.grid(column=1, row=1)
    youhealthmsg.grid(column=1, row=2)
    if health <=0:
        youloosemsg.grid(row=10, column=0)
    else:
        punchbutton.config(state=NORMAL)
        kickbutton.config(state=NORMAL)






root = Tk()

punchbutton = Button(root, text="punch", command=punch)
kickbutton = Button (root, text="kick", command=kick)
kickbutton.grid (column=1, row=0)
punchbutton.grid(column=0, row=0)

root.mainloop()
