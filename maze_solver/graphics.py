import time
import random
from tkinter import Tk, Canvas


class Maze:
    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            win,
            seed =  None
    ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self._create_cells()
        self.seed = seed
        if seed is not None:
            random.seed(seed)

        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)

    def _create_cells(self):
        self._cells = []
        for i in range(self.num_rows):
            row = []
            for j in range(self.num_cols):
                # create a cell at position (i, j)
                cell = Cell(0, 0, 0, 0, self.win) # will set actual coordinates in _draw_cell
                row.append(cell)
            self._cells.append(row)

        # draw cells
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                self._draw_cells(i, j)

    def _draw_cells(self, i, j):
        # calculate x1, y1 based on i, j, self.x1, self.y1 and cell size
        x1 = self.x1 + (j * self.cell_size_x)
        y1 = self.y1 + (i * self.cell_size_y)
        x2 = x1 + self.cell_size_x
        y2 = y1 + self.cell_size_y

        # update the cells coordinates
        cell = self._cells[i][j]
        cell._Cell__x1 = x1
        cell._Cell__x2 = x2
        cell._Cell__y1 = y1
        cell._Cell__y2 = y2

        cell._draw_cell()
        self._animate()

    def _animate(self):
        self.win.redraw()
        time.sleep(0.3)

    def _break_entrance_and_exit(self):
        top_cell = self._cells[0][0]
        bottom_cell = self._cells[-1][-1]

        top_cell.has_top_wall = False
        top_cell._draw_cell()
        bottom_cell.has_bottom_wall = False
        bottom_cell._draw_cell()

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            next_index_list = []

            # determine which cell(s) to visit next
            # left
            if i > 0 and not self._cells[i - 1][j].visited:
                next_index_list.append((i - 1, j))
            # right
            if i < self.num_cols - 1 and not self._cells[i + 1][j].visited:
                next_index_list.append((i + 1, j))
            # up
            if j > 0 and not self._cells[i][j - 1].visited:
                next_index_list.append((i, j - 1))
            # down
            if j < self.num_rows - 1 and not self._cells[i][j + 1].visited:
                next_index_list.append((i, j + 1))

            if len(next_index_list) == 0:
                return  # If no neighbors are unvisited, return

            # randomly choose the next direction to go
            direction_index = random.randrange(len(next_index_list))
            next_index = next_index_list[direction_index]

            # knock out walls between this cell and the next cell(s)
            self._break_walls_between(i, j, next_index[0], next_index[1])

            # recursively visit the next cell
            self._break_walls_r(next_index[0], next_index[1])



    def _break_walls_between(self, i, j, ni, nj):
        # right
        if ni == i + 1:
            self._cells[i][j].has_right_wall = False
            self._cells[ni][nj].has_left_wall = False
        # left
        if ni == i - 1:
            self._cells[i][j].has_left_wall = False
            self._cells[ni][nj].has_right_wall = False
        # down
        if nj == j + 1:
            self._cells[i][j].has_bottom_wall = False
            self._cells[ni][nj].has_top_wall = False
        # up
        if nj == j - 1:
            self._cells[i][j].has_top_wall = False
            self._cells[ni][nj].has_bottom_wall = False

        # Redraw only the affected cells
        self._cells[i][j]._draw_cell()
        self._cells[ni][nj]._draw_cell()

        # Animate after the walls have been redrawn
        self._animate()





class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line:
    def __init__(self, p1: Point, p2: Point):
        self.p1 = p1
        self.p2 = p2

    def draw(self, canvas, fill_color):
        print(f"Drawing line from ({self.p1.x}, {self.p1.y}) to ({self.p2.x}, {self.p2.y}) with color {fill_color}")
        line = canvas.create_line(self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill=fill_color, width=2)
        print(f"Line ID: {line}")  # Added debug statement to see if the line gets created


class Cell:
    def __init__(self, x1, x2, y1, y2, win, has_left_wall=True, has_right_wall=True,
                 has_top_wall=True, has_bottom_wall=True, visited=False):
        self.has_left_wall = has_left_wall
        self.has_right_wall = has_right_wall
        self.has_top_wall = has_top_wall
        self.has_bottom_wall = has_bottom_wall
        self.__x1 = x1
        self.__x2 = x2
        self.__y1 = y1
        self.__y2 = y2
        self.__win = win
        self.visited = visited

    def _draw_cell(self):
        if self.has_left_wall:
            line = Line(Point(self.__x1, self.__y1), Point(self.__x1, self.__y2))
            self.__win.draw_line(line, "red")
        if self.has_top_wall:
            line = Line(Point(self.__x1, self.__y1), Point(self.__x2, self.__y1))
            self.__win.draw_line(line, "red")
        if self.has_right_wall:
            line = Line(Point(self.__x2, self.__y1), Point(self.__x2, self.__y2))
            self.__win.draw_line(line, "red")
        if self.has_bottom_wall:
            line = Line(Point(self.__x1, self.__y2), Point(self.__x2, self.__y2))
            self.__win.draw_line(line, "red")
        if not self.has_top_wall:
            line = Line(Point(self.__x1, self.__y1), Point(self.__x2, self.__y1))
            self.__win.draw_line(line, "#d9d9d9")
        if not self.has_bottom_wall:
            line = Line(Point(self.__x1, self.__y2), Point(self.__x2, self.__y2))
            self.__win.draw_line(line, "#d9d9d9")

    def draw_move(self, to_cell, undo=False):
        # cell1 ( x1 y1 ), ( x2 y2 ) cell2 ( x3 y3 ) ( x4 y4 )
        # take a point from each cell.
        # create line from those points
        # draw the line
        line = Line(Point(self.__x1, self.__y2), Point(to_cell.__x1, to_cell.__y1))
        if undo:
            self.__win.draw_line(line, "red")
        else:
            self.__win.draw_line(line, "gray")


class Window:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self._root_widget = Tk()
        self.__canvas = Canvas(self._root_widget, width=self.width, height=self.height)
        self.__canvas.pack()  # Packs the canvas into the window
        self._root_widget.title(f"w:{self.width}, h:{self.height}")
        self._running = True  # Initialize as True to enter the loop

        # Bind the close event properly
        self._root_widget.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self._root_widget.update_idletasks()
        self._root_widget.update()

    def wait_for_close(self):
        # No need to reset self._running here
        while self._running:
            self.redraw()

    def close(self):
        self._running = False
        self._root_widget.destroy()  # Properly close the window

    def draw_line(self, ln: Line, fill_color):
        ln.draw(self.__canvas, fill_color)
        self.redraw()  # Force the window to refresh right after drawing the line


