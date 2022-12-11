import unittest
from math import pi

from math_components import Vector


class VectorTest(unittest.TestCase):
    def test_init(self):
        vector = Vector(3, 4)
        self.assertEqual(vector.x, 3, 'x coord not save')
        self.assertEqual(vector.y, 4, 'y coord not save')

    def test_len(self):
        test_data = [
            ((3, 4), 5.0),
            ((4, 3), 5.0),
            ((0, 0), 0),
            ((-4, -3), 5.0)
        ]
        for coord, ans in test_data:
            vector = Vector(*coord)
            self.assertEqual(vector.length(), ans, f"Length don't work for {self}")

    def test_equal_and_not_equal(self):
        test_data = [
            (((3, 4), (4, 3)), False),
            (((3, 4), (3, 4)), True),
            (((-3, -4), (3, 4)), False),
            (((0, 0), (0, 0)), True)
        ]
        for coords, ans in test_data:
            v1, v2 = [Vector(*coord) for coord in coords]
            if ans:
                self.assertEqual(v1, v2)
            else:
                self.assertNotEqual(v1, v2)

    def test_addition(self):
        test_data = [
            (((3, 0), (0, 4)), (3, 4)),
            (((3, 0), (4, 0)), (7, 0)),
            (((-3, 0), (3, 0)), (0, 0)),
            (((-3, 4), (-4, 3)), (-7, 7)),
            (((0, 0), (1, 1)), (1, 1)),
            (((3, 4), (5, 6)), (8, 10)),
        ]
        for coords, ans in test_data:
            v1, v2 = [Vector(*coord) for coord in coords]
            v_ans = Vector(*ans)
            self.assertEqual(v1 + v2, v_ans)
            self.assertEqual(v2 + v1, v_ans)
            v1 += v2
            self.assertEqual(v1, v_ans)

    def test_subtraction(self):
        test_data = [
            (((3, 4), (0, 4)), (3, 0)),
            (((3, 0), (4, 0)), (-1, 0)),
            (((-3, 0), (3, 0)), (-6, 0)),
            (((-3, 4), (-4, 3)), (1, 1)),
            (((0, 0), (1, 1)), (-1, -1)),
            (((3, 4), (5, 6)), (-2, -2)),
        ]
        for coords, ans in test_data:
            v1, v2 = [Vector(*coord) for coord in coords]
            v_ans = Vector(*ans)
            self.assertEqual(v1 - v2, v_ans)
            self.assertEqual(v2 - v1, -v_ans)
            v1 -= v2
            self.assertEqual(v1, v_ans)

    def test_multiplication(self):
        test_data = [
            (((1, 1), 10), (10, 10)),
            (((3, 4), 0.5), (1.5, 2)),
            (((6, 6), 0), (0, 0)),
            (((11, -11), -1), (-11, 11)),
        ]
        for data, ans in test_data:
            v1, m = Vector(*data[0]), data[1]
            v_ans = Vector(*ans)
            self.assertEqual(v1 * m, v_ans)
            self.assertEqual(m * v1, v_ans)
            v1 *= m
            self.assertEqual(v1, v_ans)

    def test_dividing(self):
        test_data = [
            (((10, 10), 10), (1, 1)),
            (((3, 4), 2), (1.5, 2)),
            (((6, 6), 1), (6, 6)),
            (((11, -11), -1), (-11, 11)),
        ]
        for data, ans in test_data:
            v1, m = Vector(*data[0]), data[1]
            v_ans = Vector(*ans)
            self.assertEqual(v1 / m, v_ans)
            v1 /= m
            self.assertEqual(v1, v_ans)

    def test_negative(self):
        test_data = [
            ((3, 0), (-3, 0)),
            ((3, 4), (-3, -4)),
            ((0, 0), (0, 0)),
            ((-3, 4), (3, -4)),
            ((-1, -1), (1, 1)),
            ((1, -4), (-1, 4)),
        ]
        for coord, ans in test_data:
            v, neg_v = Vector(*coord), Vector(*ans)
            self.assertEqual(-v, neg_v)

    def test_normalize(self):
        test_data = [
            (3, 4),
            (1, 1),
            (0, 1),
            (1, 0),
            (-1, 0),
            (10, 10),
        ]
        delta = 0.0001
        for coord in test_data:
            vec = Vector(*coord)
            vec_n = vec.normalize()
            self.assertLess(abs(vec.angle(vec_n)), delta)
            self.assertLess(abs(vec_n.length() - 1), delta)

    def test_dot_product(self):
        test_data = [
            (((1, 0), (0, -1)), 0),
            (((2, -5), (-1, 0)), -2),
            (((1, 1), (-1, 1)), 0),
            (((10, 20), (20, 10)), 400),
        ]
        delta = 0.0001
        for coords, ans in test_data:
            v1, v2 = [Vector(*coord) for coord in coords]
            self.assertLess(abs(v1.dot_product(v2) - ans), delta)
            self.assertLess(abs(v2.dot_product(v1) - ans), delta)
            self.assertLess(abs(v1.dot_product(v1) - v1.length() ** 2), delta)

    def test_to_tuple(self):
        test_data = [
            (3, 4),
            (1, 1),
            (0, 1),
            (1, 0),
            (-1, 0),
            (10, 10),
        ]
        for coord in test_data:
            v = Vector(*coord)
            self.assertEqual(v.to_tuple(), coord)

    def test_rotate(self):
        test_data = [
            (((1, 0), pi / 2), (0, 1)),
            (((0, 1), -pi / 2), (1, 0)),
            (((1, -1), pi / 2), (1, 1)),
            (((-1, 1), pi / 2), (-1, -1)),
        ]
        delta = 0.00001
        for data, ans in test_data:
            v, a = Vector(*data[0]), data[1]
            v_ans = Vector(*ans)
            v = v.rotate(a)
            temp = v_ans - v
            x, y = temp.x, temp.y
            self.assertLess(x, delta)
            self.assertLess(y, delta)

    def test_angle(self):
        test_data = [
            (((1, 0), (0, 1)), pi / 2),
            (((0, 1), (1, 0)), pi / 2),
            (((1, -1), (1, 1)), pi / 2),
            (((-1, 1), (-1, -1)), pi / 2),
            (((1, 1), (-1, -1)), pi)
        ]
        delta = 0.0001
        for coords, ans in test_data:
            v1, v2 = [Vector(*coord) for coord in coords]
            self.assertLess(abs(v1.angle(v2) - ans), delta)


if __name__ == '__main__':
    unittest.main()
