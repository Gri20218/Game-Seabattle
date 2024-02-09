class SeaMap:
    def __init__(self):
        self.map = [['.' for __ in range(10)] for _ in range(10)]
        self.cords = []
        self.count = 0
        self.snk = tuple()

    def cell(self, rw, cl):
        return self.map[rw][cl]

    def sink(self, y, x):
        new_x, new_y = None, None
        for i in range(min(9, y + 1), max(0, y - 1) - 1, -1):
            for j in range(min(9, x + 1), max(0, x - 1) - 1, -1):
                if self.map[i][j] != 'x':
                    self.map[i][j] = '*'
                elif i == y and j == x:
                    continue
                elif self.map[i][j] == 'x' and (i, j) not in self.cords:
                    if new_x is None:
                        new_x, new_y = j, i
        if new_x is None:
            new_y, new_x = self.snk
            self.count += 1
        if self.count != 2:
            if (new_y, new_x) not in self.cords:
                self.cords.append((new_y, new_x))
            return self.sink(new_y, new_x)
        else:
            return

    def shoot(self, rw, cl, result):
        if result == 'miss':
            self.map[rw][cl] = '*'
        elif result == 'hit':
            self.map[rw][cl] = 'x'
        else:
            self.map[rw][cl] = 'x'
            self.snk = (rw, cl)
            self.cords.append((rw, cl))
            self.count = 0
            self.sink(rw, cl)