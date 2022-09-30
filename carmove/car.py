import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((640, 640))
fpsClock = pygame.time.Clock()  # 创建时钟对象
pygame.display.set_caption('Car')
carImg = pygame.image.load('car.png')
bgImg = pygame.image.load('background.png')
WHITE = (255, 255, 255)
carx = 0
cary = 0
FPS = 60  # 初始刷新率设置为60帧


def pause():  # 定义暂停函数
    is_pause = True
    while is_pause:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                quit()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_p]:
                is_pause = False
            if keys[pygame.K_ESCAPE]:
                pygame.quit()
                quit()

        pygame.display.update()
        fpsClock.tick(5)


running = True
while running:  # 主循环
    screen.blit(bgImg, (0, 0))  # 小车起始位置
    carx += 1
    cary += 1
    if carx == 550:  # 当小车到达窗口右下角，小车重置到左上角
        carx = 0
        cary = 0
    screen.blit(carImg, (carx, cary))
    fpsClock.tick(FPS)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            quit()

        key = pygame.key.get_pressed()
        if key[pygame.K_UP]:  # 按UP键加速
            FPS += 10
            if FPS > 90:
                FPS = 90  # 设置刷新率上限为90
        if key[pygame.K_DOWN]:  # 按DOWN键减速
            FPS -= 10
            if FPS < 30:
                FPS = 30  # 设置刷新率下限为30
        if key[pygame.K_ESCAPE]:  # 按ESCAPE键结束程序
            running = False
        if key[pygame.K_SPACE]:  # 按SPACE键暂停小车
            pause()

    pygame.display.update()
