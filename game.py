import datetime
from tkinter import *

import pygame, time, random
from pygame import mixer
from pygame.locals import *

import config
import show
import main

pygame.init()
mixer.init()
mixer.music.load("sound\\Chiru.mp3")
mixer.music.set_volume(20)
audio = mixer.music.play()

width = 1080
height = 720

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

user = None


def Sign_in():
    sign_in = Tk()
    scrw = sign_in.winfo_screenwidth()
    scrh = sign_in.winfo_screenheight()
    sign_in.geometry('1080x720+%d+%d' % (scrw / 2 - 1080 / 2 - 9, scrh / 2 - 720 / 2 - 30))
    sign_in.title("Đua xe cá cược")
    thongtindangnhap = open('taikhoan.txt').read()
    data_account = open('account.txt').read()

    def chuyenhuong():
        global user
        user = signin.get()

        file = open('account.txt', mode='r')

        password = matkhau.get()
        a = str(list([user, password])) + "\n"
        data_signin = list(file)
        file.seek(0)
        check = a in data_signin
        if check == True:
            file.close()
            sign_in.destroy()
            return menu()
        else:
            pygame.init()
            mixer.init()
            mixer.music.load("sound\\sign_in.mp3")
            mixer.music.set_volume(20)
            mixer.music.play()
            time.sleep(3.5)
            pygame.display.quit()
        file.close()

    def sign_up():

        # sign_in.quit()
        sign_in.destroy()
        tk = Tk()
        scrw = tk.winfo_screenwidth()
        scrh = tk.winfo_screenheight()
        tk.geometry('1080x720+%d+%d' % (scrw / 2 - 1080 / 2 - 9, scrh / 2 - 720 / 2 - 30))
        tk.title("Đua xe cá cược")
        file = open('account.txt', mode='a+')

        title_sign = Label(tk, text="\n Đăng ký \n", font=("Jokerman", 26, "bold", "italic"), fg="red")
        title_sign.pack()
        Label(tk, text="Tài khoản", font=("Jokerman", 16, "bold", "italic"), fg="black").pack()
        signin = Entry(tk, width=20, font=("Segoe UI", 12), fg="black")
        signin.pack()
        Label(tk, text="Mật khẩu", font=("Jokerman", 16, "bold", "italic"), fg="black").pack()
        matkhau = Entry(tk, width=20, font=("Segoe UI", 12), fg="black")
        matkhau.pack()

        def dktaikhoan():
            file = open('taikhoan.txt', mode='r')
            thongtindangnhap = list(file)
            file.close()
            file = open('account.txt', mode='a+')
            global user
            user = signin.get()
            password = matkhau.get()
            a = [user, password]

            data_signin = list(file)
            b = user + "\n"
            check = b in thongtindangnhap
            if check == True:
                pygame.init()
                mixer.init()
                mixer.music.load("sound\\trungtaikhoan.mp3")
                mixer.music.set_volume(20)
                mixer.music.play()
                time.sleep(3.5)
                pygame.display.quit()
            else:

                file.write(str(a) + "\n")
                file.close()
                file = open('taikhoan.txt', mode='r')
                a = file.read(-1)
                file.close()
                file = open('taikhoan.txt', mode='w+')
                file.seek(0)
                file.seek(0)
                file.write(user + "\n" + a)
                file.close()

                tk.destroy()

                menu()

        Button(tk, text="Sign up", font=("Snap ITC", 16, "bold"),
               fg="green", width=11, command=dktaikhoan, height=1, relief="groove").pack()

        def Back_sign_in():
            tk.destroy()
            return Sign_in()

        Button(tk, text="Back", font=("Snap ITC", 16, "bold"),
               fg="green", width=11, command=Back_sign_in, height=1, relief="groove").pack()
        file.close()
        tk.mainloop()

    title_sign = Label(sign_in, text="\n Đăng Nhập \n", font=("Jokerman", 26, "bold", "italic"), fg="red")
    title_sign.pack()
    Label(sign_in, text="Tài khoản", font=("Jokerman", 16, "bold", "italic"), fg="black").pack()
    signin = Entry(sign_in, width=20, font=("Segoe UI", 12), fg="black")
    signin.pack()
    Label(sign_in, text="Mật khẩu", font=("Jokerman", 16, "bold", "italic"), fg="black").pack()
    matkhau = Entry(sign_in, width=20, font=("Segoe UI", 12), fg="black")
    matkhau.pack()
    Enter_account = Button(sign_in, text="Sign in", font=("Snap ITC", 16, "bold"),
                           fg="green", width=11, command=chuyenhuong, height=1, relief="groove")
    Enter_account.pack()

    Button(sign_in, text="Sign up", font=("Snap ITC", 16, "bold"),
           fg="green", width=11, command=sign_up, height=1, relief="groove").pack()
    Label(sign_in, text="Lịch sử đăng nhập: ", font=("Jokerman", 26, "bold", "italic"), fg="red").pack()

    Label(sign_in, text=thongtindangnhap, font=("Jokerman", 12, "bold", "italic"), fg="black").pack()

    sign_in.mainloop()


def menu():
    pygame.init()
    mixer.init()
    mixer.music.load("sound\\tick.wav")
    mixer.music.set_volume(20)
    mixer.music.play()
    time.sleep(0.35)
    mixer.music.load("sound\\ShapeOfYou.mp3")
    mixer.music.set_volume(20)
    audio = mixer.music.play()

    DISPLAY = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Đua Xe Cá Cược")

    global data
    name = user
    file = open('filesave\\' + 'money' + name + '.txt', mode='a+')
    file.seek(0)
    data = file.readline()
    if data == '':
        file.write('20000')
    else:
        pass
    file.seek(0)
    data = file.readline()

    file.close()
    textfont = pygame.font.SysFont('Jokerman', 20)

    while True:

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.display.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                # xu ly exit
                if mouse[0] >= 630 and mouse[0] <= 950 and mouse[1] > 580 and mouse[1] <= 650:
                    mixer.music.load("sound\\tick.wav")
                    mixer.music.set_volume(20)
                    mixer.music.play()
                    time.sleep(0.3)
                    pygame.display.quit()
                    sys.exit()
                # xu ly start game
                elif mouse[0] >= 630 and mouse[0] <= 950 and mouse[1] >= 300 and mouse[1] <= 370:
                    mixer.music.load("sound\\tick.wav")
                    mixer.music.set_volume(20)
                    mixer.music.play()
                    return choose_set()
                # xu ly history game
                elif mouse[0] >= 630 and mouse[0] <= 950 and mouse[1] > 370 and mouse[1] <= 440:
                    mixer.music.load("sound\\tick.wav")
                    mixer.music.set_volume(20)
                    mixer.music.play()
                    return lichsu()
                # xu ly history
                elif mouse[0] >= 630 and mouse[0] <= 950 and mouse[1] > 440 and mouse[1] <= 510:
                    mixer.music.load("sound\\tick.wav")
                    mixer.music.set_volume(20)
                    mixer.music.play()
                    help_game()
                # xu ly logout
                elif mouse[0] >= 630 and mouse[0] <= 950 and mouse[1] > 510 and mouse[1] <= 580:
                    mixer.music.load("sound\\tick.wav")
                    mixer.music.set_volume(20)
                    mixer.music.play()
                    time.sleep(0.35)
                    return logout()
                # time.sleep(0.5)
                # cửa hàng
                elif mouse[0] >= 0 and mouse[0] <= 110 and mouse[1] > 600 and mouse[1] <= 720:
                    mixer.music.load("sound\\tick.wav")
                    mixer.music.set_volume(20)
                    mixer.music.play()

                    return cuahang()
                # kiem tien
                elif mouse[0] >= 110 and mouse[0] <= 220 and mouse[1] > 600 and mouse[1] <= 720:
                    mixer.music.load("sound\\tick.wav")
                    mixer.music.set_volume(20)
                    mixer.music.play()
                    if int(data) < 10000:
                        make_money()
                    else:
                        time.sleep(1)
                        mixer.music.load("sound\\kiemtien.mp3")
                        mixer.music.set_volume(20)
                        mixer.music.play()
                else:
                    pass

        DISPLAY.fill((WHITE))
        sf_background = pygame.image.load('image of menu\\bg.png')
        DISPLAY.blit(sf_background, (0, 0))
        # in Menu
        New_game = pygame.image.load('image of menu\\startgame.png')
        DISPLAY.blit(New_game, (630, 300))
        Load_game = pygame.image.load('image of menu\\history.png')
        DISPLAY.blit(Load_game, (630, 370))
        History = pygame.image.load('image of menu\\help.png')
        DISPLAY.blit(History, (630, 440))
        Help_game = pygame.image.load('image of menu\\dangxuat.png')
        DISPLAY.blit(Help_game, (630, 510))
        Exit_game = pygame.image.load('image of menu\\exit.png')
        DISPLAY.blit(Exit_game, (630, 580))
        User_game = textfont.render('Wellcome ' + user, True, RED)
        DISPLAY.blit(User_game, (5, 3))
        Money = data
        coins = textfont.render('money ' + Money + " VND", True, RED)
        DISPLAY.blit(coins, (850, 3))
        store = pygame.image.load('image of menu\\icon.png')
        store = pygame.transform.scale(store, (100, 100))
        DISPLAY.blit(store, (10, 600))
        money = pygame.image.load('image of menu\\money.png')
        DISPLAY.blit(money, (110, 600))

        # Background

        mouse = pygame.mouse.get_pos()

        if mouse[0] >= 630 and mouse[0] <= 950 and mouse[1] >= 300 and mouse[1] <= 370:
            New_game = pygame.image.load('image of menu\\startgamev2.png')
            DISPLAY.blit(New_game, (630, 300))
        elif mouse[0] >= 630 and mouse[0] <= 950 and mouse[1] > 370 and mouse[1] <= 440:
            Load_game = pygame.image.load('image of menu\\historyv2.png')
            DISPLAY.blit(Load_game, (630, 370))

        elif mouse[0] >= 630 and mouse[0] <= 950 and mouse[1] > 440 and mouse[1] <= 510:
            History = pygame.image.load('image of menu\\helpv2.png')
            DISPLAY.blit(History, (630, 440))
        elif mouse[0] >= 630 and mouse[0] <= 950 and mouse[1] > 510 and mouse[1] <= 580:
            Help_game = pygame.image.load('image of menu\\dangxuatv2.png')
            DISPLAY.blit(Help_game, (630, 510))

        elif mouse[0] >= 630 and mouse[0] <= 950 and mouse[1] > 580 and mouse[1] <= 650:
            Exit_game = pygame.image.load('image of menu\\exitv2.png')
            DISPLAY.blit(Exit_game, (630, 580))
        elif mouse[0] >= 0 and mouse[0] <= 110 and mouse[1] > 600 and mouse[1] <= 720:
            store = pygame.image.load('image of menu\\storev2.png')
            DISPLAY.blit(store, (10, 600))
        elif mouse[0] >= 110 and mouse[0] <= 220 and mouse[1] > 600 and mouse[1] <= 720:
            money = pygame.image.load('image of menu\\moneyv2.png')
            DISPLAY.blit(money, (110, 600))

        else:
            pass

        pygame.display.update()
        DISPLAY.blit(sf_background, (0, 0))


def help_game():
    info = Tk()
    scrw = info.winfo_screenwidth()
    scrh = info.winfo_screenheight()
    info.geometry('1080x720+%d+%d' % (scrw / 2 - 1080 / 2 - 9, scrh / 2 - 720 / 2 - 30))
    info.title("Đua xe đặt cược")

    def info_quit():
        mixer.music.load("sound\\tick.wav")
        mixer.music.set_volume(20)
        mixer.music.play()
        # time.sleep(0.5)
        info.destroy()
        return menu()

    title_inf = Label(info, text="GAME ĐUA XE ĐẶT CƯỢC", font=("Jokerman", 30, "bold", "italic"), fg="red")
    title_inf.pack()
    Label(info, text="NHÓM PHÁT TRIỂN GAME: NHÓM 4", font=("Segoe UI", 18), fg="red").pack()
    Label(info, text="Hướng dẫn chơi", font=("Segoe UI", 18), fg="red").pack()
    cachchoi_maingame = """- Mỗi người chơi đăng nhập lần đầu tiên sẽ được tặng 200.000 VNĐ.
- Người chơi sẽ chọn xe mà mình muốn đặt cược và tiến hành đặt cược số tiền tùy ý,
   số tiền đặt cược không được vượt quá số tiền hiện có .
- Nếu thắng người chơi sẽ nhận được gấp đôi số tiền đã đặt cược, nếu thua sẽ mất hết số tiền đó. 
- Các loại bùa xuất hiện trên đường đua:
	   1. Bùa chạy nhanh: giúp tốc độ nhân vật tăng nhanh trong 1(s).
	   2. Bùa vượt: giúp cho nhân vật dính bùa vượt qua nhân vật đang xếp trên nó.
	   3. Bùa chạy chậm: làm cho tốc dộ nhân vật dính bùa giảm đi trong 1(s).
	   4. Bùa choáng: làm cho nhân vật dính bùa dừng lại trong 1(s).
	   5. Bùa đi lùi: làm nhân vật dính bùa đi lùi trong 1(s).
	   6. Bùa quay lại vạch xuất phát: làm cho nhân vật dính bùa ngay lập tức quay lại vạch xuất phát ban đầu.
	   7. Bùa về đích: giúp cho nhân vật dính bùa ngay lập tức biến đến vạch đích.
- Người chơi có thể mua bùa trong cửa hàng để dùng lúc chơi: bùa mua sẽ là bùa random trong 7 loại bùa có trên.
   Người chơi sẽ không biết đó là bùa gì cho đến khi dùng nó.
- Khi hết tiền người chơi sẽ được phép chơi minigame để kiếm thêm tiền."""
    Label(info, text=cachchoi_maingame, font=("Segoe UI", 13), fg="black",
          justify=LEFT).pack()
    Label(info, text="Minigame: Giải câu đố", font=("Segoe UI", 15), fg="red",
          justify=LEFT).pack()
    cachchoi_minigame = '''- Người chơi cần trả lời 3 câu đố.
- Nếu trả lời đúng 3 câu thì người chơi sẽ nhận được 50.000 VNĐ.
- Nếu trả lời sai ít nhất 1 câu người chơi sẽ không nhận được tiền.
	'''
    Label(info, text=cachchoi_minigame, font=("Segoe UI", 13), fg="black", justify=LEFT).pack()

    exit_info = Button(info, text="Back", font=("Snap ITC", 16, "bold"), fg="green",
                       width=11, height=1, relief="groove", command=info_quit)
    exit_info.pack()
    info.mainloop()


def choose_set():
    mixer.music.load("sound\\Chiru.mp3")
    mixer.music.set_volume(20)
    audio = mixer.music.play()

    DISPLAY2 = pygame.display.set_mode((width, height))
    pygame.display.set_caption("chon")
    mixer.music.load("sound\\tick.wav")
    mixer.music.set_volume(20)
    mixer.music.play()
    global set_duoc_chon

    while True:

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.display.quit()

                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:
                # set 5
                if mouse[0] >= 630 and mouse[0] <= 950 and mouse[1] > 580 and mouse[1] <= 650:
                    mixer.music.load("sound\\tick.wav")
                    mixer.music.set_volume(20)
                    mixer.music.play()
                    set_duoc_chon = 5
                    return choose_chibi()
                # set 1
                elif mouse[0] >= 630 and mouse[0] <= 950 and mouse[1] >= 300 and mouse[1] <= 370:
                    mixer.music.load("sound\\tick.wav")
                    mixer.music.set_volume(20)
                    mixer.music.play()
                    set_duoc_chon = 1
                    return choose_car()
                # set 2
                elif mouse[0] >= 630 and mouse[0] <= 950 and mouse[1] > 370 and mouse[1] <= 440:
                    mixer.music.load("sound\\tick.wav")
                    mixer.music.set_volume(20)
                    mixer.music.play()
                    set_duoc_chon = 2
                    return choose_animals()
                # set 3
                elif mouse[0] >= 630 and mouse[0] <= 950 and mouse[1] > 440 and mouse[1] <= 510:
                    mixer.music.load("sound\\tick.wav")
                    mixer.music.set_volume(20)
                    mixer.music.play()
                    set_duoc_chon = 3
                    return choose_planes()
                # set 4
                elif mouse[0] >= 630 and mouse[0] <= 950 and mouse[1] > 510 and mouse[1] <= 580:
                    mixer.music.load("sound\\tick.wav")
                    mixer.music.set_volume(20)
                    mixer.music.play()
                    set_duoc_chon = 4
                    return choose_motors()
                elif mouse[0] >= 630 and mouse[0] <= 950 and mouse[1] > 650 and mouse[1] <= 720:
                    mixer.music.load("sound\\tick.wav")
                    mixer.music.set_volume(20)
                    mixer.music.play()
                    return menu()
                else:
                    pass
            else:
                pass
        DISPLAY2.fill((WHITE))
        sf_background = pygame.image.load("image of menu\\bg.png")
        DISPLAY2.blit(sf_background, (0, 0))

        set_game = pygame.image.load('image of menu\\set_duoc_chon.png')
        DISPLAY2.blit(set_game, (630, 230))
        set1 = pygame.image.load('image of menu\\set1.png')
        DISPLAY2.blit(set1, (630, 300))
        set2 = pygame.image.load('image of menu\\set2.png')
        DISPLAY2.blit(set2, (630, 370))
        set3 = pygame.image.load('image of menu\\set3.png')
        DISPLAY2.blit(set3, (630, 440))
        set4 = pygame.image.load('image of menu\\set4.png')
        DISPLAY2.blit(set4, (630, 510))
        set5 = pygame.image.load('image of menu\\set5.png')
        DISPLAY2.blit(set5, (630, 580))
        back = pygame.image.load('image of menu\\return.png')
        DISPLAY2.blit(back, (630, 650))

        mouse = pygame.mouse.get_pos()

        if mouse[0] >= 630 and mouse[0] <= 950 and mouse[1] >= 300 and mouse[1] <= 370:
            New_game = pygame.image.load('image of menu\\set1v2.png')
            DISPLAY2.blit(New_game, (630, 300))
        elif mouse[0] >= 630 and mouse[0] <= 950 and mouse[1] > 370 and mouse[1] <= 440:
            Load_game = pygame.image.load('image of menu\\set2v2.png')
            DISPLAY2.blit(Load_game, (630, 370))

        elif mouse[0] >= 630 and mouse[0] <= 950 and mouse[1] > 440 and mouse[1] <= 510:
            History = pygame.image.load('image of menu\\set3v2.png')
            DISPLAY2.blit(History, (630, 440))

        elif mouse[0] >= 630 and mouse[0] <= 950 and mouse[1] > 510 and mouse[1] <= 580:
            Help_game = pygame.image.load('image of menu\\set4v2.png')
            DISPLAY2.blit(Help_game, (630, 510))

        elif mouse[0] >= 630 and mouse[0] <= 950 and mouse[1] > 580 and mouse[1] <= 650:
            Exit_game = pygame.image.load('image of menu\\set5v2.png')
            DISPLAY2.blit(Exit_game, (630, 580))
        elif mouse[0] >= 630 and mouse[0] <= 950 and mouse[1] > 650 and mouse[1] <= 720:
            back = pygame.image.load('image of menu\\returnv2.png')
            DISPLAY2.blit(back, (630, 650))
        else:
            pass

        pygame.display.update()
        DISPLAY2.blit(sf_background, (0, 0))


def choose_size():
    mixer.music.load("sound\\Chiru.mp3")
    mixer.music.set_volume(20)
    audio = mixer.music.play()

    DISPLAY2 = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Đua xe đặt cược")
    mixer.music.load("sound\\tick.wav")
    mixer.music.set_volume(20)
    mixer.music.play()
    global size
    while True:

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.display.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:
                # size
                # small
                if mouse[0] >= 630 and mouse[0] <= 950 and mouse[1] > 370 and mouse[1] <= 440:
                    mixer.music.load("sound\\tick.wav")
                    mixer.music.set_volume(20)
                    mixer.music.play()
                    size = 1
                    start_game()
                # middle
                elif mouse[0] >= 630 and mouse[0] <= 950 and mouse[1] > 440 and mouse[1] <= 510:
                    mixer.music.load("sound\\tick.wav")
                    mixer.music.set_volume(20)
                    mixer.music.play()
                    size = 2
                    start_game()
                # big
                elif mouse[0] >= 630 and mouse[0] <= 950 and mouse[1] > 510 and mouse[1] <= 580:
                    mixer.music.load("sound\\tick.wav")
                    mixer.music.set_volume(20)
                    mixer.music.play()
                    size = 3
                    start_game()
                elif mouse[0] >= 630 and mouse[0] <= 950 and mouse[1] > 580 and mouse[1] <= 650:
                    mixer.music.load("sound\\tick.wav")
                    mixer.music.set_volume(20)
                    mixer.music.play()
                    if set_duoc_chon == 'car':
                        return choose_car()
                    elif set_duoc_chon == 'animal':
                        return choose_animals()
                    elif set_duoc_chon == 'planes':
                        return choose_planes()
                    elif set_duoc_chon == 'motor':
                        return choose_motors()
                    elif set_duoc_chon == 'chibi':
                        return choose_chibi()
                    else:
                        return menu()
                else:
                    pass
        DISPLAY2.fill((WHITE))
        sf_background = pygame.image.load('image of menu\\bg.png')
        DISPLAY2.blit(sf_background, (0, 0))

        set1 = pygame.image.load('image of menu\\size.png')
        DISPLAY2.blit(set1, (630, 300))
        small = pygame.image.load('image of menu\\sizesmall.png')
        DISPLAY2.blit(small, (630, 370))
        middle = pygame.image.load('image of menu\\sizemiddle.png')
        DISPLAY2.blit(middle, (630, 440))
        big = pygame.image.load('image of menu\\sizebig.png')
        DISPLAY2.blit(big, (630, 510))
        back = pygame.image.load('image of menu\\return.png')
        DISPLAY2.blit(back, (630, 580))

        mouse = pygame.mouse.get_pos()

        if mouse[0] >= 630 and mouse[0] <= 950 and mouse[1] > 370 and mouse[1] <= 440:
            small = pygame.image.load('image of menu\\sizesmallv2.png')
            DISPLAY2.blit(small, (630, 370))

        elif mouse[0] >= 630 and mouse[0] <= 950 and mouse[1] > 440 and mouse[1] <= 510:
            middle = pygame.image.load('image of menu\\sizemiddlev2.png')
            DISPLAY2.blit(middle, (630, 440))
        elif mouse[0] >= 630 and mouse[0] <= 950 and mouse[1] > 510 and mouse[1] <= 580:
            big = pygame.image.load('image of menu\\sizebigv2.png')
            DISPLAY2.blit(big, (630, 510))
        elif mouse[0] >= 630 and mouse[0] <= 950 and mouse[1] > 580 and mouse[1] <= 650:
            back = pygame.image.load('image of menu\\returnv2.png')
            DISPLAY2.blit(back, (630, 580))
        else:
            pass

        pygame.display.update()
        DISPLAY2.blit(sf_background, (0, 0))


def lichsu():
    lsu = Tk()
    scrw = lsu.winfo_screenwidth()
    scrh = lsu.winfo_screenheight()
    lsu.geometry('1080x720+%d+%d' % (scrw / 2 - 1080 / 2 - 9, scrh / 2 - 720 / 2 - 29))

    def info_quit():
        mixer.music.load("sound\\tick.wav")
        mixer.music.set_volume(20)
        mixer.music.play()
        # time.sleep(0.5)
        lsu.destroy()
        menu()

    title_lsu = Label(lsu, text="Lịch sử", font=("Jokerman", 30, "bold", "italic"), fg="red")
    title_lsu.pack()
    exit_lsu = Button(lsu, text="quay lại", font=("Snap ITC", 16, "bold"), fg="green",
                      width=11, height=1, relief="groove", command=info_quit)
    exit_lsu.pack()
    Label(lsu, text="người chơi:" + user, font=("Segoe UI", 16), fg="red").pack()
    file = open('filesave\\' + 'history' + user + '.txt', mode='a+')
    file.seek(0)
    lichsu = file.read(-1)
    file.close()
    Label(lsu, text=lichsu, font=("Segoe UI", 16), fg="red", justify=LEFT).pack()
    lsu.mainloop()


def start_game():
    global xechon

    money_betting()
    pygame.display.quit()

    config.set_size(size)
    config.chon_set(set_duoc_chon)
    config.nhan_vat_duoc_chon(xechon)
    main.khoi_tao()

    winorlose = main.run_game()
    after_play(winorlose)

    return menu()

def logout():
    pygame.display.quit()
    return Sign_in()


def money_betting():
    bet = Tk()
    bet.geometry('400x200')
    bet.title('Đặt cược tiền')

    def bet_quit():
        global moneybet
        money_bet = betting.get() or '0'
        moneybet = int(money_bet)
        if moneybet > int(data):
            pygame.init()
            mixer.init()
            mixer.music.load("sound\\cacuoc.mp3")
            mixer.music.set_volume(20)
            mixer.music.play()
            time.sleep(4)

        else:
            pygame.init()
            mixer.init()
            mixer.music.load("sound\\tick.wav")
            mixer.music.set_volume(20)
            mixer.music.play()
            time.sleep(0.5)
            bet.quit()
            bet.destroy()

    Label(bet, text='Đặt cược', font=("Jokerman", 26, "bold", "italic"), fg="red").pack()
    Label(bet, text="Số tiền hiện tại: " + data, font=("Jokerman", 16, "bold", "italic"), fg="red").pack()
    betting = Entry(bet, width=30, font=("Segoe UI", 16), fg="black", )
    betting.pack()

    Button(bet, text='Enter', font=("Snap ITC", 16, "bold"),
           fg="green", width=11, command=bet_quit, height=1, relief="groove").pack()

    bet.mainloop()


def after_play(winorlose):
    name = user
    file = open('filesave\\' + 'money' + name + '.txt', mode='a+')
    file.seek(0)
    read = file.readline()
    global ownmoney
    ownmoney = int(read)
    if winorlose == True:
        file = open('filesave\\' + 'money' + user + '.txt', mode='w+')
        deghi = str(moneybet + ownmoney)
        file.write(deghi)
        file.close()
        file = open('filesave\\' + 'history' + user + '.txt', mode='a+')
        a = file.read(-1)
        file.close()
        file = open('filesave\\' + 'history' + user + '.txt', mode='w+')
        file.seek(0)
        datetime_object = datetime.datetime.now()
        time = str(datetime_object)
        file.write(
            time + " ban da thang va nhan duoc " + str(moneybet) + "so tien con lai " + str(ownmoney - moneybet) + '\n')
        file.write(a)
        file.close()
        pygame.display.quit()
        return menu()
    else:
        file = open('filesave\\' + 'money' + user + '.txt', mode='w+')
        file.write(str(ownmoney - moneybet))
        file.close()
        file = open('filesave\\' + 'history' + user + '.txt', mode='a+')
        a = file.read(-1)
        file.close()
        file = open('filesave\\' + 'history' + user + '.txt', mode='w+')
        file.seek(0)
        datetime_object = datetime.datetime.now()
        time = str(datetime_object)
        file.write(
            time + " ban da thua va bi tru " + str(moneybet) + " so tien con lai " + str(ownmoney - moneybet) + '\n')
        file.write(a)
        file.close()
        pygame.display.quit()
        return menu()


def make_money():
    question_1 = 'Xã nào đông dân nhất?'
    question_2 = 'Quần nào rộng nhất?'
    question_3 = 'Con gì đập thì sống, mà không đập thì chết?'
    question_4 = 'Con đường nào dài nhất?'
    question_5 = 'Cái gì mà tay trái cầm được nhưng tay phải cầm không được?'
    question_6 = 'Nhà lớn nhất thế giới?'
    question_7 = 'Sở thú bị cháy ,đố bạn con gì chạy ra đầu tiên?'
    question_8 = 'Khi phát âm ra từ này, thì 100% ngời dân Việt Nam đều phát âm sai?'
    question_9 = 'Con gì đầu dê mình ốc?'
    question_10 = 'Môn gì càng thắng càng thua?'

    questions = (question_1, question_2, question_3, question_4, question_5,
                 question_6, question_7, question_8, question_9, question_10)
    answer_1 = 'xã hội'
    answer_2 = 'quần đảo'
    answer_3 = 'con tim'
    answer_4 = 'đường đời'
    answer_5 = 'tay phải'
    answer_6 = 'nhà nước'
    answer_7 = 'con người'
    answer_8 = 'sai'
    answer_9 = 'con dốc'
    answer_10 = 'đua xe'
    answers = (answer_1, answer_2, answer_3, answer_4, answer_5, answer_6, answer_7, answer_8, answer_9, answer_10)

    b = random.randint(0, 9)
    a = random.randint(0, 9)
    c = random.randint(0, 9)

    tk = Tk()
    tk.geometry('1080x720')
    tk.title('hello')

    Label(tk, text="\nMini Game\n", font=("Jokerman", 26, "bold", "italic"), fg="red").pack()
    Label(tk, text='\n' + questions[a], font=("Segoe UI", 16), fg="black").pack()
    ques1 = Entry(tk, width=30, font=("Segoe UI", 16), fg="black")
    ques1.pack()
    Label(tk, text='\n' + questions[b], font=("Segoe UI", 16), fg="black").pack()
    ques2 = Entry(tk, width=30, font=("Segoe UI", 16), fg="black")
    ques2.pack()
    Label(tk, text='\n' + questions[c], font=("Segoe UI", 16), fg="black").pack()
    ques3 = Entry(tk, width=30, font=("Segoe UI", 16), fg="black")
    ques3.pack()

    def win_quit():
        mixer.music.load("sound\\win.mp3")
        mixer.music.set_volume(20)
        mixer.music.play()
        time.sleep(2)
        tk.quit()
        tk.destroy()
        menu()

    def lose_quit():
        mixer.music.load("sound\\lose.mp3")
        mixer.music.set_volume(20)
        mixer.music.play()
        time.sleep(2)
        tk.quit()
        tk.destroy()
        menu()

    def ketqua():
        if ques1.get() == answers[a] and ques2.get() == answers[b] and ques3.get() == answers[c]:
            global data
            name = user
            file = open('filesave\\' + 'money' + name + '.txt', mode='a+')
            file.seek(0)
            data = file.readline()
            data = int(data) + 30000
            print(data)
            file.close()
            file = open('filesave\\' + 'money' + name + '.txt', mode='w+')
            file.seek(0)
            file.write(str(data))
            file.close()
            win_quit()
        else:
            Label(tk, text="trả lời sai", font=("Jokerman", 30, "bold", "italic"), fg="red").pack()
            lose_quit()

    Enter = Button(tk, text="Enter", font=("Snap ITC", 16, "bold"),
                   fg="green", width=11, command=ketqua, height=1, relief="groove")
    Enter.pack()
    tk.mainloop()


def choose_car():
    DISPLAY2 = pygame.display.set_mode((width, height))
    pygame.display.set_caption("chon")
    mixer.music.load("sound\\tick.wav")
    mixer.music.set_volume(20)
    mixer.music.play()
    global xechon

    while True:

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.display.quit()

                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:
                # set 5
                if mouse[0] >= 630 and mouse[0] <= 950 and mouse[1] > 580 and mouse[1] <= 650:
                    mixer.music.load("sound\\tick.wav")
                    mixer.music.set_volume(20)
                    mixer.music.play()
                    xechon = 5
                    return choose_size()
                # set 1
                elif mouse[0] >= 630 and mouse[0] <= 950 and mouse[1] >= 300 and mouse[1] <= 370:
                    mixer.music.load("sound\\tick.wav")
                    mixer.music.set_volume(20)
                    mixer.music.play()
                    xechon = 1
                    return choose_size()
                # set 2
                elif mouse[0] >= 630 and mouse[0] <= 950 and mouse[1] > 370 and mouse[1] <= 440:
                    mixer.music.load("sound\\tick.wav")
                    mixer.music.set_volume(20)
                    mixer.music.play()
                    xechon = 2
                    return choose_size()
                # set 3
                elif mouse[0] >= 630 and mouse[0] <= 950 and mouse[1] > 440 and mouse[1] <= 510:
                    mixer.music.load("sound\\tick.wav")
                    mixer.music.set_volume(20)
                    mixer.music.play()
                    xechon = 3
                    return choose_size()
                # set 4
                elif mouse[0] >= 630 and mouse[0] <= 950 and mouse[1] > 510 and mouse[1] <= 580:
                    mixer.music.load("sound\\tick.wav")
                    mixer.music.set_volume(20)
                    mixer.music.play()
                    xechon = 4
                    return choose_size()
                elif mouse[0] >= 630 and mouse[0] <= 950 and mouse[1] > 650 and mouse[1] <= 720:
                    mixer.music.load("sound\\tick.wav")
                    mixer.music.set_volume(20)
                    mixer.music.play()
                    return choose_set()
                else:
                    pass
            else:
                pass
        DISPLAY2.fill((WHITE))
        sf_background = pygame.image.load("image of menu\\bg.png")
        DISPLAY2.blit(sf_background, (0, 0))

        set_game = pygame.image.load('image of menu\\set_duoc_chon.png')
        DISPLAY2.blit(set_game, (630, 230))
        set1 = pygame.image.load('image of menu\\xe1.png')
        set1 = pygame.transform.scale(set1, (150, 65))
        DISPLAY2.blit(set1, (700, 300))
        set2 = pygame.image.load('image of menu\\xe2.png')
        set2 = pygame.transform.scale(set2, (150, 65))
        DISPLAY2.blit(set2, (700, 370))
        set3 = pygame.image.load('image of menu\\xe3.png')
        set3 = pygame.transform.scale(set3, (150, 65))
        DISPLAY2.blit(set3, (700, 440))
        set4 = pygame.image.load('image of menu\\xe4.png')
        set4 = pygame.transform.scale(set4, (150, 65))
        DISPLAY2.blit(set4, (700, 510))
        set5 = pygame.image.load('image of menu\\xe5.png')
        set5 = pygame.transform.scale(set5, (150, 65))
        DISPLAY2.blit(set5, (700, 580))
        back = pygame.image.load('image of menu\\return.png')
        DISPLAY2.blit(back, (650, 650))

        mouse = pygame.mouse.get_pos()

        if mouse[0] >= 630 and mouse[0] <= 950 and mouse[1] >= 300 and mouse[1] <= 370:
            set1 = pygame.image.load('image of menu\\xe1v2.png')
            set1 = pygame.transform.scale(set1, (150, 65))
            DISPLAY2.blit(set1, (700, 300))
        elif mouse[0] >= 630 and mouse[0] <= 950 and mouse[1] > 370 and mouse[1] <= 440:
            set2 = pygame.image.load('image of menu\\xe2v2.png')
            set2 = pygame.transform.scale(set2, (150, 65))
            DISPLAY2.blit(set2, (700, 370))

        elif mouse[0] >= 630 and mouse[0] <= 950 and mouse[1] > 440 and mouse[1] <= 510:
            set3 = pygame.image.load('image of menu\\xe3v2.png')
            set3 = pygame.transform.scale(set3, (150, 65))
            DISPLAY2.blit(set3, (700, 440))

        elif mouse[0] >= 630 and mouse[0] <= 950 and mouse[1] > 510 and mouse[1] <= 580:
            set4 = pygame.image.load('image of menu\\xe4v2.png')
            set4 = pygame.transform.scale(set4, (150, 65))
            DISPLAY2.blit(set4, (700, 510))

        elif mouse[0] >= 630 and mouse[0] <= 950 and mouse[1] > 580 and mouse[1] <= 650:
            set5 = pygame.image.load('image of menu\\xe5v2.png')
            set5 = pygame.transform.scale(set5, (150, 65))
            DISPLAY2.blit(set5, (700, 580))
        elif mouse[0] >= 630 and mouse[0] <= 950 and mouse[1] > 650 and mouse[1] <= 720:
            back = pygame.image.load('image of menu\\returnv2.png')
            DISPLAY2.blit(back, (650, 650))
        else:
            pass

        pygame.display.update()
        DISPLAY2.blit(sf_background, (0, 0))


def choose_animals():
    DISPLAY2 = pygame.display.set_mode((width, height))
    pygame.display.set_caption("đua xe đặt cược")
    mixer.music.load("sound\\tick.wav")
    mixer.music.set_volume(20)
    mixer.music.play()
    global xechon

    while True:

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.display.quit()

                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:
                # set 5
                if mouse[0] >= 630 and mouse[0] <= 950 and mouse[1] > 580 and mouse[1] <= 650:
                    mixer.music.load("sound\\tick.wav")
                    mixer.music.set_volume(20)
                    mixer.music.play()
                    xechon = 5
                    return choose_size()
                # set 1
                elif mouse[0] >= 630 and mouse[0] <= 950 and mouse[1] >= 300 and mouse[1] <= 370:
                    mixer.music.load("sound\\tick.wav")
                    mixer.music.set_volume(20)
                    mixer.music.play()
                    xechon = 1
                    return choose_size()
                # set 2
                elif mouse[0] >= 630 and mouse[0] <= 950 and mouse[1] > 370 and mouse[1] <= 440:
                    mixer.music.load("sound\\tick.wav")
                    mixer.music.set_volume(20)
                    mixer.music.play()
                    xechon = 2
                    return choose_size()
                # set 3
                elif mouse[0] >= 630 and mouse[0] <= 950 and mouse[1] > 440 and mouse[1] <= 510:
                    mixer.music.load("sound\\tick.wav")
                    mixer.music.set_volume(20)
                    mixer.music.play()
                    xechon = 3
                    return choose_size()
                # set 4
                elif mouse[0] >= 630 and mouse[0] <= 950 and mouse[1] > 510 and mouse[1] <= 580:
                    mixer.music.load("sound\\tick.wav")
                    mixer.music.set_volume(20)
                    mixer.music.play()
                    xechon = 4
                    return choose_size()
                elif mouse[0] >= 630 and mouse[0] <= 950 and mouse[1] > 650 and mouse[1] <= 720:
                    mixer.music.load("sound\\tick.wav")
                    mixer.music.set_volume(20)
                    mixer.music.play()
                    return choose_set()
                else:
                    pass
            else:
                pass
        DISPLAY2.fill((WHITE))
        sf_background = pygame.image.load("image of menu\\bg.png")
        DISPLAY2.blit(sf_background, (0, 0))

        set_game = pygame.image.load('image of menu\\set_duoc_chon.png')
        DISPLAY2.blit(set_game, (630, 230))
        set1 = pygame.image.load('image of menu\\canhcut.png')
        set1 = pygame.transform.scale(set1, (150, 65))
        DISPLAY2.blit(set1, (700, 300))
        set2 = pygame.image.load('image of menu\\chim.png')
        set2 = pygame.transform.scale(set2, (150, 65))
        DISPLAY2.blit(set2, (700, 370))
        set3 = pygame.image.load('image of menu\\ga.png')
        set3 = pygame.transform.scale(set3, (150, 65))
        DISPLAY2.blit(set3, (700, 440))
        set4 = pygame.image.load('image of menu\\heo.png')
        set4 = pygame.transform.scale(set4, (150, 65))
        DISPLAY2.blit(set4, (700, 510))
        set5 = pygame.image.load('image of menu\\turtle.png')
        set5 = pygame.transform.scale(set5, (150, 65))
        DISPLAY2.blit(set5, (700, 580))
        back = pygame.image.load('image of menu\\return.png')
        DISPLAY2.blit(back, (650, 650))

        mouse = pygame.mouse.get_pos()

        if mouse[0] >= 630 and mouse[0] <= 950 and mouse[1] >= 300 and mouse[1] <= 370:
            set1 = pygame.image.load('image of menu\\canhcutv2.png')
            set1 = pygame.transform.scale(set1, (150, 65))
            DISPLAY2.blit(set1, (700, 300))
        elif mouse[0] >= 630 and mouse[0] <= 950 and mouse[1] > 370 and mouse[1] <= 440:
            set2 = pygame.image.load('image of menu\\chimv2.png')
            set2 = pygame.transform.scale(set2, (150, 65))
            DISPLAY2.blit(set2, (700, 370))

        elif mouse[0] >= 630 and mouse[0] <= 950 and mouse[1] > 440 and mouse[1] <= 510:
            set3 = pygame.image.load('image of menu\\gav2.png')
            set3 = pygame.transform.scale(set3, (150, 65))
            DISPLAY2.blit(set3, (700, 440))

        elif mouse[0] >= 630 and mouse[0] <= 950 and mouse[1] > 510 and mouse[1] <= 580:
            set4 = pygame.image.load('image of menu\\heov2.png')
            set4 = pygame.transform.scale(set4, (150, 65))
            DISPLAY2.blit(set4, (700, 510))

        elif mouse[0] >= 630 and mouse[0] <= 950 and mouse[1] > 580 and mouse[1] <= 650:
            set5 = pygame.image.load('image of menu\\turtlev2.png')
            set5 = pygame.transform.scale(set5, (150, 65))
            DISPLAY2.blit(set5, (700, 580))
        elif mouse[0] >= 630 and mouse[0] <= 950 and mouse[1] > 650 and mouse[1] <= 720:
            back = pygame.image.load('image of menu\\returnv2.png')
            DISPLAY2.blit(back, (650, 650))
        else:
            pass

        pygame.display.update()
        DISPLAY2.blit(sf_background, (0, 0))


def choose_planes():
    DISPLAY2 = pygame.display.set_mode((width, height))
    pygame.display.set_caption("chon")
    mixer.music.load("sound\\tick.wav")
    mixer.music.set_volume(20)
    mixer.music.play()
    global xechon

    while True:

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.display.quit()

                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:
                # set 5
                if mouse[0] >= 630 and mouse[0] <= 950 and mouse[1] > 580 and mouse[1] <= 650:
                    mixer.music.load("sound\\tick.wav")
                    mixer.music.set_volume(20)
                    mixer.music.play()
                    xechon = 5
                    return choose_size()
                # set 1
                elif mouse[0] >= 630 and mouse[0] <= 950 and mouse[1] >= 300 and mouse[1] <= 370:
                    mixer.music.load("sound\\tick.wav")
                    mixer.music.set_volume(20)
                    mixer.music.play()
                    xechon = 1
                    return choose_size()
                # set 2
                elif mouse[0] >= 630 and mouse[0] <= 950 and mouse[1] > 370 and mouse[1] <= 440:
                    mixer.music.load("sound\\tick.wav")
                    mixer.music.set_volume(20)
                    mixer.music.play()
                    xechon = 2
                    return choose_size()
                # set 3
                elif mouse[0] >= 630 and mouse[0] <= 950 and mouse[1] > 440 and mouse[1] <= 510:
                    mixer.music.load("sound\\tick.wav")
                    mixer.music.set_volume(20)
                    mixer.music.play()
                    xechon = 3
                    return choose_size()
                # set 4
                elif mouse[0] >= 630 and mouse[0] <= 950 and mouse[1] > 510 and mouse[1] <= 580:
                    mixer.music.load("sound\\tick.wav")
                    mixer.music.set_volume(20)
                    mixer.music.play()
                    xechon = 4
                    return choose_size()
                elif mouse[0] >= 630 and mouse[0] <= 950 and mouse[1] > 650 and mouse[1] <= 720:
                    mixer.music.load("sound\\tick.wav")
                    mixer.music.set_volume(20)
                    mixer.music.play()
                    return choose_set()
                else:
                    pass
            else:
                pass
        DISPLAY2.fill((WHITE))
        sf_background = pygame.image.load("image of menu\\bg.png")
        DISPLAY2.blit(sf_background, (0, 0))

        set_game = pygame.image.load('image of menu\\set_duoc_chon.png')
        DISPLAY2.blit(set_game, (630, 230))
        set1 = pygame.image.load('image of menu\\planes1.png')
        set1 = pygame.transform.scale(set1, (150, 65))
        DISPLAY2.blit(set1, (700, 300))
        set2 = pygame.image.load('image of menu\\planes2.png')
        set2 = pygame.transform.scale(set2, (150, 65))
        DISPLAY2.blit(set2, (700, 370))
        set3 = pygame.image.load('image of menu\\planes3.png')
        set3 = pygame.transform.scale(set3, (150, 65))
        DISPLAY2.blit(set3, (700, 440))
        set4 = pygame.image.load('image of menu\\planes4.png')
        set4 = pygame.transform.scale(set4, (150, 65))
        DISPLAY2.blit(set4, (700, 510))
        set5 = pygame.image.load('image of menu\\planes5.png')
        set5 = pygame.transform.scale(set5, (150, 65))
        DISPLAY2.blit(set5, (700, 580))
        back = pygame.image.load('image of menu\\return.png')
        DISPLAY2.blit(back, (650, 650))

        mouse = pygame.mouse.get_pos()

        if mouse[0] >= 630 and mouse[0] <= 950 and mouse[1] >= 300 and mouse[1] <= 370:
            set1 = pygame.image.load('image of menu\\planes1v2.png')
            set1 = pygame.transform.scale(set1, (150, 65))
            DISPLAY2.blit(set1, (700, 300))
        elif mouse[0] >= 630 and mouse[0] <= 950 and mouse[1] > 370 and mouse[1] <= 440:
            set2 = pygame.image.load('image of menu\\planes2v2.png')
            set2 = pygame.transform.scale(set2, (150, 65))
            DISPLAY2.blit(set2, (700, 370))

        elif mouse[0] >= 630 and mouse[0] <= 950 and mouse[1] > 440 and mouse[1] <= 510:
            set3 = pygame.image.load('image of menu\\planes3v2.png')
            set3 = pygame.transform.scale(set3, (150, 65))
            DISPLAY2.blit(set3, (700, 440))

        elif mouse[0] >= 630 and mouse[0] <= 950 and mouse[1] > 510 and mouse[1] <= 580:
            set4 = pygame.image.load('image of menu\\planes4v2.png')
            set4 = pygame.transform.scale(set4, (150, 65))
            DISPLAY2.blit(set4, (700, 510))

        elif mouse[0] >= 630 and mouse[0] <= 950 and mouse[1] > 580 and mouse[1] <= 650:
            set5 = pygame.image.load('image of menu\\planes5v2.png')
            set5 = pygame.transform.scale(set5, (150, 65))
            DISPLAY2.blit(set5, (700, 580))
        elif mouse[0] >= 630 and mouse[0] <= 950 and mouse[1] > 650 and mouse[1] <= 720:
            back = pygame.image.load('image of menu\\returnv2.png')
            DISPLAY2.blit(back, (650, 650))
        else:
            pass

        pygame.display.update()
        DISPLAY2.blit(sf_background, (0, 0))


def choose_motors():
    DISPLAY2 = pygame.display.set_mode((width, height))
    pygame.display.set_caption("chon")
    mixer.music.load("sound\\tick.wav")
    mixer.music.set_volume(20)
    mixer.music.play()
    global xechon

    while True:

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.display.quit()

                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:
                # set 5
                if mouse[0] >= 630 and mouse[0] <= 950 and mouse[1] > 580 and mouse[1] <= 650:
                    mixer.music.load("sound\\tick.wav")
                    mixer.music.set_volume(20)
                    mixer.music.play()
                    xechon = 5
                    return choose_size()
                # set 1
                elif mouse[0] >= 630 and mouse[0] <= 950 and mouse[1] >= 300 and mouse[1] <= 370:
                    mixer.music.load("sound\\tick.wav")
                    mixer.music.set_volume(20)
                    mixer.music.play()
                    xechon = 1
                    return choose_size()
                # set 2
                elif mouse[0] >= 630 and mouse[0] <= 950 and mouse[1] > 370 and mouse[1] <= 440:
                    mixer.music.load("sound\\tick.wav")
                    mixer.music.set_volume(20)
                    mixer.music.play()
                    xechon = 2
                    return choose_size()
                # set 3
                elif mouse[0] >= 630 and mouse[0] <= 950 and mouse[1] > 440 and mouse[1] <= 510:
                    mixer.music.load("sound\\tick.wav")
                    mixer.music.set_volume(20)
                    mixer.music.play()
                    xechon = 3
                    return choose_size()
                # set 4
                elif mouse[0] >= 630 and mouse[0] <= 950 and mouse[1] > 510 and mouse[1] <= 580:
                    mixer.music.load("sound\\tick.wav")
                    mixer.music.set_volume(20)
                    mixer.music.play()
                    xechon = 4
                    return choose_size()
                elif mouse[0] >= 630 and mouse[0] <= 950 and mouse[1] > 650 and mouse[1] <= 720:
                    mixer.music.load("sound\\tick.wav")
                    mixer.music.set_volume(20)
                    mixer.music.play()
                    return choose_set()
                else:
                    pass
            else:
                pass
        DISPLAY2.fill((WHITE))
        sf_background = pygame.image.load("image of menu\\bg.png")
        DISPLAY2.blit(sf_background, (0, 0))

        set_game = pygame.image.load('image of menu\\set_duoc_chon.png')
        DISPLAY2.blit(set_game, (630, 230))
        set1 = pygame.image.load('image of menu\\motor1.png')
        set1 = pygame.transform.scale(set1, (150, 65))
        DISPLAY2.blit(set1, (700, 300))
        set2 = pygame.image.load('image of menu\\motor2.png')
        set2 = pygame.transform.scale(set2, (150, 65))
        DISPLAY2.blit(set2, (700, 370))
        set3 = pygame.image.load('image of menu\\motor3.png')
        set3 = pygame.transform.scale(set3, (150, 65))
        DISPLAY2.blit(set3, (700, 440))
        set4 = pygame.image.load('image of menu\\motor4.png')
        set4 = pygame.transform.scale(set4, (150, 65))
        DISPLAY2.blit(set4, (700, 510))
        set5 = pygame.image.load('image of menu\\motor5.png')
        set5 = pygame.transform.scale(set5, (150, 65))
        DISPLAY2.blit(set5, (700, 580))
        back = pygame.image.load('image of menu\\return.png')
        DISPLAY2.blit(back, (650, 650))

        mouse = pygame.mouse.get_pos()

        if mouse[0] >= 630 and mouse[0] <= 950 and mouse[1] >= 300 and mouse[1] <= 370:
            set1 = pygame.image.load('image of menu\\motor1v2.png')
            set1 = pygame.transform.scale(set1, (150, 65))
            DISPLAY2.blit(set1, (700, 300))
        elif mouse[0] >= 630 and mouse[0] <= 950 and mouse[1] > 370 and mouse[1] <= 440:
            set2 = pygame.image.load('image of menu\\motor2v2.png')
            set2 = pygame.transform.scale(set2, (150, 65))
            DISPLAY2.blit(set2, (700, 370))

        elif mouse[0] >= 630 and mouse[0] <= 950 and mouse[1] > 440 and mouse[1] <= 510:
            set3 = pygame.image.load('image of menu\\motor3v2.png')
            set3 = pygame.transform.scale(set3, (150, 65))
            DISPLAY2.blit(set3, (700, 440))

        elif mouse[0] >= 630 and mouse[0] <= 950 and mouse[1] > 510 and mouse[1] <= 580:
            set4 = pygame.image.load('image of menu\\motor4v2.png')
            set4 = pygame.transform.scale(set4, (150, 65))
            DISPLAY2.blit(set4, (700, 510))

        elif mouse[0] >= 630 and mouse[0] <= 950 and mouse[1] > 580 and mouse[1] <= 650:
            set5 = pygame.image.load('image of menu\\motor5v2.png')
            set5 = pygame.transform.scale(set5, (150, 65))
            DISPLAY2.blit(set5, (700, 580))
        elif mouse[0] >= 630 and mouse[0] <= 950 and mouse[1] > 650 and mouse[1] <= 720:
            back = pygame.image.load('image of menu\\returnv2.png')
            DISPLAY2.blit(back, (650, 650))
        else:
            pass

        pygame.display.update()
        DISPLAY2.blit(sf_background, (0, 0))


def choose_chibi():
    DISPLAY2 = pygame.display.set_mode((width, height))
    pygame.display.set_caption("chon")
    mixer.music.load("sound\\tick.wav")
    mixer.music.set_volume(20)
    mixer.music.play()
    global xechon

    while True:

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.display.quit()

                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:
                # set 5
                if mouse[0] >= 630 and mouse[0] <= 950 and mouse[1] > 580 and mouse[1] <= 650:
                    mixer.music.load("sound\\tick.wav")
                    mixer.music.set_volume(20)
                    mixer.music.play()
                    xechon = 5
                    return choose_size()
                # set 1
                elif mouse[0] >= 630 and mouse[0] <= 950 and mouse[1] >= 300 and mouse[1] <= 370:
                    mixer.music.load("sound\\tick.wav")
                    mixer.music.set_volume(20)
                    mixer.music.play()
                    xechon = 1
                    return choose_size()
                # set 2
                elif mouse[0] >= 630 and mouse[0] <= 950 and mouse[1] > 370 and mouse[1] <= 440:
                    mixer.music.load("sound\\tick.wav")
                    mixer.music.set_volume(20)
                    mixer.music.play()
                    xechon = 2
                    return choose_size()
                # set 3
                elif mouse[0] >= 630 and mouse[0] <= 950 and mouse[1] > 440 and mouse[1] <= 510:
                    mixer.music.load("sound\\tick.wav")
                    mixer.music.set_volume(20)
                    mixer.music.play()
                    xechon = 3
                    return choose_size()
                # set 4
                elif mouse[0] >= 630 and mouse[0] <= 950 and mouse[1] > 510 and mouse[1] <= 580:
                    mixer.music.load("sound\\tick.wav")
                    mixer.music.set_volume(20)
                    mixer.music.play()
                    xechon = 4
                    return choose_size()
                elif mouse[0] >= 630 and mouse[0] <= 950 and mouse[1] > 650 and mouse[1] <= 720:
                    mixer.music.load("sound\\tick.wav")
                    mixer.music.set_volume(20)
                    mixer.music.play()
                    return choose_set()
                else:
                    pass
            else:
                pass
        DISPLAY2.fill((WHITE))
        sf_background = pygame.image.load("image of menu\\bg.png")
        DISPLAY2.blit(sf_background, (0, 0))

        set_game = pygame.image.load('image of menu\\set_duoc_chon.png')
        DISPLAY2.blit(set_game, (630, 230))
        set1 = pygame.image.load('image of menu\\chibi1.png')
        set1 = pygame.transform.scale(set1, (150, 65))
        DISPLAY2.blit(set1, (700, 300))
        set2 = pygame.image.load('image of menu\\chibi2.png')
        set2 = pygame.transform.scale(set2, (150, 65))
        DISPLAY2.blit(set2, (700, 370))
        set3 = pygame.image.load('image of menu\\chibi3.png')
        set3 = pygame.transform.scale(set3, (150, 65))
        DISPLAY2.blit(set3, (700, 440))
        set4 = pygame.image.load('image of menu\\chibi4.png')
        set4 = pygame.transform.scale(set4, (150, 65))
        DISPLAY2.blit(set4, (700, 510))
        set5 = pygame.image.load('image of menu\\chibi5.png')
        set5 = pygame.transform.scale(set5, (150, 65))
        DISPLAY2.blit(set5, (700, 580))

        back = pygame.image.load('image of menu\\return.png')
        DISPLAY2.blit(back, (650, 650))

        mouse = pygame.mouse.get_pos()

        if mouse[0] >= 630 and mouse[0] <= 950 and mouse[1] >= 300 and mouse[1] <= 370:
            set1 = pygame.image.load('image of menu\\chibi1v2.png')
            set1 = pygame.transform.scale(set1, (150, 65))
            DISPLAY2.blit(set1, (700, 300))
        elif mouse[0] >= 630 and mouse[0] <= 950 and mouse[1] > 370 and mouse[1] <= 440:
            set2 = pygame.image.load('image of menu\\chibi2v2.png')
            set2 = pygame.transform.scale(set2, (150, 65))
            DISPLAY2.blit(set2, (700, 370))

        elif mouse[0] >= 630 and mouse[0] <= 950 and mouse[1] > 440 and mouse[1] <= 510:
            set3 = pygame.image.load('image of menu\\chibi3v2.png')
            set3 = pygame.transform.scale(set3, (150, 65))
            DISPLAY2.blit(set3, (700, 440))

        elif mouse[0] >= 630 and mouse[0] <= 950 and mouse[1] > 510 and mouse[1] <= 580:
            set4 = pygame.image.load('image of menu\\chibi4v2.png')
            set4 = pygame.transform.scale(set4, (150, 65))
            DISPLAY2.blit(set4, (700, 510))

        elif mouse[0] >= 630 and mouse[0] <= 950 and mouse[1] > 580 and mouse[1] <= 650:
            set5 = pygame.image.load('image of menu\\chibi5v2.png')
            set5 = pygame.transform.scale(set5, (150, 65))
            DISPLAY2.blit(set5, (700, 580))
        elif mouse[0] >= 630 and mouse[0] <= 950 and mouse[1] > 650 and mouse[1] <= 720:
            back = pygame.image.load('image of menu\\returnv2.png')
            DISPLAY2.blit(back, (650, 650))
        else:
            pass

        pygame.display.update()
        DISPLAY2.blit(sf_background, (0, 0))


def cuahang():
    list_store = [0, 0, 0, 0, 0, 0]

    DISPLAYSURF = pygame.display.set_mode((config.WIDTH, config.HEIGHT))
    pygame.display.set_caption('Đua Xe Đat Cuoc!')
    show.init(DISPLAYSURF)

    while True:
        DISPLAYSURF.fill((255, 255, 255))
        show.Show_Background()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.display.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                # xu ly exit
                mouse = pygame.mouse.get_pos()
                if mouse[0] >= 0 and mouse[0] <= 30 and mouse[1] > 580 and mouse[1] <= 620:

                    mixer.music.load("sound\\tick.wav")
                    mixer.music.set_volume(20)
                    mixer.music.play()
                    return menu()
                else:
                    pass

        x, y = pygame.mouse.get_pos()

        show.Show_Big(0, 264, 209, 271 < x < 354 and 207 < y < 303)

        show.Show_Big(2, 504, 212, 510 < x < 597 and 207 < y < 303)

        pygame.display.update()


def user_win():
    tk = Tk()
    tk.geometry('300x300')
    tk.title("Đua xe cá cược")

    def tk_quit():
        mixer.music.load("sound\\tick.wav")
        mixer.music.set_volume(20)
        mixer.music.play()
        # time.sleep(0.5)
        tk.destroy()
        pygame.display.quit()
        return menu()

    Label(tk, text=user + " win", font=("Jokerman", 16, "bold", "italic"), fg="black").pack()
    Button(tk, text="Back", font=("Snap ITC", 16, "bold"), fg="green",
           width=11, height=1, relief="groove", command=tk_quit).pack()
    tk.mainloop()


def user_lose():
    tk = Tk()
    tk.geometry('300x300')
    tk.title("Đua xe cá cược")

    def tk_quit():
        mixer.music.load("sound\\tick.wav")
        mixer.music.set_volume(20)
        mixer.music.play()
        # time.sleep(0.5)
        tk.destroy()
        pygame.display.quit()
        return menu()

    Label(tk, text=user + " thua", font=("Jokerman", 16, "bold", "italic"), fg="black").pack()
    Button(tk, text="Back", font=("Snap ITC", 16, "bold"), fg="green",
           width=11, height=1, relief="groove", command=tk_quit).pack()
    tk.mainloop()


if __name__ == '__main__':
    Sign_in()
