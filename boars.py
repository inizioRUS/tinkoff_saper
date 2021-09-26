import random
import cryptocode


class Board:
    def __init__(self, w, h, bomb_count, new=True, data=[]):
        self.w = w
        self.h = h
        self.cells = {}
        self.bomb_count = bomb_count
        self.count_flag = 0
        for x in range(w):
            self.cells[x] = {}
        self.open = 0
        if new:
            for x in range(w):
                for y in range(h):
                    self.cells[x][y] = Cell("clear", x, y, w, h)
            for i in range(bomb_count):
                x, y = random.choice(range(w)), random.choice(range(h))
                while self.cells[x][y].type == "bomb":
                    x, y = random.choice(range(0, w)), random.choice(range(0, h))
                self.cells[x][y].type = "bomb"
                for j in self.cells[x][y].give_list_around_object():
                    self.cells[j[0]][j[1]].digit += 1
        else:
            for i in data:
                i = i.split("/")
                objectt = Cell(i[0], int(i[1]), int(i[2]), self.w, self.h)
                objectt.digit = int(i[3])
                objectt.close = int(i[4])
                objectt.flag = int(i[5])
                self.cells[int(i[1])][int(i[2])] = objectt

    def save(self, password):
        s = f"{self.w}/{self.h} "
        for i in list(self.cells.keys()):
            for j in list(self.cells[i].keys()):
                a = self.cells[i][j]
                s += a.type + "/" + str(a.x) + "/" + str(a.y) + "/" + str(a.digit) + "/" + str(a.close) + "/" + str(
                    a.flag) + " "
        s += "tisgfd"
        return cryptocode.encrypt(s, password)

    def output(self):
        print("_", end="\t")
        print("_", end="\t")
        for i in range(self.w):
            print(i + 1, end="\t")
        print()
        for i in range(self.w + 2):
            print("_", end="\t")
        print()
        for i in range(self.w):
            print(i + 1, end="\t")
            print("|", end="\t")
            for j in range(self.h):
                if self.cells[i][j].close:
                    print("f" if self.cells[i][j].flag else "*", end="\t")
                else:
                    print(self.cells[i][j].digit, end="\t")
            print()

    def update(self, what_do, x, y):
        x -= 1
        y -= 1
        if what_do.lower() == "flag":
            if self.cells[x][y].close:
                self.cells[x][y].flag = 0 if self.cells[x][y].flag else 1
                self.open += 1 if self.cells[x][y].flag else -1
                self.count_flag += 1 if self.cells[x][y].flag else -1
                return True
            else:
                print("Клетка уже открыта")
                return True
        elif what_do.lower() == "open":
            if self.cells[x][y].type == "bomb":
                print("Вы пройграли")
                return False
            elif not self.cells[x][y].close:
                print("Вы уже открыли")
                return True
            elif self.cells[x][y].flag:
                print("Здесь флаг")
                return True
            else:
                was = []
                what_check = [(x, y)]
                what_open = [(x, y)]
                while what_check:
                    a = what_check.pop()
                    was.append(a)
                    if self.cells[a[0]][a[1]].digit == 0:
                        for j in self.cells[a[0]][a[1]].give_list_around_object():
                            if j not in what_open:
                                what_open.append(j)
                            if j not in was:
                                what_check.append(j)
                for i in what_open:
                    self.cells[i[0]][i[1]].close = 0
                    self.open += 1
                return True

    def check_win(self, flag):
        if not (flag):
            return flag
        if self.w * self.h == self.open and self.bomb_count == self.count_flag:
            print("Победа")
            return False
        return True

    def last_output(self):
        print("_", end="\t")
        print("_", end="\t")
        for i in range(self.w):
            print(i + 1, end="\t")
        print()
        for i in range(self.w + 2):
            print("_", end="\t")
        print()
        for i in range(self.w):
            print(i + 1, end="\t")
            print("|", end="\t")
            for j in range(self.h):
                if self.cells[i][j].type == "bomb":
                    print("b", end="\t")
                else:
                    print(self.cells[i][j].digit, end="\t")
            print()


class Cell:
    def __init__(self, type, x, y, w, h):
        self.x = x
        self.y = y
        self.type = type
        self.digit = 0
        self.close = 1
        self.flag = 0
        self.list_around_object = [(x + i, y + j) for i in range(-1, 2) for j in range(-1, 2) if
                                   (i != 0 or j != 0) and -1 < x + i < w and -1 < y + j < h]

    def give_list_around_object(self):
        return self.list_around_object
