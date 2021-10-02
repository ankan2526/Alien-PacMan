import pygame,time,keyboard, random

pygame.init()

screen= pygame.display.set_mode((400,432))

pygame.display.set_caption("Alien_Run")

ball=pygame.image.load(r'alien.png')
enemy=pygame.image.load(r'military.png')
coin=pygame.image.load(r'coin.png')
background=pygame.image.load(r'bg.jpg')
px,py=2,2
d=1
ex=0
score=0
Highscore=0
font=pygame.font.Font('freesansbold.ttf',24)
text=font.render('Press "ENTER" to start!',True,(250,250,0),(255,0,0))
textrect=text.get_rect()
textrect.center=(200,416)
coinx,coiny=random.randint(10,360),random.randint(10,360)
st=0

try:
    Highscore = int(open("score").read())
except:
    file = open("score","w")
    file.write(str(0))
    file.close()
    Highscore = 0

posx,posy,dirx,diry=[],[],[1,1,-1,-1],[1,-1,-1,1]
for i in range(4):
    posx.append(random.randint(50,369))
    posy.append(random.randint(50,369))

running=True
while 1:
    screen.fill((205,0,255))
    screen.blit(background,(0,0))
    pygame.draw.line(screen,(50,180,0),(0,400),(400,400),4)
    pygame.draw.line(screen,(50,180,0),(0,0),(400,0),4)
    pygame.draw.line(screen,(50,180,0),(0,400),(0,0),4)
    pygame.draw.line(screen,(50,180,0),(398,0),(398,400),4)
    screen.blit(text,textrect)
    screen.blit(ball,(px,py))
    screen.blit(coin,(coinx,coiny))
    for i in range(4):
        screen.blit(enemy,(posx[i],posy[i]))

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            quit()
        
    pygame.display.update()
    if st==0:
        if keyboard.is_pressed('enter'):
            st=1
        else:
            continue
        
    text=font.render(f'Score: {score}  Highscore: {Highscore}',True,(250,250,0),(255,0,0))
    textrect=text.get_rect()
    textrect.center=(200,416)
    
    time.sleep(0.007)
    if keyboard.is_pressed('down'):
        d=4
    elif keyboard.is_pressed('left'):
        d=1
    elif keyboard.is_pressed('up'):
        d=3
    elif keyboard.is_pressed('right'):
        d=2

    if d==1 and px>=3:
        px-=2
    elif d==2 and px<=372:
        px+=2
    elif d==3 and py>=3:
        py-=2
    elif d==4 and py<=372:
        py+=2

    for i in range(4):
        if posx[i]<=3 and dirx[i]==-1:
            dirx[i]=1
        elif posx[i]>=372 and dirx[i]==1:
            dirx[i]=-1
        if posy[i]<=3 and diry[i]==-1:
            diry[i]=1
        elif posy[i]>=373 and diry[i]==1:
            diry[i]=-1
        posx[i]+=dirx[i]
        posy[i]+=diry[i]
        
        if abs(px-posx[i])<=18 and abs(py-posy[i])<=18:
            time.sleep(1)
            ex=1
            
    if abs(px-coinx)<=20 and abs(py-coiny)<=20:
        score+=10
        if score>Highscore:
            Highscore=score
            file = open("score","w")
            file.write(str(Highscore))
            file.close()
        coinx,coiny=random.randint(10,360),random.randint(10,360)
    if ex==1:
        score=0
        st=0
        posx,posy,dirx,diry=[],[],[1,1,-1,-1],[1,-1,-1,1]
        for i in range(4):
            posx.append(random.randint(50,369))
            posy.append(random.randint(50,369))
        px,py=2,2
        coinx,coiny=random.randint(10,360),random.randint(10,360)
        ex=0
        text=font.render('Press   "ENTER"   to  start!',True,(250,250,0),(255,0,0))
        textrect=text.get_rect()
        textrect.center=(200,416)
