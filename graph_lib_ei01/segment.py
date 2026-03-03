import math
from graph_lib_ei01.point import Point2d, Point3d


class Segment2d:
    def __init__(self, start: Point2d, end: Point2d):
        self.start = start
        self.end = end

        if math.isclose(self.start.distance_to(self.end), 0, abs_tol=1e-9):
            raise ValueError("A segment cannot have zero length.")

    def __str__(self):
        return f"Segment2d(start={self.start}, end={self.end})"

    def __repr__(self):
        return f"Segment2d(start={self.start}, end={self.end})"

    def length(self) -> float:
        return self.start.distance_to(self.end)

    def midpoint(self) -> Point2d:
        mid_x = (self.start.x + self.end.x) / 2
        mid_y = (self.start.y + self.end.y) / 2
        return Point2d(mid_x, mid_y)

    def orientation(self, p: Point2d) -> float:
        return (self.end.x - self.start.x) * (p.y - self.start.y) - (
            self.end.y - self.start.y
        ) * (p.x - self.start.x)

    def is_parallel_to(self, other: "Segment2d", tol: float = 1e-9) -> bool:
        dx1 = self.end.x - self.start.x
        dy1 = self.end.y - self.start.y
        dx2 = other.end.x - other.start.x
        dy2 = other.end.y - other.start.y
        return math.isclose(dx1 * dy2, dy1 * dx2, abs_tol=tol)

    def intersection_with(self, other: "Segment2d") -> Point2d:
        A1 = self.end.y - self.start.y
        B1 = self.start.x - self.end.x
        C1 = A1 * self.start.x + B1 * self.start.y

        A2 = other.end.y - other.start.y
        B2 = other.start.x - other.end.x
        C2 = A2 * other.start.x + B2 * other.start.y

        det = A1 * B2 - A2 * B1
        if det == 0:
            return None

        x = (B2 * C1 - B1 * C2) / det
        y = (A1 * C2 - A2 * C1) / det
        return Point2d(x, y)

    def contains_point(self, p: Point2d, tol: float = 1e-9) -> bool:
        within_x = (
            min(self.start.x, self.end.x) - tol
            <= p.x
            <= max(self.start.x, self.end.x) + tol
        )
        within_y = (
            min(self.start.y, self.end.y) - tol
            <= p.y
            <= max(self.start.y, self.end.y) + tol
        )
        return within_x and within_y

    def classify_intersection(self, other: "Segment2d") -> str:
        if self.is_parallel_to(other):
            if math.isclose(self.orientation(other.start), 0, abs_tol=1e-9):
                return "Collinear"
            else:
                return "Parallel"

        intersection_point = self.intersection_with(other)
        if intersection_point:
            if self.contains_point(intersection_point) and other.contains_point(
                intersection_point
            ):
                return f"Intersecting at {intersection_point}"
            return f"Intersecting outside segments at {intersection_point}"

        return "Not intersecting"


class Segment3d:
    def __init__(self, start: Point3d, end: Point3d):
        self.start = start
        self.end = end

        if self.start == self.end:
            raise ValueError("A segment cannot have zero length.")

    def __str__(self):
        return f"Segment3d(start={self.start}, end={self.end})"

    def __repr__(self):
        return f"Segment3d(start={self.start}, end={self.end})"

    def length(self) -> float:
        return self.start.distance_to(self.end)

    def midpoint(self):
        mid_x = (self.start.x + self.end.x) / 2
        mid_y = (self.start.y + self.end.y) / 2
        mid_z = (self.start.z + self.end.z) / 2
        return Point3d(mid_x, mid_y, mid_z)
