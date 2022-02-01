class Cell:
    def __init__(self, number_of_cells):
        self.number_of_cells = number_of_cells

    def make_order(self, number):
        return (('*' * number + '\n') * (self.number_of_cells // number)) + ('*' * (self.number_of_cells % number))

    def __add__(self, other):
        return Cell(self.number_of_cells + other.number_of_cells)

    def __sub__(self, other):
        if self.number_of_cells - other.number_of_cells <= 0:
            print('количество ячеек второй клетки меньше чем первой')
        else:
            return Cell(self.number_of_cells - other.number_of_cells)

    def __mul__(self, other):
        return Cell(self.number_of_cells * other.number_of_cells)

    def __floordiv__(self, other):
        return Cell(self.number_of_cells // other.number_of_cells)

    def __truediv__(self, other):
        return Cell(self.number_of_cells // other.number_of_cells)


cell_1 = Cell(12)
cell_2 = Cell(10)
cell_3 = cell_1 + cell_2
cell_4 = cell_1 - cell_2
cell_5 = cell_3 * cell_4
cel_6 = cell_1 / cell_2
print(cell_3.number_of_cells)
print(cell_4.number_of_cells)
print(cell_5.number_of_cells)
print(cel_6.number_of_cells)
print(cell_1.make_order(3))
