import pygame as g
from random import randint

g.init()
screen = g.display.set_mode((450, 400))
g.display.set_caption("test mouse event")

g.display.flip()

while True:
    event = g.event.wait()

    if event.type == g.QUIT:
        exit("quit..")

    if event.type == g.MOUSEBUTTONDOWN:
        print("mouse press down", event.pos)
        mx, my = event.pos
        g.draw.circle(screen, (255, 255, 0), (mx, my), 50)
        g.display.update()
    elif event.type == g.MOUSEMOTION:
        print("mouse moving..")
        x, y = event.pos
        r = randint(0, 255)
        gg = randint(0, 255)
        b = randint(0, 255)
        g.draw.circle(screen, (r, gg, b), (x, y), 50)
        g.display.update()
