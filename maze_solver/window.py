from tkinter import Tk, Canvas
import random


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
                 has_top_wall=True, has_bottom_wall=True):
        self.has_left_wall = has_left_wall
        self.has_right_wall = has_right_wall
        self.has_top_wall = has_top_wall
        self.has_bottom_wall = has_bottom_wall
        self.__x1 = x1
        self.__x2 = x2
        self.__y1 = y1
        self.__y2 = y2
        self.__win = win

    def draw(self):
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

    def draw_move(self, to_cell, undo=False):
        if not undo:
            line =
class Window:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.__root_widget = Tk()
        self.__canvas = Canvas(self.__root_widget, width=self.width, height=self.height)
        self.__canvas.pack()  # Packs the canvas into the window
        self.__root_widget.title(f"w:{self.width}, h:{self.height}")
        self._running = True  # Initialize as True to enter the loop

        # Bind the close event properly
        self.__root_widget.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root_widget.update_idletasks()
        self.__root_widget.update()

    def wait_for_close(self):
        # No need to reset self._running here
        while self._running:
            self.redraw()

    def close(self):
        self._running = False
        self.__root_widget.destroy()  # Properly close the window

    def draw_line(self, ln: Line, fill_color):
        ln.draw(self.__canvas, fill_color)
        self.redraw()  # Force the window to refresh right after drawing the line

    def generate_random_cells(self, num_cells):
        cells = []
        for i in range(num_cells):
            x1 = random.randint(0, self.width - 100)
            x2 = x1 + random.randint(50, 150)  # cell width between 50 and 150
            y1 = random.randint(0, self.height - 100)
            y2 = y1 + random.randint(50, 150)  # cell height between 50 and 150
            cell = Cell(x1, x2, y1, y2, self)
            cells.append(cell)
        return cells

    @staticmethod  # Define main as a static method
    def main():
        win = Window(1280, 720)
        cells = win.generate_random_cells(8)

        for cell in cells:
            cell.draw()
        win.wait_for_close()


# Call the main method
Window.main()
