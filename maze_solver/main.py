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
        time.sleep(0.7)

    def _break_entrance_and_exit(self):
        top_cell = self._cells[0][0]
        bottom_cell = self._cells[-1][-1]

        top_cell.has_top_wall = False
        top_cell._draw_cell()
        bottom_cell.has_bottom_wall = False
        bottom_cell._draw_cell()

    def _break_walls_r(self, i, j):
        current_cell = self._cells[i][j]
        current_cell.visited = True
        max_i = self.num_cols
        max_j = self.num_rows

        while True:
            path = []  # list to hold i, j
            if i > 0:  # can move up
                adjacent_up = self._cells[i-1][j]
                if adjacent_up.visited == False:
                    path.append((adjacent_up, i-1, j))
            if i < max_i:  # can move down
                adjacent_down = self._cells[i+1][j]
                if adjacent_down.visited == False:
                    path.append((adjacent_down, i+1, j))
            if j > 0:  # can move left
                adjacent_left = self._cells[i][j-1]
                if adjacent_left.visited == False:
                      path.append((adjacent_left, i, j-1))
            if j < max_j:  # can move right
                adjacent_right = self._cells[i][j+1]
                if adjacent_right.visited == False:
                    path.append((adjacent_right, i, j+1))
            if not path:
                current_cell._draw_cell()
                return
            pick_cell = random.choice(path)
            Cell.break_down_walls_between(current_cell, pick_cell[0], i, j, pick_cell[1], pick_cell[2])
            # DFS
            self._break_walls_r(pick_cell[1], pick_cell[2])




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


    def break_down_walls_between(self, to_cell ,i, j, ix, jx):
        #  find indices, based on indices check where cell is located
        if i < ix:  #
            self.has_right_wall = False
            to_cell.has_left_wall = False
        if i > ix:
            self.has_left_wall = False
            to_cell.has_right_wall = False
        if j < jx:  # cell is below
            self.has_bottom_wall = False
            to_cell.has_top_wall = False
        if j > jx: # cell above below
            self.has_top_wall_wall = False
            to_cell.has_bottom_wall = False


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

    # def generate_random_cells(self, num_cells):
    #     cells = []
    #     for i in range(num_cells):
    #         x1 = random.randint(0, self.width - 100)
    #         x2 = x1 + random.randint(50, 150)  # cell width between 50 and 150
    #         y1 = random.randint(0, self.height - 100)
    #         y2 = y1 + random.randint(50, 150)  # cell height between 50 and 150
    #         cell = Cell(x1, x2, y1, y2, self)
    #         cells.append(cell)
    #     return cells

    @staticmethod  # Define main as a static method
    def main():
        win = Window(1280, 720)
        # cells = win.generate_random_cells(8)
        # cell_a = cells[2]
        # cell_b = cells[3]
        # cell_a.draw_move(cell_b)
        # for cell in cells:
        #     cell.draw()
        win.wait_for_close()


# Call the main method
Window.main()
