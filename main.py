from pygame import *

try:
    class Fx():
        def __init__(self):
            self.numoffxs = int(input("\nΠόσες συναρτήσεις θέλετε να σχεδιάσετε;"))
            self.factors = {"angle": [], "degree": [], "add": []}
            for i in range(self.numoffxs):
                self.factors["angle"].append(float(input("\nΕισαγάγετε τον συντελεστή του x: ")))
                self.factors["degree"].append(float(input("Εισαγάγετε τον εκθέτη του x: ")))
                self.factors["add"].append((float(input("Εισγάγετε τον αριθμό που θέλετε να προσθέσετε στον τύπο της συνάρτησης: "))))
    fxobj = Fx()
    w = display.set_mode((1500, 750))
    display.set_caption("Cf")
    x = 0
    y = 375
    xx = []
    for i in range(1500):
        xx.append(rect.Rect(x, y, 1, 1))
        x += 1
    x = 750
    y = 0
    yy = []
    for i in range(750):
        yy.append(rect.Rect(x, y, 1, 1))
        y += 1
    funclist = []
    for i in range(fxobj.numoffxs):
        fx = []
        x = -750
        y = 750
        for j in range(1500):
            fx.append(rect.Rect(x+750, y+375, 1, 1))
            x += 1
            y = - (((fxobj.factors["angle"][i] * pow(x, fxobj.factors["degree"][i])) + fxobj.factors["add"][i]) / 500)
        funclist.append(fx)
    clock = time.Clock()
    close = False
    while not close:
        w.fill((255, 255, 255))
        for i in event.get():
            if i.type == QUIT:
                close = True
        for i in xx:
            draw.rect(w, (0, 0, 0), i)
        for i in yy:
            draw.rect(w, (0, 0, 0), i)
        for i in funclist:
            for j in i:
                draw.rect(w, (0, 0, 0), j)
        display.update()
        clock.tick(60)
except:
    print("Άκυρη είσοδος!")