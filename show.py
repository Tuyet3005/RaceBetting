import pygame, sys
import config, obstacle, random
from pygame.locals import *

DISPLAYSURF = 0
list_store = [0,0,0,0,0,0]

def init(_DISPLAYSURF):
    global DISPLAYSURF
    DISPLAYSURF = _DISPLAYSURF

def scale(image, scale_ratio):
    rect = image.get_rect()
    w, h = rect.size
    ratio = h / w
    new_image = pygame.transform.scale(image, (int(config.WIDTH * scale_ratio), int(config.WIDTH * scale_ratio * ratio)))
    return new_image

def Show_Background():
    background_store = pygame.image.load("img\\cuahang\\background_store.png")
    background_store = scale(background_store,1)
    DISPLAYSURF.blit(background_store, (-20, 0))



nhanh = pygame.image.load("img\\cuahang\\nhanh.png")

thang = pygame.image.load("img\\cuahang\\thang.png")

vuot = pygame.image.load("img\\cuahang\\vuot.png")

list_qua_hien_thi = []


def Show_Big(i, x, y, is_big):
    if i == 0:
        image = nhanh
    elif i == 1:
        image = thang
    elif i == 2:
        image = vuot
    small = scale(image, 0.115)
    large = scale(image, 0.125)

    if is_big:
        w_s, h_s = small.get_rect().size
        w_l, h_l = large.get_rect().size

        new_x = int(x - (w_l - w_s) / 2)
        new_y = int(y - (h_l - h_s) / 2)

        DISPLAYSURF.blit(large, (new_x, new_y))

    else:
        DISPLAYSURF.blit(small, (x, y))
