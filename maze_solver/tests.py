import unittest
from main import Maze, Window


class Tests(unittest.TestCase):
    # def test_maze_create_cells(self):
    #     window = Window(1280, 720)
    #     num_cols = 4
    #     num_rows = 4
    #     m1 = Maze(0, 0, num_rows, num_cols, 10, 10, window)
    #
    #     self.assertEqual(
    #         len(m1._cells),
    #         num_cols,
    #     )
    #     self.assertEqual(
    #         len(m1._cells[0]),
    #         num_rows,
    #     )

    def test_break_entrance_and_exit(self):
        window = Window(1280, 720)
        num_cols = 5
        num_rows = 5
        m2 = Maze(40, 40, num_rows, num_cols, 20, 20, window)
        m2._break_entrance_and_exit()

        self.assertEqual(
            m2._cells[0][0].has_top_wall,
            False
        )
        self.assertEqual(
            m2._cells[-1][-1].has_bottom_wall,
            False
        )

        # Redraw and process events
        window.redraw()
        for _ in range(10):  # Process events multiple times
            window._root_widget.update_idletasks()
            window._root_widget.update()

        # Close the window after processing
        window._root_widget.destroy()

    def test_break_walls_r(self):
        # initialize maze
        # select random i, j and call the break_walls_r
        # self.assertEqual with what?
        pass



if __name__ == "__main__":
    unittest.main()