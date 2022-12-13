from math import hypot, cos, sin, acos
from typing_extensions import Self


class Vector:
    def __init__(self, x: float = 0.0, y: float = 0.0):
        self.x, self.y = x, y

    def length(self) -> float:
        return hypot(self.x, self.y)

    def __eq__(self, other: Self) -> bool:
        return self.x == other.x and self.y == other.y

    def __ne__(self, other: Self) -> bool:
        return not self == other

    def __add__(self, other: Self) -> Self:
        return Vector(self.x + other.x, self.y + other.y)

    def __radd__(self, other: Self) -> Self:
        return self + other

    def __iadd__(self, other: Self) -> Self:
        self.x += other.x
        self.y += other.y
        return self

    def __sub__(self, other: Self) -> Self:
        return Vector(self.x - other.x, self.y - other.y)

    def __rsub__(self, other: Self) -> Self:
        return self - other

    def __isub__(self, other: Self) -> Self:
        self.x -= other.x
        self.y -= other.y
        return self

    def __mul__(self, other: float) -> Self:
        return Vector(self.x * other, self.y * other)

    def __rmul__(self, other: float) -> Self:
        return self * other

    def __imul__(self, other: float) -> Self:
        self.x *= other
        self.y *= other
        return self

    def __truediv__(self, other: float) -> Self:
        return Vector(self.x / other, self.y / other)

    def __itruediv__(self, other: float) -> Self:
        self.x /= other
        self.y /= other
        return self

    def __neg__(self) -> Self:
        return Vector(-self.x, -self.y)

    def __pos__(self) -> Self:
        return self

    def normalize(self) -> Self:
        return self / self.length()

    def dot_product(self, other: Self) -> float:
        return self.x * other.x + self.y * other.y

    def to_tuple(self) -> tuple[float, float]:
        return self.x, self.y

    def rotate(self, angle: float) -> Self:
        return Vector(self.x * cos(angle) - self.y * sin(angle),
                      self.x * sin(angle) + self.y * cos(angle))

    def angle(self, other: Self) -> float:
        # noinspection PyTypeChecker
        dot = self.dot_product(other)
        l1, l2 = self.length(), other.length()
        return acos(dot / (l1 * l2))

    def __str__(self) -> str:
        return str(self.to_tuple())

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"
