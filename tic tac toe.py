field = list(range(1, 10))
winning_combinations = [
    (1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 5, 9), (3, 5, 7),
    (1, 4, 7), (2, 5, 8), (3, 6, 9)
]
name_x = input("Введите имя игрока Х")
name_o = input("Введите имя игрока О")

def draw_field():
    print('-' * 13)
    for i in range(3):
        print(f'|', field[0 + i * 3], '|', field[1 + i * 3], '|', field[2 + i * 3], "|")
        print("-" * 13)


def take_input(player_sign):
    while True:
        value = input("Куда ставить:" + player_sign + "?")
        if not (value in '123456789'):
            print("Ошибка ввода, поле игры от 1 до 9! Повторите ввод")
            continue
        value = int(value)
        if str(field[value - 1]) in "XO":
            print("Эта клетка занята!")
            continue
        field[value - 1] = player_sign
        break


def win_lines():
    for i in winning_combinations:
        if field[i[0] - 1] == field[i[1] - 1] == field[i[2] - 1]:
            return field[i[1] - 1]
    else:
        return False


def main():
    counter = 0
    while True:
        draw_field()
        if counter % 2 == 0:
            take_input("X")
        else:
            take_input("O")
        if counter > 3:
            winner = win_lines()
            if winner:
                draw_field()
                print("Кто чемпион?!", winner, "чемпион!!!!")
                break
        counter += 1
        if counter > 8:
            draw_field()
            print("Ничья")
            break


main()
