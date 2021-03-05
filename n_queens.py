
from numpy import zeros, fliplr


class board:
    def __init__(self, n):
        self.b = zeros((n, n), dtype=int)
        self.f_pos = []
        self.lm = n
        self.ij = (0, 0)

    def put_queen(self, pos):
        self.f_pos.append(pos)
        self.b[pos] = 1

    def remove_queen(self, pos):
        self.f_pos.remove(pos)
        self.b[pos] = 0

    def solve(self, i=0, jd=0):
        if self.is_solved():
            return True
        if jd < self.lm:
            for j in range(self.lm):
                if self.check_valid((i, j)) and j >= jd:
                    self.put_queen((i, j))
                    if self.solve(i=i+1):
                        return True
            if 1 not in self.b[i]:
                i, j = self.f_pos[-1]
                self.remove_queen((i, j))
                if self.solve(i, j+1):
                    return True
        else:
            i, j = self.f_pos[-1]
            self.remove_queen((i, j))
            if self.solve(i, j+1):
                return True

    def check_valid(self, pos):
        if self.check_row(pos[0]):
            if self.check_col(pos[1]):
                if self.check_dig(*pos):
                    return True
        return False

    def check_row(self, x):
        row = self.b[x]
        if 1 not in row:
            return True
        return False

    def check_col(self, y):
        col = self.b[:, y]
        if 1 not in col:
            return True
        return False

    def check_dig(self, i, j):
        d1 = j-i
        d2 = self.lm - (i + j) - 1
        dig1 = self.b.diagonal(d1)
        dig2 = fliplr(self.b).diagonal(d2)
        if 1 not in dig1:
            if 1 not in dig2:
                return True
        return False

    def is_solved(self):
        if len(self.f_pos) != self.lm:
            return False
        return True

    def show(self):
        for l in self.b:
            print(l)


for j in range(4, 14):
    gg = board(j)
    gg.solve()
    print("\n", j, ":\n")
    gg.show()
