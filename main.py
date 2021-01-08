import pygame
import ball as b
import app as a
pygame.init() 

SCREENWIDTH = 1000
SCREENHEIGHT = 1000

win = a.Main(SCREENWIDTH, SCREENHEIGHT, (0,0,0), "Bouncing Ball")
win.setDisplay()

b1 = b.Ball(30, (255,255,0), SCREENWIDTH/2, SCREENHEIGHT/2, 1/75 , 1)
b2 = b.Ball(50, (0,255,255), SCREENWIDTH/4, SCREENHEIGHT/2, 1/25, 3)
b3 = b.Ball(20, (255,0,255), 3*SCREENWIDTH/4, SCREENHEIGHT/2, 1/100, 0.75)

while win.run:
    pygame.time.delay(12)

    win.bgdisplay()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            win.run = False
        elif event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            b1.addForce(pos)
            b2.addForce(pos)
            b3.addForce(pos)

    b1.draw(win.screen, win.width, win.height)
    b2.draw(win.screen, win.width, win.height)
    b3.draw(win.screen, win.width, win.height)


    pygame.display.update()

pygame.quit()