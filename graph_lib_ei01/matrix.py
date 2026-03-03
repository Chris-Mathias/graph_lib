class SquareMatrix:
    def __init__(self, size, data=None):
        self.size = size

        if data:
            if len(data) != size or any(len(row) != size for row in data):
                raise ValueError("Invalid dimensions for the provided data.")
            self.matrix = data
        else:
            self.matrix = [[0 for _ in range(size)] for _ in range(size)]

    def __getitem__(self, index):
        return self.matrix[index]

    def __setitem__(self, index, value):
        self.matrix[index] = value

    def __str__(self):
        return "\n".join(" ".join(map(str, row)) for row in self.matrix)

    def __repr__(self):
        return f"SquareMatrix(size={self.size}, data={self.matrix})"

    def __add__(self, other):
        if self.size != other.size:
            raise ValueError("Matrices must be of the same size.")

        result = SquareMatrix(self.size)

        for i in range(self.size):
            for j in range(self.size):
                result[i][j] = self[i][j] + other[i][j]

        return result

    def __mul__(self, other):
        if self.size != other.size:
            raise ValueError("Matrices must be of the same size.")

        result = SquareMatrix(self.size)

        for i in range(self.size):
            for j in range(self.size):
                result[i][j] = sum(self[i][k] * other[k][j] for k in range(self.size))

        return result
