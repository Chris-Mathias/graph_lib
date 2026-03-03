from graph_lib_ei01.point import Point2d, Point3d
from graph_lib_ei01.matrix import SquareMatrix
from graph_lib_ei01.segment import Segment2d, Segment3d

P2D1 = Point2d(0, 0)
P2D2 = Point2d(3, 4)
P2D3 = Point2d(6, -2)
P2D4 = Point2d(1, 4)

S2D1 = Segment2d(P2D1, P2D2)
S2D2 = Segment2d(P2D3, P2D4)

P3D1 = Point3d(0, 0, 0)
P3D2 = Point3d(1, 2, 2)
P3D3 = Point3d(1, 0, 0)
P3D4 = Point3d(0, 1, 1)

S3D1 = Segment3d(P3D1, P3D2)
S3D2 = Segment3d(P3D3, P3D4)

M1 = SquareMatrix(
    4, data=[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
)
M2 = SquareMatrix(
    4, data=[[16, 15, 14, 13], [12, 11, 10, 9], [8, 7, 6, 5], [4, 3, 2, 1]]
)


def test_point2d():
    print("\nTesting Point2d:\n")
    print("P2D1:", P2D1)
    print("P2D2:", P2D2)
    print()


def test_point3d():
    print("\nTesting Point3d:\n")
    print("P3D1:", P3D1)
    print("P3D2:", P3D2)
    print()


def test_matrix():
    print("\nTesting Square Matrix:\n")
    print("Matrix M1:")
    print(M1)
    print("\nMatrix M2:")
    print(M2)
    result = M1 * M2
    print("\nResult of multiplication:")
    print(result)
    print()


def test_segment2d():
    print("\nTesting Segment2d:\n")
    print(S2D1)
    print(S2D2)
    print("Length of S2D1:", S2D1.length())
    print("Midpoint of S2D1:", S2D1.midpoint())
    print("Length of S2D2:", S2D2.length())
    print("Midpoint of S2D2:", S2D2.midpoint())
    print("Orientation of S2D1 with respect to P2D3:", S2D1.orientation(P2D3))
    print("Orientation of S2D1 with respect to P2D4:", S2D1.orientation(P2D4))
    print("Are S2D1 and S2D2 parallel?", S2D1.is_parallel_to(S2D2))
    print(
        "Classification of intersection between S2D1 and S2D2:\n",
        S2D1.classify_intersection(S2D2),
    )
    print()


def test_segment3d():
    print("\nTesting Segment3d:\n")
    print(S3D1)
    print(S3D2)
    print("Length of S3D1:", S3D1.length())
    print("Midpoint of S3D1:", S3D1.midpoint())
    print("Length of S3D2:", S3D2.length())
    print("Midpoint of S3D2:", S3D2.midpoint())
    print()


if __name__ == "__main__":
    test_point2d()
    test_point3d()
    test_matrix()
    test_segment2d()
    test_segment3d()
