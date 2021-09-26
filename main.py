from sfun import *

flag = True
game_is_start = False
main_password = "9235682479534863h6u693459h8vq3=i9-23cfj3b24454956u945h85ho212[ni41212449"
print(
    "Привет это сапёр, вот перечень всех команд\nstart <ширина поля> <высота поля> <бомбы> - запуск игры(минимальная ширина и высота 5, максимальная 100, минимальное колличество бомб 1, макимальное 1/7 от всех клеток)\n"
    "save - сохраняет текущую игру\nopenfile <путь к файлу> - открывает файл\n"
    "open <координата 1> <координата 2> - открытие клетки\nflag <координата 1> <координата 2> - установка флага\n")
a = input().split()
while flag:
    res = check_input(a)
    if res[0]:
        args = res[1]
        if args[0] == "start":
            if not game_is_start:
                res = start(args)
                game_is_start = res[1]
                if game_is_start:
                    board = res[2]
            else:
                print("Игра уже начата")
        elif args[0] == "save":
            if game_is_start:
                res = save(board, main_password)
            else:
                res = ['Игра не начата']
        elif args[0] == "openfile":
            if not game_is_start:
                res = open_file(args, main_password)
                game_is_start = res[1]
                if game_is_start:
                    board = res[2]
            else:
                res = ["Игра уже начата"]
        else:
            if game_is_start:
                res = do_in_game(args, board)
                flag = res[2]
            else:
                res = ["Игра еще не начата"]
        print(res[0])
    else:
        print("Неправильный ввод")
    if game_is_start:
        flag = board.check_win(flag)
        if flag:
            board.output()
        else:
            board.last_output()
    if flag:
        a = input().split()
input("нажмите любую клавишу для выхода...")
