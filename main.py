"""«Ним». Имеется три кучки спичек. Двое играющих по очереди делают ходы. Каждый ход заключается в том,
что из одной какой-то кучки берется произвольное ненулевое число спичек. Выигрывает взявший последнюю спичку.
Реализовать два режима: «компьютер-человек» и «человек-человек»."""
import random
import time
from random import randint
from random import randrange
class color:
    RED = '\033[91m'
    END = '\033[0m'
    BLUE = '\033[94m'
    YELLOW = '\033[93m'
    PURPLE = '\033[95m'
    DARKCYAN = '\033[36m'
    GREEN = '\033[92m'
    CYAN = '\033[96m'
    PLAYER = '\033[97m'
ky = 1
j = 1
key2 = 1
while ky == 1 and j == 1:
    print("Введите цифру:")
    print(color.GREEN + "1 - НОВАЯ ИГРА" + color.END)
    print(color.RED + "0 - ЗАКОНЧИТЬ ИГРУ" + color.END)
    key = int(input())
    if key == 1:
        ky = 0
        j = 0
        print("Укажите кол-во спичек в кучках:")
        print("Чтобы сгенерировать случайное кол-во спичек введите -1.")
        time.sleep(3)
        print("Введите кол-во спичек в 1-ой кучке: ")
        a = int(input())
        if a == -1:
            a = randint(0, 1000)
        print("Введите кол-во спичек в 2-ой кучке: ")
        b = int(input())
        if b == -1:
            b = randint(0, 1000)
        print("Введите кол-во спичек в 3-ой кучке: ")
        c = int(input())
        if c == -1:
            c = randint(0, 1000)
        if a >= 0 and b >= 0 and c >= 0:
            print(color.DARKCYAN + "В 1-ой кучке - ", a, " спичек." + color.END)
            print(color.YELLOW + "В 2-ой кучке - ", b, " спичек." + color.END)
            print(color.BLUE + "В 3-ой кучке - ", c, " спичек.\n" + color.END)
            time.sleep(2)
            key2 = 0
            print("Введите цифру: 1 - «компьютер-человек», 0 - «человек-человек»")
            d = int(input())
            if d == 1:
                z = 0
                print("Вы выбрали режим - «компьютер-человек»")
                w = 0
                while w == 0:
                    """ИГРОК!!!!!!!!!!"""
                    if z == 1:
                        break
                    if a == 0 and b == 0 and c == 0:
                        print("Все кучки пусты.")
                        print(color.YELLOW + "Ничья...\n" + color.END)
                        j = 1
                        ky = 1
                        z = 1
                        break
                    print("Ваш ход:")
                    r = 1
                    while r == 1:
                        r = 0
                        print("Выберите номер кучки: 1 - 1-я кучка, 2 - 2-я кучка, 3 - 3-я кучка:")
                        e = int(input())
                        if e == 1:
                            if a == 1:
                                print("Вы убрали последнюю спичку.")
                                print(color.DARKCYAN + "В 1-ой кучке осталось 0 спичек." + color.END)
                                print(color.PURPLE + "Поздравляем, вы победили!\n" + color.END)
                                j = 1
                                ky = 1
                                z = 1
                                break
                            if a != 0:
                                print("Сколько спичек вы хотите убрать: ")
                                f = int(input())
                                if f <= 0:
                                    print("Ошибка. Выберите положительное число.")
                                    r = 1
                                    continue
                                if f > a:
                                    print("Ошибка. Вы не можете взять больше спичек чем есть в кучке!")
                                    r = 1
                                    continue
                                if f == a:
                                    print("Вы не можете убрать все спички из кучки!")
                                    r = 1
                                    continue
                                q = f % 10
                                if q == 1:
                                    t = (f / 10) - (q / 10)
                                    y = t % 10
                                    if y == 1:
                                        print("Вы убрали", f, "спичек.")
                                    else:
                                        print("Вы убрали", f, "спичку.")
                                elif q > 1 and q < 5:
                                        i = (f / 10) - (q / 10)
                                        m = i % 10
                                        if m == 1:
                                            print("Вы убрали", f, "спичек.")
                                        else:
                                            print("Вы убрали", f, "спички.")
                                else:
                                    print("Вы убрали", f, "спичек.")
                                a = a - f
                                p = a % 10
                                if p == 1:
                                    t = (f / 10) - (q / 10)
                                    y = t % 10
                                    if y == 1:
                                        print(color.DARKCYAN + "В 1-ой кучке осталось" + color.END, a, "спичек.\n")
                                    else:
                                        print(color.DARKCYAN + "В 1-ой кучке осталось" + color.END, a, "спичка.\n")
                                elif p > 1 and p < 5:
                                    i = (f / 10) - (q / 10)
                                    m = i % 10
                                    if m == 1:
                                        print(color.DARKCYAN + "В 1-ой кучке осталось" + color.END, a, "спичек.\n")
                                    else:
                                        print(color.DARKCYAN + "В 1-ой кучке осталось" + color.END, a, "спички.\n")
                                else:
                                    print(color.DARKCYAN + "В 1-ой кучке осталось" + color.END, a, "спичек.\n")
                            else:
                                print("Ошибка. 1-я кучка пуста...")
                                print("Выберите другую.")
                                r = 1

                        elif e == 2:
                            if b == 1:
                                print("Вы убрали последнюю спичку.")
                                print(color.YELLOW + "В 2-ой кучке осталось 0 спичек." + color.END)
                                print(color.PURPLE + "Поздравляем, вы победили!\n" + color.END)
                                j = 1
                                ky = 1
                                z = 1
                                break
                            if b != 0:
                                print("Сколько спичек вы хотите убрать: ")
                                f = int(input())
                                if f <= 0:
                                    print("Ошибка. Выберите ненулевое число.")
                                    r = 1
                                    continue
                                if f > b:
                                    print("Ошибка. Вы не можете взять больше спичек чем есть в кучке!")
                                    r = 1
                                    continue
                                if f == b:
                                    print("Вы не можете убрать все спички из кучки!")
                                    r = 1
                                    continue
                                q = f % 10
                                if q == 1:
                                    t = (f / 10) - (q / 10)
                                    y = t % 10
                                    if y == 1:
                                        print("Вы убрали", f, "спичек.")
                                    else:
                                        print("Вы убрали", f, "спичку.")
                                elif q > 1 and q < 5:
                                    i = (f / 10) - (q / 10)
                                    m = i % 10
                                    if m == 1:
                                        print("Вы убрали", f, "спичек.")
                                    else:
                                        print("Вы убрали", f, "спички.")
                                else:
                                    print("Вы убрали", f, "спичек.")
                                b = b - f
                                p = b % 10
                                if p == 1:
                                    t = (f / 10) - (q / 10)
                                    y = t % 10
                                    if y == 1:
                                        print(color.YELLOW + "Во 2-ой кучке осталось" + color.END, b, "спичек.\n")
                                    else:
                                        print(color.YELLOW + "Во 2-ой кучке осталось" + color.END, b, "спичка.\n")
                                elif p > 1 and p < 5:
                                    i = (f / 10) - (q / 10)
                                    m = i % 10
                                    if m == 1:
                                        print(color.YELLOW + "Во 2-ой кучке осталось" + color.END, b, "спичек.\n")
                                    else:
                                        print(color.YELLOW + "Во 2-ой кучке осталось" + color.END, b, "спички.\n")
                                else:
                                    print(color.YELLOW + "Во 2-ой кучке осталось" + color.END, b, "спичек.\n")
                            else:
                                print("Ошибка. 2-я кучка пуста...")
                                print("Выберите другую.")
                                r = 1

                        elif e == 3:
                            if c == 1:
                                print("Вы убрали последнюю спичку.")
                                print(color.BLUE + "В 3-ой кучке осталось 0 спичек." + color.END)
                                print(color.GREEN + "Поздравляем, вы победили!\n" + color.END)
                                j = 1
                                ky = 1
                                z = 1
                                break
                            if b != 0:
                                print("Сколько спичек вы хотите убрать: ")
                                f = int(input())
                                if f <= 0:
                                    print("Ошибка. Выберите ненулевое число.")
                                    r = 1
                                    continue
                                if f > c:
                                    print("Ошибка. Вы не можете взять больше спичек чем есть в кучке!")
                                    r = 1
                                    continue
                                if f == c:
                                    print("Вы не можете убрать все спички из кучки!")
                                    r = 1
                                    continue
                                q = f % 10
                                if q == 1:
                                    t = (f / 10) - (q / 10)
                                    y = t % 10
                                    if y == 1:
                                        print("Вы убрали", f, "спичек.")
                                    else:
                                        print("Вы убрали", f, "спичку.")
                                elif q > 1 and q < 5:
                                    i = (f / 10) - (q / 10)
                                    m = i % 10
                                    if m == 1:
                                        print("Вы убрали", f, "спичек.")
                                    else:
                                        print("Вы убрали", f, "спички.")
                                else:
                                    print("Вы убрали", f, "спичек.")
                                c = c - f
                                p = c % 10
                                if p == 1:
                                    t = (f / 10) - (q / 10)
                                    y = t % 10
                                    if y == 1:
                                        print(color.BLUE + "В 3-ей кучке осталось" + color.END, c, "спичек.\n")
                                    else:
                                        print(color.BLUE + "В 3-ей кучке осталось" + color.END, c, "спичка.\n")
                                elif p > 1 and p < 5:
                                    i = (f / 10) - (q / 10)
                                    m = i % 10
                                    if m == 1:
                                        print(color.BLUE + "В 3-ей кучке осталось" + color.END, c, "спички.\n")
                                    else:
                                        print(color.BLUE + "В 3-ей кучке осталось" + color.END, c, "спички.\n")
                                else:
                                    print(color.BLUE + "В 3-ей кучке осталось" + color.END, c, "спичек.\n")
                            else:
                                print("Ошибка. 3-я кучка пуста...")
                                print("Выберите другую.")
                                r = 1

                        elif e != 1 and e != 2 and e != 3:
                            print("Ошибка. Выберите 1,2 или 3 кучку.")
                            r = 1






                    """КОМПЬЮТЕР!!!!!!!!!"""
                    if z == 1:
                        break
                    g = randint(1, 3)
                    if a == 1:
                        g = 1
                    if b == 1:
                        g = 2
                    if c == 1:
                        g = 3
                    if a == 0:
                        g = randint(2, 3)
                    if b == 0:
                        g = randrange(1, 3)
                    if c == 0:
                        g = randint(1, 2)
                    if a == 0 and b == 0:
                        g = 3
                    if a == 0 and c == 0:
                        g = 2
                    if b == 0 and c == 0:
                        g = 1
                    if a == 0 and b == 0 and c == 0:
                        print("Все кучки пусты.")
                        print(color.YELLOW + "Ничья..." + color.END)
                        j = 1
                        ky = 1
                        z = 1
                        break
                    if w == 1:
                        g = 5

                    if g == 1:
                        print("Ходит противник...")
                        time.sleep(2)
                        print("Противник выбрал 1-ю кучку")
                        if a == 1:
                            print("Противник убрал последнюю спичку.")
                            print(color.DARKCYAN + "В 1-ой кучке осталось 0 спичек." + color.END)
                            print(color.RED + "К сожалению, вы проиграли...\n" + color.END)
                            j = 1
                            ky = 1
                            z = 1
                            break
                        h = randint(1, a-1)
                        q = h % 10
                        if q == 1:
                            t = (h / 10) - (q / 10)
                            y = t % 10
                            if y == 1:
                                print("Противник убрал", h, "спичек.")
                            else:
                                print("Противник убрал", h, "спичку.")
                        elif q > 1 and q < 5:
                            i = (h / 10) - (q / 10)
                            m = i % 10
                            if m == 1:
                                print("Противник убрал", h, "спичек.")
                            else:
                                print("Противник убрал", h, "спички.")
                        else:
                            print("Противник убрал", h, "спичек.")
                        a = a - h
                        p = a % 10
                        if p == 1:
                            t = (h / 10) - (q / 10)
                            y = t % 10
                            if y == 1:
                                print(color.DARKCYAN + "В 1-ой кучке осталось" + color.END, a, "спичек.\n")
                            else:
                                print(color.DARKCYAN + "В 1-ой кучке осталось" + color.END, a, "спичка.\n")
                        elif p > 1 and p < 5:
                            i = (h / 10) - (q / 10)
                            m = i % 10
                            if m == 1:
                                print(color.DARKCYAN + "В 1-ой кучке осталось" + color.END, a, "спичек.\n")
                            else:
                                print(color.DARKCYAN + "В 1-ой кучке осталось" + color.END, a, "спички.\n")
                        else:
                            print(color.DARKCYAN + "В 1-ой кучке осталось" + color.END, a, "спичек.\n")

                    elif g == 2:
                        print("Ходит противник...")
                        time.sleep(2)
                        print("Противник выбрал 2-ю кучку")
                        if b == 1:
                            print("Противник убрал последнюю спичку.")
                            print(color.YELLOW + "В 2-ой кучке осталось 0 спичек." + color.END)
                            print(color.RED + "К сожалению, вы проиграли...\n" + color.END)
                            j = 1
                            ky = 1
                            z = 1
                            break
                        h = randint(1, b-1)
                        q = h % 10
                        if q == 1:
                            t = (h / 10) - (q / 10)
                            y = t % 10
                            if y == 1:
                                print("Противник убрал", h, "спичек.")
                            else:
                                print("Противник убрал", h, "спичку.")
                        elif q > 1 and q < 5:
                            i = (h / 10) - (q / 10)
                            m = i % 10
                            if m == 1:
                                print("Противник убрал", h, "спичек.")
                            else:
                                print("Противник убрал", h, "спички.")
                        else:
                            print("Противник убрал", h, "спичек.")
                        b = b - h
                        p = b % 10
                        if p == 1:
                            t = (h / 10) - (q / 10)
                            y = t % 10
                            if y == 1:
                                print(color.YELLOW + "Во 2-ой кучке осталось" + color.END, b, "спичек.\n")
                            else:
                                print(color.YELLOW + "Во 2-ой кучке осталось" + color.END, b, "спичка.\n")
                        elif p > 1 and p < 5:
                            i = (h / 10) - (q / 10)
                            m = i % 10
                            if m == 1:
                                print(color.YELLOW + "Во 2-ой кучке осталось" + color.END, b, "спичек.\n")
                            else:
                                print(color.YELLOW + "Во 2-ой кучке осталось" + color.END, b, "спички.\n")
                        else:
                            print(color.YELLOW + "Во 2-ой кучке осталось" + color.END, b, "спичек.\n")

                    elif g == 3:
                        print("Ходит противник...")
                        time.sleep(2)
                        print("Противник выбрал 3-ю кучку")
                        if c == 1:
                            print("Противник убрал последнюю спичку.")
                            print(color.BLUE + "В 3-ой кучке осталось 0 спичек." + color.END)
                            print(color.RED + "К сожалению, вы проиграли...\n" + color.END)
                            j = 1
                            ky = 1
                            z = 1
                            break
                        h = randint(1, c-1)
                        q = h % 10
                        if q == 1:
                            t = (h / 10) - (q / 10)
                            y = t % 10
                            if y == 1:
                                print("Противник убрал", h, "спичек.")
                            else:
                                print("Противник убрал", h, "спичку.")
                        elif q > 1 and q < 5:
                            i = (h / 10) - (q / 10)
                            m = i % 10
                            if m == 1:
                                print("Противник убрал", h, "спичек.")
                            else:
                                print("Противник убрал", h, "спички.")
                        else:
                            print("Противник убрал", h, "спичек.")
                        c = c - h
                        p = c % 10
                        if p == 1:
                            t = (t / 10) - (q / 10)
                            y = t % 10
                            if y == 1:
                                print(color.BLUE + "В 3-ей кучке осталось" + color.END, c, "спичек.\n")
                            else:
                                print(color.BLUE + "В 3-ей кучке осталось" + color.END, c, "спичка.\n")
                        elif p > 1 and p < 5:
                            i = (h / 10) - (q / 10)
                            m = i % 10
                            if m == 1:
                                print(color.BLUE + "В 3-ей кучке осталось" + color.END, c, "спички.\n")
                            else:
                                print(color.BLUE + "В 3-ей кучке осталось" + color.END, c, "спички.\n")
                        else:
                            print(color.BLUE + "В 3-ей кучке осталось" + color.END, c, "спичек.\n")
                    elif g == 5:
                        break





            elif d == 0:
                z = 0
                print("Вы выбрали режим - «человек-человек»")
                w = 0
                while w == 0:

                    """ИГРОК № 1  !!!!!!!!!!"""
                    if z == 1:
                        break
                    if a == 0 and b == 0 and c == 0:
                        print("Все кучки пусты.")
                        print(color.YELLOW + "Ничья...\n" + color.END)
                        j = 1
                        ky = 1
                        z = 1
                        break
                    print(color.PLAYER + "Ход игрока № 1:" + color.END)
                    r = 1
                    while r == 1:
                        r = 0
                        print("Выберите номер кучки: 1 - 1-я кучка, 2 - 2-я кучка, 3 - 3-я кучка:")
                        e = int(input())
                        if e == 1:
                            if a == 1:
                                print("Вы убрали последнюю спичку.")
                                print(color.DARKCYAN + "В 1-ой кучке осталось 0 спичек." + color.END)
                                print(color.PURPLE + "Поздравляем, игрок № 1 победил!\n" + color.END)
                                ky = 1
                                j = 1
                                z = 1
                                break
                            if a != 0:
                                print("Сколько спичек вы хотите убрать: ")
                                f = int(input())
                                if f <= 0:
                                    print("Ошибка. Выберите положительное число.")
                                    r = 1
                                    continue
                                if f > a:
                                    print("Ошибка. Вы не можете взять больше спичек чем есть в кучке!")
                                    r = 1
                                    continue
                                if f == a:
                                    print("Вы не можете убрать все спички из кучки!")
                                    r = 1
                                    continue
                                q = f % 10
                                if q == 1:
                                    t = (f / 10) - (q / 10)
                                    y = t % 10
                                    if y == 1:
                                        print("Вы убрали", f, "спичек.")
                                    else:
                                        print("Вы убрали", f, "спичку.")
                                elif q > 1 and q < 5:
                                    i = (f / 10) - (q / 10)
                                    m = i % 10
                                    if m == 1:
                                        print("Вы убрали", f, "спичек.")
                                    else:
                                        print("Вы убрали", f, "спички.")
                                else:
                                    print("Вы убрали", f, "спичек.")
                                a = a - f
                                p = a % 10
                                if p == 1:
                                    t = (f / 10) - (q / 10)
                                    y = t % 10
                                    if y == 1:
                                        print(color.DARKCYAN + "В 1-ой кучке осталось" + color.END, a, "спичек.\n")
                                    else:
                                        print(color.DARKCYAN + "В 1-ой кучке осталось" + color.END, a, "спичка.\n")
                                elif p > 1 and p < 5:
                                    i = (f / 10) - (q / 10)
                                    m = i % 10
                                    if m == 1:
                                        print(color.DARKCYAN + "В 1-ой кучке осталось" + color.END, a, "спичек.\n")
                                    else:
                                        print(color.DARKCYAN + "В 1-ой кучке осталось" + color.END, a, "спички.\n")
                                else:
                                    print(color.DARKCYAN + "В 1-ой кучке осталось" + color.END, a, "спичек.\n")
                            else:
                                print("Ошибка. 1-я кучка пуста...")
                                print("Выберите другую.")
                                r = 1

                        elif e == 2:
                            if b == 1:
                                print("Вы убрали последнюю спичку.")
                                print(color.YELLOW + "В 2-ой кучке осталось 0 спичек." + color.END)
                                print(color.PURPLE + "Поздравляем, игрок № 1 победил!\n" + color.END)
                                j = 1
                                ky = 1
                                z = 1
                                break
                            if b != 0:
                                print("Сколько спичек вы хотите убрать: ")
                                f = int(input())
                                if f <= 0:
                                    print("Ошибка. Выберите ненулевое число.")
                                    r = 1
                                    continue
                                if f > b:
                                    print("Ошибка. Вы не можете взять больше спичек чем есть в кучке!")
                                    r = 1
                                    continue
                                if f == b:
                                    print("Вы не можете убрать все спички из кучки!")
                                    r = 1
                                    continue
                                q = f % 10
                                if q == 1:
                                    t = (f / 10) - (q / 10)
                                    y = t % 10
                                    if y == 1:
                                        print("Вы убрали", f, "спичек.")
                                    else:
                                        print("Вы убрали", f, "спичку.")
                                elif q > 1 and q < 5:
                                    i = (f / 10) - (q / 10)
                                    m = i % 10
                                    if m == 1:
                                        print("Вы убрали", f, "спичек.")
                                    else:
                                        print("Вы убрали", f, "спички.")
                                else:
                                    print("Вы убрали", f, "спичек.")
                                b = b - f
                                p = b % 10
                                if p == 1:
                                    t = (f / 10) - (q / 10)
                                    y = t % 10
                                    if y == 1:
                                        print(color.YELLOW + "Во 2-ой кучке осталось" + color.END, b, "спичек.\n")
                                    else:
                                        print(color.YELLOW + "Во 2-ой кучке осталось" + color.END, b, "спичка.\n")
                                elif p > 1 and p < 5:
                                    i = (f / 10) - (q / 10)
                                    m = i % 10
                                    if m == 1:
                                        print(color.YELLOW + "Во 2-ой кучке осталось" + color.END, b, "спичек.\n")
                                    else:
                                        print(color.YELLOW + "Во 2-ой кучке осталось" + color.END, b, "спички.\n")
                                else:
                                    print(color.YELLOW + "Во 2-ой кучке осталось" + color.END, b, "спичек.\n")
                            else:
                                print("Ошибка. 2-я кучка пуста...")
                                print("Выберите другую.")
                                r = 1

                        elif e == 3:
                            if c == 1:
                                print("Вы убрали последнюю спичку.")
                                print(color.BLUE + "В 3-ой кучке осталось 0 спичек." + color.END)
                                print(color.GREEN + "Поздравляем, игрок № 1 победил!\n" + color.END)
                                j = 1
                                z = 1
                                ky = 1
                                break
                            if b != 0:
                                print("Сколько спичек вы хотите убрать: ")
                                f = int(input())
                                if f <= 0:
                                    print("Ошибка. Выберите ненулевое число.")
                                    r = 1
                                    continue
                                if f > c:
                                    print("Ошибка. Вы не можете взять больше спичек чем есть в кучке!")
                                    r = 1
                                    continue
                                if f == c:
                                    print("Вы не можете убрать все спички из кучки!")
                                    r = 1
                                    continue
                                q = f % 10
                                if q == 1:
                                    t = (f / 10) - (q / 10)
                                    y = t % 10
                                    if y == 1:
                                        print("Вы убрали", f, "спичек.")
                                    else:
                                        print("Вы убрали", f, "спичку.")
                                elif q > 1 and q < 5:
                                    i = (f / 10) - (q / 10)
                                    m = i % 10
                                    if m == 1:
                                        print("Вы убрали", f, "спичек.")
                                    else:
                                        print("Вы убрали", f, "спички.")
                                else:
                                    print("Вы убрали", f, "спичек.")
                                c = c - f
                                p = c % 10
                                if p == 1:
                                    t = (f / 10) - (q / 10)
                                    y = t % 10
                                    if y == 1:
                                        print(color.BLUE + "В 3-ей кучке осталось" + color.END, c, "спичек.\n")
                                    else:
                                        print(color.BLUE + "В 3-ей кучке осталось" + color.END, c, "спичка.\n")
                                elif p > 1 and p < 5:
                                    i = (f / 10) - (q / 10)
                                    m = i % 10
                                    if m == 1:
                                        print(color.BLUE + "В 3-ей кучке осталось" + color.END, c, "спички.\n")
                                    else:
                                        print(color.BLUE + "В 3-ей кучке осталось" + color.END, c, "спички.\n")
                                else:
                                    print(color.BLUE + "В 3-ей кучке осталось" + color.END, c, "спичек.\n")
                            else:
                                print("Ошибка. 3-я кучка пуста...")
                                print("Выберите другую.")
                                r = 1

                        elif e != 1 and e != 2 and e != 3:
                            print("Ошибка. Выберите 1,2 или 3 кучку.")
                            r = 1

                    """ИГРОК № 2  !!!!!!!!!!"""
                    if z == 1:
                        break
                    if w == 1:
                        break
                    if a == 0 and b == 0 and c == 0:
                        print("Все кучки пусты.")
                        print(color.YELLOW + "Ничья...\n" + color.END)
                        j = 1
                        ky = 1
                        z = 1
                        break
                    print(color.PLAYER + "Ход игрока № 2:" + color.END)
                    r = 1
                    while r == 1:
                        r = 0
                        print("Выберите номер кучки: 1 - 1-я кучка, 2 - 2-я кучка, 3 - 3-я кучка:")
                        e = int(input())
                        if e == 1:
                            if a == 1:
                                print("Вы убрали последнюю спичку.")
                                print(color.DARKCYAN + "В 1-ой кучке осталось 0 спичек." + color.END)
                                print(color.PURPLE + "Поздравляем, игрок № 2 победил!\n" + color.END)
                                j = 1
                                ky = 1
                                z = 1
                                break
                            if a != 0:
                                print("Сколько спичек вы хотите убрать: ")
                                f = int(input())
                                if f <= 0:
                                    print("Ошибка. Выберите положительное число.")
                                    r = 1
                                    continue
                                if f > a:
                                    print("Ошибка. Вы не можете взять больше спичек чем есть в кучке!")
                                    r = 1
                                    continue
                                if f == a:
                                    print("Вы не можете убрать все спички из кучки!")
                                    r = 1
                                    continue
                                q = f % 10
                                if q == 1:
                                    t = (f / 10) - (q / 10)
                                    y = t % 10
                                    if y == 1:
                                        print("Вы убрали", f, "спичек.")
                                    else:
                                        print("Вы убрали", f, "спичку.")
                                elif q > 1 and q < 5:
                                    i = (f / 10) - (q / 10)
                                    m = i % 10
                                    if m == 1:
                                        print("Вы убрали", f, "спичек.")
                                    else:
                                        print("Вы убрали", f, "спички.")
                                else:
                                    print("Вы убрали", f, "спичек.")
                                a = a - f
                                p = a % 10
                                if p == 1:
                                    t = (f / 10) - (q / 10)
                                    y = t % 10
                                    if y == 1:
                                        print(color.DARKCYAN + "В 1-ой кучке осталось" + color.END, a, "спичек.\n")
                                    else:
                                        print(color.DARKCYAN + "В 1-ой кучке осталось" + color.END, a, "спичка.\n")
                                elif p > 1 and p < 5:
                                    i = (f / 10) - (q / 10)
                                    m = i % 10
                                    if m == 1:
                                        print(color.DARKCYAN + "В 1-ой кучке осталось" + color.END, a, "спичек.\n")
                                    else:
                                        print(color.DARKCYAN + "В 1-ой кучке осталось" + color.END, a, "спички.\n")
                                else:
                                    print(color.DARKCYAN + "В 1-ой кучке осталось" + color.END, a, "спичек.\n")
                            else:
                                print("Ошибка. 1-я кучка пуста...")
                                print("Выберите другую.")
                                r = 1

                        elif e == 2:
                            if b == 1:
                                print("Вы убрали последнюю спичку.")
                                print(color.YELLOW + "В 2-ой кучке осталось 0 спичек." + color.END)
                                print(color.PURPLE + "Поздравляем, игрок № 2 победил!\n" + color.END)
                                j = 1
                                ky = 1
                                z = 1
                                break
                            if b != 0:
                                print("Сколько спичек вы хотите убрать: ")
                                f = int(input())
                                if f <= 0:
                                    print("Ошибка. Выберите ненулевое число.")
                                    r = 1
                                    continue
                                if f > b:
                                    print("Ошибка. Вы не можете взять больше спичек чем есть в кучке!")
                                    r = 1
                                    continue
                                if f == b:
                                    print("Вы не можете убрать все спички из кучки!")
                                    r = 1
                                    continue
                                q = f % 10
                                if q == 1:
                                    t = (f / 10) - (q / 10)
                                    y = t % 10
                                    if y == 1:
                                        print("Вы убрали", f, "спичек.")
                                    else:
                                        print("Вы убрали", f, "спичку.")
                                elif q > 1 and q < 5:
                                    i = (f / 10) - (q / 10)
                                    m = i % 10
                                    if m == 1:
                                        print("Вы убрали", f, "спичек.")
                                    else:
                                        print("Вы убрали", f, "спички.")
                                else:
                                    print("Вы убрали", f, "спичек.")
                                b = b - f
                                p = b % 10
                                if p == 1:
                                    t = (f / 10) - (q / 10)
                                    y = t % 10
                                    if y == 1:
                                        print(color.YELLOW + "Во 2-ой кучке осталось" + color.END, b, "спичек.\n")
                                    else:
                                        print(color.YELLOW + "Во 2-ой кучке осталось" + color.END, b, "спичка.\n")
                                elif p > 1 and p < 5:
                                    i = (f / 10) - (q / 10)
                                    m = i % 10
                                    if m == 1:
                                        print(color.YELLOW + "Во 2-ой кучке осталось" + color.END, b, "спичек.\n")
                                    else:
                                        print(color.YELLOW + "Во 2-ой кучке осталось" + color.END, b, "спички.\n")
                                else:
                                    print(color.YELLOW + "Во 2-ой кучке осталось" + color.END, b, "спичек.\n")
                            else:
                                print("Ошибка. 2-я кучка пуста...")
                                print("Выберите другую.")
                                r = 1

                        elif e == 3:
                            if c == 1:
                                print("Вы убрали последнюю спичку.")
                                print(color.BLUE + "В 3-ой кучке осталось 0 спичек." + color.END)
                                print(color.GREEN + "Поздравляем, игрок № 2 победил!\n" + color.END)
                                j = 1
                                ky = 1
                                z = 1
                                break
                            if b != 0:
                                print("Сколько спичек вы хотите убрать: ")
                                f = int(input())
                                if f <= 0:
                                    print("Ошибка. Выберите ненулевое число.")
                                    r = 1
                                    continue
                                if f > c:
                                    print("Ошибка. Вы не можете взять больше спичек чем есть в кучке!")
                                    r = 1
                                    continue
                                if f == c:
                                    print("Вы не можете убрать все спички из кучки!")
                                    r = 1
                                    continue
                                q = f % 10
                                if q == 1:
                                    t = (f / 10) - (q / 10)
                                    y = t % 10
                                    if y == 1:
                                        print("Вы убрали", f, "спичек.")
                                    else:
                                        print("Вы убрали", f, "спичку.")
                                elif q > 1 and q < 5:
                                    i = (f / 10) - (q / 10)
                                    m = i % 10
                                    if m == 1:
                                        print("Вы убрали", f, "спичек.")
                                    else:
                                        print("Вы убрали", f, "спички.")
                                else:
                                    print("Вы убрали", f, "спичек.")
                                c = c - f
                                p = c % 10
                                if p == 1:
                                    t = (f / 10) - (q / 10)
                                    y = t % 10
                                    if y == 1:
                                        print(color.BLUE + "В 3-ей кучке осталось" + color.END, c, "спичек.\n")
                                    else:
                                        print(color.BLUE + "В 3-ей кучке осталось" + color.END, c, "спичка.\n")
                                elif p > 1 and p < 5:
                                    i = (f / 10) - (q / 10)
                                    m = i % 10
                                    if m == 1:
                                        print(color.BLUE + "В 3-ей кучке осталось" + color.END, c, "спички.\n")
                                    else:
                                        print(color.BLUE + "В 3-ей кучке осталось" + color.END, c, "спички.\n")
                                else:
                                    print(color.BLUE + "В 3-ей кучке осталось" + color.END, c, "спичек.\n")
                            else:
                                print("Ошибка. 3-я кучка пуста...")
                                print("Выберите другую.")
                                r = 1

                        elif e != 1 and e != 2 and e != 3:
                            print("Ошибка. Выберите 1,2 или 3 кучку.")
                            r = 1




            elif d != 1 and d != 0:
                print("Ошибка. Введите 0 или 1.")
                j = 1
        else:
            print("Ошибка. Кол-во спичек не может быть отрицательным.\n")
            j = 1
            ky = 1
            z = 1
            continue
    elif key == 0:
        ky = 0
        print(color.RED + "Игра окончена." + color.END)
    elif key != 1 and key != 0:
        print("Введите 0 или 1")




