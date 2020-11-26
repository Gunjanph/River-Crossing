import pygame
pygame.init()

win = pygame.display.set_mode((800, 625))

pygame.display.set_caption("River Crossing Competiton Game")

win.fill((0,0,225))
ls = pygame.image.load('ls.png')
rs = pygame.image.load('rs.png')
rock = pygame.image.load('rock.png')
font2 = pygame.font.Font('freesansbold.ttf',24)
def reset():
    global x1
    x1 = 400
    global y1
    y1 = 10
    global x2
    x2 = 400
    global y2
    y2 = 625
    global count
    count += 1
    global vel
    vel += 4

def finish():
    global waterf1
    waterf1=0
    global waterf2
    waterf2=0
    global waterf3
    waterf3=0
    global waterf4
    waterf4=0
    global waterf5
    waterf5=0
    global waterf6
    waterf6=0
    global surfacef1
    surfacef1=0
    global surfacef2
    surfacef2=0
    global surfacef3
    surfacef3=0
    global surfacef4
    surfacef4=0
    global surfacef5
    surfacef5=0

def cols(player1,player2,SX,SY):
    if (SX <= player1 <= (SX+16) and SY <= player2 <= (SY +16) ):
        reset() 
        finish()
    elif (SX <= (player1+16) <= (SX+16) and SY <= (player2+16) <= (SY +16)):
        reset()
        finish()
    elif (SX <= (player1+16) <= (SX+16) and SY <= (player2) <= (SY +16)):
        reset()
        finish()
    elif (SX <= (player1) <= (SX+16) and SY <= (player2+16) <= (SY +16)):
        reset() 
        finish()

def colM(player1,player2,MX,MY):
    if (MX <= player1 <= (MX+64) and MY <= player2 <= (MY +64) ):
        reset()
        finish()
    elif (MX <= (player1+16) <= (MX+64) and MY <= (player2+16) <= (MY +64)):
        reset()
        finish()
    elif (MX <= (player1+16) <= (MX+64) and MY <= (player2) <= (MY +64)):
        reset()
        finish()
    elif (MX <= (player1) <= (MX+64) and MY <= (player2+16) <= (MY +64)):
        reset()
        finish()

run = True
while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        x1 -= vel
    if keys[pygame.K_RIGHT]:
        x1 += vel
    if keys[pygame.K_UP]:
        y1 -= vel	
    if keys[pygame.K_DOWN]:
        y1 += vel

    win.fill((0, 225, 225))
 #   pygame.draw.circle(win, (225, 0, 0), (x1, y1), radius, thickness1)
  #  pygame.draw.circle(win, (225, 0, 0), (x1, y1), radius, thickness1)
    pygame.draw.rect(win, (200, 190, 140), (0,100, 800, 25))
    pygame.draw.rect(win, (200, 190, 140), (0,200, 800, 25))
    pygame.draw.rect(win, (200, 190, 140), (0,300, 800, 25))
    pygame.draw.rect(win, (200, 190, 140), (0,400, 800, 25))
    pygame.draw.rect(win, (200, 190, 140), (0,500, 800, 25))
    pygame.draw.rect(win, (200, 190, 140), (0,600, 800, 25))
    pygame.draw.rect(win, (200, 190, 140), (0,0, 800, 25))

    if waterf1 == 0:
        if y1 > 100:
            waterf1 = 1
            score1 += 10
    if waterf2 == 0:
        if y1 > 200:
            waterf2 = 1
            score1 += 10
    if waterf3 == 0:
        if y1 > 300:
            waterf3 = 1
            score1 += 10
    if waterf4 == 0:
        if y1 > 400:
            waterf4 = 1
            score1 += 10
    if waterf5 == 0:
        if y1 > 500:
            waterf5 = 1
            score1 += 10
    if waterf6 == 0:
        if y1 > 600:
            waterf6 = 1
            score1 += 10
    if surfacef1 == 0:
        if y1 > 125:
            surfacef1 = 1
            score1 += 5
    if surfacef2 == 0:
        if y1 > 225:
            surfacef2 = 1
            score1 += 5
    if surfacef3 == 0:
        if y1 > 325:
            surfacef3 = 1
            score1 += 5
    if surfacef4 == 0:
        if y1 > 425:
            surfacef4 = 1
            score1 += 5
    if surfacef5 == 0:
        if y1 > 525:
            surfacef5 = 1
            score1 += 5

#    font2 = pygame.font.Font('freesansbold.ttf',24)
    msg = font2.render("START" ,True ,(0 , 0 , 0))
    win.blit(msg, (360,0))
    msg = font2.render("END" ,True ,(0 , 0 , 0))
    win.blit(msg, (375,600))
    
    xb1 += vel
    if xb1 >= 775:
        xb1 = 15
    xb2 += vel
    if xb2 >= 775:
        xb2 = 15
    xb3 -= vel
    if xb3 <= 15:
        xb3 = 775
    xb4 -= vel
    if xb4 <= 15:
        xb4 = 775
    win.blit(ls , (xb1,yb1))
    win.blit(rs , (xb4,yb2))
    win.blit(ls , (xb1,yb3))
    win.blit(ls , (xb2,yb4))
    win.blit(rs , (xb3,yb4))
    win.blit(ls , (xb1,yb5))
    win.blit(rs , (xb4,yb6))
    win.blit(rock , (xr5,yr1))
    win.blit(rock , (xr3,yr2))
    win.blit(rock , (xr6,yr3))
    win.blit(rock , (xr2,yr3))
    win.blit(rock , (xr1,yr4))
    win.blit(rock , (xr4,yr5))
    if x1 >= 800:
        x1 = 800
    if x1 <= 0:
        x1 = 0
    if y1 <= 0:
        y1 = 0
    if y1 >= 625:
        y1 = 625


    keys = pygame.key.get_pressed()
    if keys[pygame.K_q]:
    	pygame.quit()
    if keys[pygame.K_a]:
        x2 -= vel
    if keys[pygame.K_d]:
        x2 += vel
    if keys[pygame.K_w]:
        y2 -= vel
    if keys[pygame.K_s]:
        y2 += vel

    if waterf1 == 0:
        if y2 < 535:
            waterf1 = 1
            score2 += 10
    if waterf2 == 0:
        if y2 < 435:
            waterf2 = 1
            score2 += 10
    if waterf3 == 0:
        if y2 < 335:
            waterf3 = 1
            score2 += 10
    if waterf4 == 0:
        if y2 < 235:
            waterf4 = 1
            score2 += 10
    if waterf5 == 0:
        if y2 < 135:
            waterf5 = 1
            score2 += 10
    if waterf6 == 0:
        if y2 < 35:
            waterf6 = 1
            score2 += 10
    if surfacef1 == 0:
        if y2 < 510:
            surfacef1 = 1
            score2 += 5
    if surfacef2 == 0:
        if y2 < 410:
            surfacef2 = 1
            score2 += 5
    if surfacef3 == 0:
        if y2 < 310:
            surfacef3 = 1
            score2 += 5
    if surfacef4 == 0:
        if y2 < 210:
            surfacef4 = 1
            score2 += 5
    if surfacef5 == 0:
        if y2 < 110:
            surfacef5 = 1
            score2 += 5


#    screen.fill((0, 0, 0))
    player1 = pygame.image.load('circle.png')
    win.blit(player1,(x1,y1))
    player2 = pygame.image.load('circle1.png')
    win.blit(player2,(x2,y2))
#    player1.fill((240,0,255))
#    player2.fill((225,0,0))
    pygame.display.update()


    if x2 >= 800:
        x2 = 800
    if x2 <= 0:
        x2 = 0
    if y2 <= 0:
        y2 = 0
    if y2 >= 625:
        y2 = 625

    if y1 == 610:
        reset()
        finish()

    if y2 == 15:
        reset()
        finish()
    
    colM(x1,y1,xb1,yb1)
    colM(x1,y1,xb4,yb2)
    colM(x1,y1,xb1,yb3)
    colM(x1,y1,xb2,yb4)
    colM(x1,y1,xb3,yb4)
    colM(x1,y1,xb1,yb5)
    colM(x1,y1,xb4,yb6)
    colM(x2,y2,xb1,yb1)
    colM(x2,y2,xb4,yb2)
    colM(x2,y2,xb1,yb3)
    colM(x2,y2,xb2,yb4)
    colM(x2,y2,xb3,yb4)
    colM(x2,y2,xb1,yb5)
    colM(x2,y2,xb4,yb6)
    cols(x1,y1,xr5,yr1)
    cols(x1,y1,xr3,yr2)
    cols(x1,y1,xr6,yr3)
    cols(x1,y1,xr2,yr3)
    cols(x1,y1,xr1,yr4)
    cols(x1,y1,xr4,yr5)
    cols(x2,y2,xr5,yr1)
    cols(x2,y2,xr3,yr2)
    cols(x2,y2,xr6,yr3)
    cols(x2,y2,xr2,yr3)
    cols(x2,y2,xr1,yr4)
    cols(x2,y2,xr4,yr5)

    if count == 0:
        t1p1 = (int)((pygame.time.get_ticks()) / 1000)
    if count == 1:
        t1p2 = (int)((pygame.time.get_ticks())/1000 - t1p1)
    if count == 2:
        t2p1 = (int)((pygame.time.get_ticks())/1000 - t1p1 - t1p2)
    if count == 3:
        t2p2 = (int)((pygame.time.get_ticks())/1000 - t1p1 - t1p2 - t2p1)

    msg = font2.render("SCORE 1: " +str(score1 - t1p1 - t2p1), True, (225, 0, 0))
    win.blit(msg, (0, 0))

    msg = font2.render("SCORE 2: " +str(score2 - t1p2 - t2p2), True, (225, 0, 0))
    win.blit(msg, (650, 0))


#    print (count)
    if count == 4:
        run = False
        result = True

while result:
    win.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            result = False
    if score1 >= score2:
        msg = font2.render("PLAYER 1 WINS",True ,(225,225,225))
        win.blit(msg,(300,300))
    else:
        msg = font2.render("PLAYER 2 WINS",True ,(225,225,225))
        win.blit(msg,(300,300))

    pygame.display.update()

pygame.quit()
