import random

##### Игра  X - 0

# Отображение поля
def show():
        print()
        print('    0   1   2')
        for i in range(3):
                print(i,' ', m[i][0],' ',m[i][1],' ',m[i][2])
        print()


# Ход игрока
def go_gamer():
        while True:
                xy_str = input('Ваш ход (x y) 0..2: ').split()
                if not(len(xy_str) == 2):
                        print('Введите 2 числа через пробел!')
                else:
                        x = int(xy_str[0])
                        y = int(xy_str[1])
                        if (0 <= x <= 2) and (0 <= y <= 2):
                                x = int(xy_str[0])
                                y = int(xy_str[1])

                                if m[x][y] != '-':
                                        print('Эта ячейка занята!')
                                else:
                                        m[x][y] = user_symbol
                                        break
                        else:
                                print('Введите корректные числа от 0 до 2!')


# Ход ПК
def go_pc():
        while True:
                xr = random.randint(0, 2)
                yr = random.randint(0, 2)
                if m[xr][yr] == '-':
                        m[xr][yr] = pc_symbol
                        print('Ход ПК: ', xr, ' ', yr)
                        break

def next_step():  # Проверка наличие еще шагов
        step_next = False
        for i in range(3):
                if '-' in m[i]:
                        step_next = True  # есть еще ход
                        break
        return step_next



def get_winner(): # Проверка на выигрыш
        res = ''
        for i in range(3):
                if m[i][0] == m[i][1] == m[i][2] == user_symbol:
                        res = 'WIN_USER'  # выигрыш пользователя
                        break

                if m[0][i] == m[1][i] == m[2][i] == user_symbol:
                        res = 'WIN_USER'  # выигрыш пользователя
                        break

                if m[i][0] == m[i][1] == m[i][2] == pc_symbol:
                        res = 'WIN_PC'  # выигрыш PC
                        break

                if m[0][i] == m[1][i] == m[2][i] == pc_symbol:
                        res = 'WIN_PC'  # выигрыш PC
                        break

        if m[0][0] == m[1][1] == m[2][2] == user_symbol:
                res = 'WIN_USER'  # выигрыш пользователя

        if m[2][0] == m[1][1] == m[0][2] == user_symbol:
                res = 'WIN_USER'  # выигрыш пользователя

        if m[0][0] == m[1][1] == m[2][2] == pc_symbol:
                res = 'WIN_PC'  # выигрыш PC

        if m[2][0] == m[1][1] == m[0][2] == pc_symbol:
                res = 'WIN_PC'  # выигрыш PC

        return res


# НАЧАЛО
# Инициализация поля и игроков
m = [['-' for j in range(3)] for i in range(3)]
user_symbol = input('Чем играете? X/0: ')
if user_symbol.upper() == 'X':
        pc_symbol = '0'
        step_pc = False
else:
        pc_symbol = 'X'
        step_pc = True

status = ''

while (not status) and next_step():
        if step_pc:
                go_pc()
        else:
                go_gamer()
        status = get_winner()
        show()
        step_pc = not step_pc

if get_winner() == 'WIN_PC':
        print('ВЫИГРАЛ ПК!')
elif get_winner() == 'WIN_USER':
        print('ПОЗДРАВЛЯЮ ВАС С ПОБЕДОЙ!')
else:
        print('ШАГИ ЗАКОНЧИЛИСЬ')