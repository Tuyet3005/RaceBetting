import pygame, sys
import config, obstacle
import show
from pygame.locals import *

list_store = [0,0,0,0,0,0]

DISPLAYSURF = pygame.display.set_mode((config.WIDTH,config.HEIGHT))
pygame.display.set_caption('Đua Xe Đat Cuoc!')
show.init(DISPLAYSURF)


while True:
    DISPLAYSURF.fill((255,255,255))
    show.Show_Background()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.display.quit()
            sys.exit()
       # if event.type == pygame.MOUSEMOTION:
    print(pygame.mouse.get_pos())
    x, y = pygame.mouse.get_pos()

    show.Show_Big(0, 264, 209, 271 < x < 354 and 207 < y < 303)
    show.Show_Big(1, 384, 204, 355 < x < 509 and 207 < y < 303)
    show.Show_Big(2, 504, 212, 510 < x < 597 and 207 < y < 303)

    pygame.display.update()
    #
    #     # if event.type == pygame.MOUSEMOTION:
    # print(pygame.mouse.get_pos())
    # DISPLAYSURF.blit(background, (0, 0))
    # DISPLAYSURF.blit(list[0], (0+x, 80))
    # pygame.display.update()
    # x += int(180 / config.FPS)
    # config.fpsClock.tick(config.FPS)


