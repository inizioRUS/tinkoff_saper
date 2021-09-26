from boars import Board
import time
import cryptocode


def check_input(args):
    if len(args) != 3 and len(args) != 1 and len(args) != 4 and len(args) != 2:
        return False, ''
    if args[0] not in ['start', 'save', 'flag', 'open', 'openfile']:
        return False, ''
    return True, args


def start(args):
    if len(args) != 4:
        return "Не удачное создание", False
    if not (args[1].isdigit() and args[2].isdigit() and args[3].isdigit()):
        return "Не удачное создание", False
    args[1] = max(int(args[1]), 5)
    args[2] = max(int(args[2]), 5)
    args[1] = min(100, args[1])
    args[2] = min(100, args[2])
    args[3] = max(1, int(args[3]))
    args[3] = min(int(args[1] * args[2] * (1 / 7)), args[3])
    return "Поле создано", True, Board(int(args[1]), int(args[2]), int(args[3]))


def save(b, pas):
    with open(f"{time.time()}.txt", 'w') as file:
        file.write(b.save(pas))
    return ["Все сохраненно"]


def open_file(args, main_password):
    if len(args) != 2:
        return "ошибка", False
    try:
        with open(args[1], "r") as data:
            s = data.read()
        a = cryptocode.decrypt(s, main_password).split(" ")
        if a[-1] != "tisgfd":
            return "не правильный файл", False
        a = a[:-1]
        return "игра началась", True, Board(int(a[0].split("/")[0]), int(a[0].split("/")[1]), 0, False, a[1:])
    except Exception as e:
        return ["ошибка", False]


def do_in_game(args, b):
    if len(args) != 3:
        return "Не приавльно указаны цифры", False, True
    what_do, x, y = args
    if not (args[1].isdigit() and args[2].isdigit()):
        return "Не приавльно указаны цифры", False, True
    x = int(x)
    y = int(y)
    if (x < 0 or x > b.w or y < 0 or y > b.h):
        return "Не приавльно указаны цифры", False, True
    a = b.update(what_do, x, y)
    return ["ок", True, a]
