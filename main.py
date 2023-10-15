from pygame import *

try:
    angle = float(input("\nΕισαγάγετε τον συντελεστή του x: "))
    degree = float(input("Εισαγάγετε τον εκθέτη του x: "))
    add = (float(input("Εισγάγετε τον αριθμό που θέλετε να προσθέσετε στον τύπο της συνάρτησης: ")))
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
    fx = []
    x = -750
    y = 750
    for i in range(1500):
        fx.append(rect.Rect(x+750, y+375, 1, 1))
        x += 1
        y = - ((angle * pow(x, degree))/500 + add)
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
        for i in fx:
            draw.rect(w, (0, 0, 0), i)
        display.update()
        clock.tick(60)
except:
    pass