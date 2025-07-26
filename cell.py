from graphics import Window, Point, Line


class Cell:
    def __init__(self, window: Window = None) -> None:
        self.__win = window

        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True

        self.visited = False

        self.__x1 = -1
        self.__x2 = -1
        self.__y1 = -1
        self.__y2 = -1

    def draw(self, x1, y1, x2, y2):
        if self.__win is None:
            return

        self.__x1 = x1
        self.__x2 = x2
        self.__y1 = y1
        self.__y2 = y2

        l = Line(Point(self.__x1, self.__y1), Point(self.__x1, self.__y2))
        if self.has_left_wall:
            self.__win.draw_line(l, "black")
        else:
            self.__win.draw_line(l, "white")

        l = Line(Point(self.__x2, self.__y1), Point(self.__x2, self.__y2))
        if self.has_right_wall:
            self.__win.draw_line(l, "black")
        else:
            self.__win.draw_line(l, "white")

        l = Line(Point(self.__x1, self.__y1), Point(self.__x2, self.__y1))
        if self.has_top_wall:
            self.__win.draw_line(l, "black")
        else:
            self.__win.draw_line(l, "white")

        l = Line(Point(self.__x1, self.__y2), Point(self.__x2, self.__y2))
        if self.has_bottom_wall:
            self.__win.draw_line(l, "black")
        else:
            self.__win.draw_line(l, "white")

    def draw_move(self, to_cell: "Cell", undo=False):
        center_x = (self.__x1 + self.__x2) // 2
        center_y = (self.__y1 + self.__y2) // 2

        to_center_x = (to_cell.__x1 + to_cell.__x2) // 2
        to_center_y = (to_cell.__y1 + to_cell.__y2) // 2

        l = Line(Point(center_x, center_y), Point(to_center_x, to_center_y))

        if undo:
            self.__win.draw_line(l, "gray")
        else:
            self.__win.draw_line(l, "red")
