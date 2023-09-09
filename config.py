import pygame, sys

pygame.init()

# Cai dat kich thuoc cho man hinh
HEIGHT = 666
WIDTH = 1000

# Cai dat toc do cho game
speed_min = 60
speed_max = 120

# Chon set nhan vat
size_ = 1
set_duoc_chon = 1
user = "Tuyet"
nhan_vat = 1


def set_size(size):
    global HEIGHT, WIDTH, size_

    if size == 1:
        WIDTH, HEIGHT = 600, 400
    elif size == 2:
        WIDTH, HEIGHT = 800, 533
    elif size == 3:
        WIDTH, HEIGHT = 1000, 666
    size_ = size


def chon_set(set_duoc_chon_):
    global set_duoc_chon
    set_duoc_chon = set_duoc_chon_


def ten_nguoi_choi(user_):
    global user
    user = user_


def nhan_vat_duoc_chon(nhan_vat_):
    global nhan_vat
    nhan_vat = nhan_vat_ - 1

FPS = 60
fpsClock = pygame.time.Clock()