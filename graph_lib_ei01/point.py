class Point2d:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __repr__(self):
        return f"Point2d(x={self.x}, y={self.y})"

    def length(self) -> float:
        return (self.x**2 + self.y**2) ** 0.5

    def distance_to(self, other: "Point2d") -> float:
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5


class Point3d:
    def __init__(self, x: float, y: float, z: float):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"

    def __repr__(self):
        return f"Point3d(x={self.x}, y={self.y}, z={self.z})"

    def length(self) -> float:
        return (self.x**2 + self.y**2 + self.z**2) ** 0.5

    def distance_to(self, other: "Point3d") -> float:
        return (
            (self.x - other.x) ** 2 + (self.y - other.y) ** 2 + (self.z - other.z) ** 2
        ) ** 0.5
