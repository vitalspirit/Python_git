# ЗАДАНИЕ №1   #############################################
class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix
    def __str__(self):
        return '\n'.join([''.join(['%d\t' % i for i in row]) for row in self.matrix])
    def __add__(self, other):
        summable = False
        result = self.matrix
        if len(self.matrix) == len(other.matrix):
            for k in range(len(self.matrix)):
                if len(self.matrix[k]) == len(other.matrix[k]):
                    summable = True
                else:
                    return "Извените, но матрицы имеют разную размерность"
        else:
            return "Извените, но матрицы имеют разную размерность"
        if summable == True:
            for i in range(len(self.matrix)):
                for j in range(len(self.matrix[0])):
                    result[i][j] = self.matrix[i][j] + other.matrix[i][j]
            return '\n'.join([''.join(['%d\t' % i for i in row]) for row in result])

matrix_1 = Matrix([[2, 1, 1], [5, 6, 6], [1, 2, 45]])
matrix_2 = Matrix([[3, 5, 6], [6, 4, 6], [15, 6, 6]])

print(f"Первая матрица: \n{matrix_1}")
print(f"Вторая матрица: \n{matrix_2}")
print(f"Сумма двух матриц: \n{matrix_1+matrix_2}")



# ЗАДАНИЕ №2   #############################################
class Cloth:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def get_square_c(self):
        return self.width / 6.5 + 0.5
    def get_square_j(self):
        return self.height * 2 + 0.3
    @property
    def get_sq_full(self):
        return str(f'Общая площадь ткани:'
                   f' {(self.width / 6.5 + 0.5) + (self.height * 2 + 0.3)}')

class Coat(Cloth):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.square_c = round(self.width / 6.5 + 0.5)
    def __str__(self):
        return f'Площадь на пальто: {self.square_c}м2'

class Jacket(Cloth):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.square_j = round(self.height * 2 + 0.3)
    def __str__(self):
        return f'Площадь на костюм: {self.square_j}м2'

coat = Coat(2, 4)
jacket = Jacket(1, 2)
print(coat)
print(jacket)
print(coat.get_sq_full)
print(jacket.get_sq_full)


# ЗАДАНИЕ №3   #############################################
class Cell:
    def __init__(self, q):
        self.q = int(q)
    def __str__(self):
        return f'Количество ячеек в клетке: {self.q} шт.'

    def __add__(self, other):
        return f'Количество ячеек в объединенной клетке: {self.q + other.q}шт.'

    def __sub__(self, other):
        if int(self.q) - int(other.q) > 0:
            return f'Количество ячеек в результате вычитания: {int(self.q - other.q)}шт.'
        else:
            return f'Операция вычитания невозможна'""
    def __mul__(self, other):
        return f'Количество ячеек в результате умножения: {int(self.q * other.q)}шт.'
    def __floordiv__(self, other):
        return f'Количество ячеек в результате деления: {int(self.q // other.q)}шт.'

    def make_order(self, row):
        r = ''
        for i in range(int(self.q / row)):
            r += f'{"*" * row} \n'
        r += f'{"*" * (self.q % row)}'
        return r

cells1 = Cell(33)
cells2 = Cell(13)
print(cells1)
print(cells1 + cells2)
print(cells1 - cells2)
print(cells1 * cells2)
print(cells1 // cells2)
print(cells2.make_order(5))



