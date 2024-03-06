import pygame, sys, math
from pygame.locals import*
pygame.init()

screen=pygame.display.set_mode((1000, 600))
img_palette=pygame.image.load("picture\Palette.png").convert_alpha()#更改標題旁圖標

pygame.display.set_caption("Painter")
pygame.display.set_icon(img_palette)

screen.fill((255,255,255))

red=(255,0,0)
orange=(255,123,0)
yellow=(255,255,0)
green=(0,255,0)
lightblue=(0,255,255)
blue=(0,0,255)
pink=(255,110,157)
purple=(255,0,255)
gray=(88,88,88)
black=(0,0,0)
white=(255,255,255)

colors=[red,orange,yellow,green,lightblue,blue,pink,purple,gray,black]
img_color=[red,orange,yellow,green,lightblue,blue,pink,purple,gray,black]#放圖檔
address=["picture\(255,0,0).png","picture\(255,123,0).png","picture\(255,255,0).png","picture\(0,255,0).png","picture\(0,255,255).png","picture\(0,0,255).png","picture\(255,110,157).png","picture\(255,0,255).png","picture\(88,88,88).png","picture\(0,0,0).png"]


decided_color=[white,black]
getcolor=black
pen_size=20

painting=False


def load_img():
    img_eraser=pygame.image.load("picture\eraser.png").convert_alpha()
    img_painter=pygame.image.load("picture\painter.png").convert_alpha()
    img_trash=pygame.image.load("picture\\trash.png").convert_alpha()#在python要表示\t要用\\t表示

    img_painter = pygame.transform.smoothscale(img_painter, (60, 60))#使圖像變為60*60
    img_eraser = pygame.transform.smoothscale(img_eraser, (61, 44))
    img_trash=pygame.transform.smoothscale(img_trash,(55,71))

    screen.blit(img_painter,(80,20))
    screen.blit(img_eraser,(80,100))
    screen.blit(img_trash,(80,500))

def load_color():
    for i in range (10):
        img_color[i]=pygame.image.load(address[i]).convert_alpha()        
        screen.blit(img_color[i],(10,60*i))



while True:
    load_img()
    load_color()
    
    for event in pygame.event.get():
        X,Y=pygame.mouse.get_pos()
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
            
        elif event.type==MOUSEBUTTONUP:
            painting=False
        elif event.type==MOUSEBUTTONDOWN:
            painting=True
            if event.button==4:
                if 2<=pen_size<=38:
                    pen_size=pen_size+2
                    print("筆刷大小=",pen_size)
            elif event.button==5:
                if 4<=int(pen_size)<=40:
                    pen_size=pen_size-2
                    print("筆刷大小=",pen_size)

            elif event.button==1:
                
                pygame.draw.circle(screen,getcolor,(X,Y),pen_size)

                y=math.floor(Y/60)
                #print(y) #偵錯
                if 10 <= X <=70 and 0+60*y <= Y <= 60+60*y:
                    del decided_color[1]
                    decided_color.append(colors[y])
                    getcolor=decided_color[1]
                    print(getcolor)

                elif  80 <= X <= 140 and 20 <= Y <= 80:#painter
                    getcolor=decided_color[1]
                    print(getcolor)
                elif  80 <= X <= 141 and 100 <= Y <= 144:#eraser
                    getcolor=decided_color[0]#white
                    print(getcolor)
                elif  80 <= X <= 135 and 500 <= Y <= 571:#trashcan
                    screen.fill(white)
                    print("clean")
                else:
                    pass

        elif event.type==MOUSEMOTION:
            if painting==True: 
                pygame.draw.circle(screen, getcolor, (X,Y), pen_size)
                pygame.display.update()

    pygame.display.update()





