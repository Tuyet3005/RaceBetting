import pygame, sys, random
import config


list_gift = []
list_effect_bua = []
random_gift = []
ratio = 0.07

def import_effect_bua():
    global ratio, list_effect_bua

    list_effect_bua = []

    for i in range(0, 7):
        list_effect_bua.append(pygame.image.load("img\\effect_bua\\" + str(i) + ".png"))
        list_effect_bua[i] = pygame.transform.smoothscale(list_effect_bua[i], (int(config.WIDTH * ratio), int(config.HEIGHT * ratio)))

def import_():
    global ratio, list_gift, random_gift

    list_gift = []
    random_gift = []

    for i in range(0, 16):
        list_gift.append(pygame.image.load("img\\gift\\giftbox" + str(i+1) + ".png"))
        list_gift[i] = pygame.transform.smoothscale(list_gift[i], (int(config.WIDTH * ratio), int(config.HEIGHT * ratio)))
    for i in range(0,5):
        random_gift.append(list_gift[random.randint(0, 15)])
    import_effect_bua()


