def greet():
    print('-----------------------')
    print('|  Приветствуем вас   |')
    print('|       в игре        |')
    print('|   крестики-нолики   |')
    print('-----------------------')
    print('|  формат ввода: х у  |')
    print('|  х - номер строки   |')
    print('|  у - номер столбца  |')
    print('| ввод осуществляется |')
    print('|    через пробел     |')
    print('-----------------------')

def show():
    print()
    print("   | 0 | 1 | 2 |")
    print(" ---------------")
    for i, play in enumerate(field):
        play_field = f" {i} | {' | '.join(play)} | "
        print(play_field)
        print(" ---------------")
    print()

def ask():
    while True:
        cord = input("          Ваш ход: ").split()

        if len(cord) != 2:
            print("Введите 2-е координаты: ")
            continue

        x, y = cord

        if not(x.isdigit()) or not(y.isdigit()):
            print("Введите числа! ")
            continue

        x, y = int(x), int(y)

        if 0 > x or x > 2 or 0 > y or y > 2:
            print("Координаты вне диапазона! ")
            continue

        if field[x][y] != " ":
            print("Клетка занята! ")
            continue

        return x, y


def win():
    win_comb = [((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 0), (1, 0), (2, 0)), ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2))]

    for cord in win_comb:
        symbols = []

        for c in cord:
            symbols.append(field[c[0]][c[1]])

            if symbols == ["X", 'X', 'X']:
                show()
                print('!!! Выиграл Х!!!')
                return True
            if symbols == ["0", '0', '0']:
                show()
                print('!!! Выиграл 0!!!')
                return True
    return False

greet()
field = [[" "] * 3 for i in range(3)]
num = 0

while True:
    num += 1

    show()

    if num % 2 == 1:
        print("Ходит крестик")
    else:
        print("Ходит нолик")

    x, y = ask()

    if num % 2 == 1:
        field[x][y] = "X"
    else:
        field[x][y] = "0"

    if win():
        break

    if num == 9:
        print("Ничья")
        break

