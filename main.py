import pygame, sys, random, time
import config, obstacle
from pygame import constants
from pygame.locals import *


def default():
    global name_, list, vitri, nv, _x, nen, speed, _so_khung_hinh, hienthi_effect_bua
    global bat_dau_dung, thoi_gian_dung, check_lat_nguoc, _bua, toa_do
    global _check, _check_bua, xuat_hien_bua, effect, kich_thuoc_bxh, ratio, ratio_eff, ratio_next_button
    global vi_tri_nhan_vat, list_dongvat, thutu, thang, thua, next_button, height, HEIGHT, i, j, speed_td, speed

    f = open("name.txt", "r")
    name_ = f.read().split("\n")
    f.close()

    list = [0, 0, 0, 0, 0]
    vitri = [0, 0, 0, 0, 0]
    nv = [0, 0, 0, 0, 0]
    _x = [0, 0, 0, 0, 0]
    nen = [0, 0, 0, 0, 0]
    speed = [0, 0, 0, 0, 0]
    _so_khung_hinh = [0, 0, 0, 0, 0]
    bat_dau_dung = [0, 0, 0, 0, 0]
    effect = [0, 0, 0, 0, 0]
    list_dongvat = [0, 0, 0, 0, 0]
    thutu = [0, 0, 0, 0, 0]
    height = [0, 0, 0, 0, 0]

    hienthi_effect_bua = [False, False, False, False, False]
    check_lat_nguoc = [False, False, False, False, False]
    _check = [False, False, False, False, False]
    _check_bua = [False, False, False, False, False]

    _bua = random.choices(range(0, 7), weights=[1, 1, 0.05, 1, 1, 1, 1], k=5)
    thoi_gian_dung = 1.0
    kich_thuoc_bxh = 0.5
    ratio = 0.08
    ratio_next_button = 0.08
    vi_tri_nhan_vat = thang = thua = next_button = 0

    xuat_hien_bua = [random.randint(0, 3) for i in range(5)]
    speed = [random.randint(60, 120) for i in range(5)]

    HEIGHT = config.HEIGHT / 7
    toa_do = int(config.WIDTH / 5)

    speed_td = [
        [
            random.randrange(config.speed_min, config.speed_max)
            for i in range(config.WIDTH // toa_do * 10)
        ]
        for j in range(0, 5)
    ]

    j = 0
    ratio_eff = 0.1

    random.shuffle(name_)


def load_function(img, ratio):
    img = pygame.image.load(img)
    img = pygame.transform.smoothscale(
        img, (int(config.WIDTH * ratio), int(config.HEIGHT * ratio))
    )
    return img


def load_bangxephang():
    global thang, thua, next_button
    thang = load_function("img\\bang_xep_hang\\thang.png", kich_thuoc_bxh)
    thua = load_function("img\\bang_xep_hang\\thua.png", kich_thuoc_bxh)
    next_button = load_function("img\\next_button.png", ratio_next_button)


def khoi_tao():
    global HEIGHT, toa_do, dich, _nen, height

    default()
    load_nen()
    load_set()
    load_effect()
    load_bangxephang()
    obstacle.import_()

    for i in range(config.WIDTH // toa_do * 10):
        for j in range(0, 5):
            speed_td[j].append(random.randrange(config.speed_min, config.speed_max))

    for i in range(0, 5):
        height[i] = HEIGHT * (1.5 + i) - list[i].get_rect().size[1] / 2

    dich = config.WIDTH - list[1].get_rect().size[0]
    dich = dich - 15 / config.size_

    if config.set_duoc_chon == 2:
        _nen = nen[0]
    elif config.set_duoc_chon == 3:
        _nen = nen[1]
    elif config.set_duoc_chon == 5:
        _nen = nen[2]
    elif config.set_duoc_chon == 1 or config.set_duoc_chon == 4:
        _nen = nen[3]


def form():  # in ra cai khung
    global DISPLAYSURF
    DISPLAYSURF = pygame.display.set_mode(
        (config.WIDTH, config.HEIGHT), constants.RESIZABLE
    )
    pygame.display.set_caption("Đua Xe Đặt Cược!")


def bang_xep_hang():
    font = pygame.font.SysFont(None, config.WIDTH // 30)
    font_ = pygame.font.SysFont(None, config.WIDTH // 40)
    test_ten = font_.render(str(i) + "   " + config.user, True, (255, 255, 255))

    khoang_cach_dong = test_ten.get_height()
    for k in range(0, 5):
        if config.nhan_vat == thutu[k]:
            _ten = font_.render(str(k + 1) + "   " + config.user, True, (0, 0, 0))
            DISPLAYSURF.blit(
                _ten,
                (
                    config.WIDTH * 0.4,
                    config.HEIGHT // 2 + khoang_cach_dong * ((k + 1.5)),
                ),
            )
        else:
            _ten = font_.render(str(k + 1) + "   " + name_[k], True, (255, 255, 255))
            DISPLAYSURF.blit(
                _ten,
                (
                    config.WIDTH * 0.4,
                    config.HEIGHT // 2 + khoang_cach_dong * ((k + 1.5)),
                ),
            )


def output():
    if _check[0] and _check[1] and _check[2] and _check[3] and _check[4]:
        i = 0

        if (config.nhan_vat) == thutu[0]:
            DISPLAYSURF.blit(
                thang,
                (
                    config.WIDTH // 2 - thang.get_rect().size[0] // 2,
                    config.HEIGHT // 2 - thang.get_rect().size[1] // 2,
                ),
            )
            font = pygame.font.SysFont(None, 34)
            ket_qua_ = font.render(config.user + " win !", True, (255, 0, 0))
            DISPLAYSURF.blit(
                ket_qua_,
                (config.WIDTH // 2 - ket_qua_.get_width() // 2, config.HEIGHT * 0.47),
            )

        else:
            DISPLAYSURF.blit(
                thua,
                (
                    config.WIDTH // 2 - thua.get_rect().size[0] // 2,
                    config.HEIGHT // 2 - thua.get_rect().size[1] // 2,
                ),
            )
            font = pygame.font.SysFont(None, 34)
            ket_qua_ = font.render(config.user + " lose !", True, (255, 0, 0))
            DISPLAYSURF.blit(
                ket_qua_,
                (config.WIDTH // 2 - ket_qua_.get_width() // 2, config.HEIGHT * 0.47),
            )

        bang_xep_hang()

        next_button_x = config.WIDTH // 2 + thang.get_width() // 2
        next_button_y = config.HEIGHT // 2 + thang.get_height() // 2
        DISPLAYSURF.blit(next_button, (next_button_x, next_button_y))
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if (
                next_button_x <= mouse_x <= next_button_x + next_button.get_width()
                and next_button_y <= mouse_y <= next_button_y + next_button.get_height()
            ):
                pygame.display.quit()


def load_nen():
    global nen
    for i in range(0, 4):
        nen[i] = load_function(f"img\\nen{i + 1}.png", 1)


def set_xe():
    for i in range(0, 5):
        list[i] = load_function(f"img\\xe\\xe{i + 1}.png", ratio)


def set_dongvat():
    for i in range(0, 5):
        list[i] = load_function(f"img\\dongvat\\dv{i + 1}.png", ratio)


def set_maybay():
    for i in range(0, 5):
        list[i] = load_function(f"img\\maybay\\maybay{i + 1}.png", ratio)
    

def set_moto():
    for i in range(0, 5):
        list[i] = load_function(f"img\\moto\\moto{i + 1}.png", ratio)


def set_chibi():
    global ratio
    ratio = 0.12
    for i in range(0, 5):
        list[i] = load_function(f"img\\chibi\\{i + 1}.png", ratio)

   
def load_set():
    global _nen

    if config.set_duoc_chon == 1:
        set_xe()
    elif config.set_duoc_chon == 2:
        set_dongvat()
    elif config.set_duoc_chon == 3:
        set_maybay()
    elif config.set_duoc_chon == 4:
        set_moto()
    elif config.set_duoc_chon == 5:
        set_chibi()

    for i in range(0, 5):
        height[i] = HEIGHT * (1.5 + i) - list[i].get_rect().size[1] / 2


def load_effect():
    global ratio_eff
    for i in range(0, 3):
        effect[i] = load_function(f"img\\wineffect\\{i + 1}.png", ratio_eff)


def solve():
    global _x, _check, i, j, toa_do, speed, speed_td, nv, vi_tri_nhan_vat
    global nv, height, effect, thutu, vitri

    for i in range(0, 5):
        if _x[i] < (dich - 20 / config.size_):
            if time.time() - bat_dau_dung[i] >= thoi_gian_dung and speed[i] == 0:
                speed[i] = speed_td[i][nv[i]]

            if (
                toa_do - 1 <= _x[i] <= toa_do + 1
                or 2 * toa_do - 1 <= _x[i] <= 2 * toa_do + 1
                or 3 * toa_do - 1 <= _x[i] <= 3 * toa_do + 1
                or 4 * toa_do - 1 <= _x[i] <= 4 * toa_do + 1
            ):
                nv[i] = round(_x[i] / toa_do)

                if check_lat_nguoc[i] == False:
                    speed[i] = speed_td[i][nv[i]]

                else:
                    if _x[i] <= vi_tri_nhan_vat - toa_do * 0.2 or _x[i] <= 0:
                        list[i] = pygame.transform.flip(list[i], True, False)
                        speed[i] = abs(speed[i])
                        check_lat_nguoc[i] = False

            if _x[i] < 0:
                _x[i] = 0
                list[i] = pygame.transform.flip(list[i], True, False)
                speed[i] = abs(speed[i])
                check_lat_nguoc[i] = False

            if xuat_hien_bua[i] <= nv[i]:
                if _check_bua[i] == False:
                    if vitri[i] == 0:
                        vitri[i] = _x[i] + toa_do * 0.6

                    DISPLAYSURF.blit(obstacle.random_gift[i], (vitri[i], height[i]))
                    if (
                        vitri[i] + obstacle.random_gift[i].get_width() // 2
                        < _x[i] + list[i].get_width()
                    ):
                        if _bua[i] == 0:  # 0: nhanh
                            speed[i] = speed_td[i][nv[i] + 1] = speed[i] * 1.5
                            hienthi_effect_bua[i] = True

                        elif _bua[i] == 1:  # 1:cham
                            speed[i] = speed_td[i][nv[i] + 1] = speed[i] * 0.5
                            hienthi_effect_bua[i] = True

                        elif _bua[i] == 2:  # tro ve vach bat dau
                            _x[i] = 0
                            nv[i] = 0
                            hienthi_effect_bua[i] = True

                        elif _bua[i] == 3:  # toi dich
                            _x[i] = dich
                            nv[i] = 5
                            hienthi_effect_bua[i] = True

                        elif _bua[i] == 4:  # bien hinh
                            _x[i] += toa_do // 2
                            nv[i] += 1
                            hienthi_effect_bua[i] = True

                        elif _bua[i] == 5:  # dung
                            bat_dau_dung[i] = time.time()
                            speed[i] = 0
                            hienthi_effect_bua[i] = True

                        elif _bua[i] == 6:  # chay lui
                            list[i] = pygame.transform.flip(list[i], True, False)
                            speed[i] = -speed[i]
                            vi_tri_nhan_vat = _x[i]
                            check_lat_nguoc[i] = True
                            hienthi_effect_bua[i] = True

                        _check_bua[i] = True

            if hienthi_effect_bua[i] == True:
                if _so_khung_hinh[i] < 50:
                    DISPLAYSURF.blit(
                        obstacle.list_effect_bua[_bua[i]],
                        (
                            _x[i],
                            height[i] - obstacle.list_effect_bua[_bua[i]].get_height(),
                        ),
                    )
                    _so_khung_hinh[i] += 1
                else:
                    hienthi_effect_bua[i] = False

            DISPLAYSURF.blit(list[i], (int(_x[i]), height[i]))
            _x[i] += speed[i] / config.FPS
        else:
            if _check[i] == False:
                thutu[j] = i
                j += 1
                _check[i] = True
            DISPLAYSURF.blit(list[i], (dich, height[i]))

            if thutu[0] == i:
                DISPLAYSURF.blit(effect[0], (dich - effect[0].get_width(), height[i]))
            elif thutu[1] == i:
                DISPLAYSURF.blit(effect[1], (dich - effect[1].get_width(), height[i]))
            elif thutu[2] == i:
                DISPLAYSURF.blit(effect[2], (dich - effect[2].get_width(), height[i]))

    output()


def run_game():
    global event

    pygame.init()
    form()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.display.quit()
                sys.exit()

        DISPLAYSURF.blit(_nen, (0, 0))
        if event.type == constants.VIDEORESIZE:
            config.WIDTH, config.HEIGHT = DISPLAYSURF.get_size()
            load_set()
            load_nen()
        solve()

        if not pygame.display.get_init():
            # User quit
            break

        pygame.display.update()
        config.fpsClock.tick(config.FPS)

    return config.nhan_vat == thutu[0]


if __name__ == "__main__":
    khoi_tao()
    run_game()
