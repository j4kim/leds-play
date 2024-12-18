class Pixels:
    cells = (
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
    )
    default_color = 0xffffff

    def fill(self):
        for y in range(7):
            for x in range(6):
                self.cells[y][x] = 0xffffff

    def clear(self):
        for y in range(7):
            for x in range(6):
                self.cells[y][x] = 0

    def set(self, x, y, color):
        self.cells[y][x] = color

    def show(self):
        for y in range(7):
            for x in range(6):
                print("#" if self.cells[y][x] else " ", end="|")
            print()