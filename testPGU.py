# здесь подключаются модули
import pygame
import sys
import PGU

# здесь определяются константы,
# классы и функции
FPS = 60

# здесь происходит инициация,
# создание объектов
pygame.init()
surf=pygame.display.set_mode((600, 400))
clock = pygame.time.Clock()

# если надо до цикла отобразить
# какие-то объекты, обновляем экран
pygame.display.update()
pic=pygame.image.load('backsp.png')
#pic.set_colorkey((255, 255, 255))
testButton=PGU.pgButton(surf,(50,50),200,200,pict=pic,function=print,args=["dsdf"],)
textButton=PGU.pgButton(surf,(300,300),40,40,text="Hello",function=print,args=["dsdf"],changeXYWH=True,font=pygame.font.SysFont('arial', 30),backGround=(100,0,100))
# главный цикл
while True:

    # задержка
    clock.tick(FPS)

    # цикл обработки событий
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()

    # --------
    # изменение объектов
    # --------

    # обновление экрана
    surf.fill((255,255,255))
    testButton.blit()
    textButton.blit()
    pygame.display.update()