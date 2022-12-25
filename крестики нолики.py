from colorama import Fore

name_x = input("Введите имя игрока Х")
name_O = input("Введите имя игрока O")
field = [["-"] * 3 for _ in range(3)]


def game_rules():
    print(Fore.LIGHTRED_EX + "------------------------------")
    print("   Приветствуем Вас в игре    ")
    print("       Крестики нолики        ")
    print(" Используйте числа от 0 до 2")
    print("  что бы поставить х или о    ")
    print("Сначала выбирите   x - строка ")
    print("затем выбирите   y - столбец  ")
    print(" И пусть победит сильнейщий!")
    print("------------------------------")


def show_field():
    print(Fore.LIGHTGREEN_EX + "  | 0 | 1 | 2 |")
    for i, row in enumerate(field):
        row_str = f"{i} | {' | '.join(row)} |"
        print(Fore.LIGHTGREEN_EX + row_str)
        print(Fore.LIGHTGREEN_EX + "-" * 15)
    print()


def plaing_input():
    while True:
        cords = input("         Ваш ход: ").split()
        if len(cords) != 2:
            print(Fore.RED + "Введите 2 координаты через пробел")
            continue
        x, y = cords
        if not (x.isdigit()) or not (y.isdigit()):
            print(Fore.RED + " Введите числа от 0 до 2! ")
            continue

        x, y = int(x), int(y)

        if 0 > x or x > 2 and 0 > y or y > 2:
            print(Fore.RED + "Координаты вне поля игры")
            continue

        if field[x][y] != "-":
            print(Fore.RED + " Клетка занята! Введите другие координаты ")
            continue
        return x, y


def wins_combination():
    win_cord = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for cord in win_cord:
        symbols = []
        for c in cord:
            symbols.append(field[c[0]][c[1]])
        if symbols == ["X", "X", "X"]:
            print(f"Выиграл  {name_x}!!!")
            return True
        if symbols == ["0", "0", "0"]:
            print(f"Выиграл {name_O}!!!")
            return True
    return False


def game():
    game_rules()
    count = 0
    while True:
        show_field()
        count += 1
        if count % 2 == 1:
            print(Fore.LIGHTYELLOW_EX + f"Ходит игрок {name_x} Х")
        else:
            print(Fore.LIGHTCYAN_EX + f"Ходит игрок {name_O} О ")

        x, y = plaing_input()

        if count % 2 == 1:
            field[x][y] = "X"
        else:
            field[x][y] = "O"
        if wins_combination():
            show_field()
            break
        if count == 9:
            print("Ничья")
            show_field()
            break


game()
