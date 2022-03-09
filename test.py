import unittest
from book_print_settings import book_print_settings


class TestPrintPages(unittest.TestCase):

    def test_negative_2(self):
        res = book_print_settings(-2, 2)
        self.assertEqual(res, 'Error')
        return

    def test_0_1(self):
        res = book_print_settings(0, 1)
        self.assertEqual(res, [])
        return

    def test_2_negative(self):
        res = book_print_settings(2, -2)
        self.assertEqual(res, 'Error')
        return

    def test_1_0(self):
        res = book_print_settings(1, 0)
        self.assertEqual(res, [])
        return

    def test_1_1(self):
        res = book_print_settings(1, 1)
        self.assertEqual(res, [(0, 1)])
        return

    def test_2_1(self):
        res = book_print_settings(2, 1)
        self.assertEqual(res, [(0, 1), '@', (2, 0)])
        return

    def test_3_1(self):
        res = book_print_settings(3, 1)
        self.assertEqual(res, [(0, 1), '@', (2, 3)])
        return

    def test_4_1(self):
        res = book_print_settings(4, 1)
        self.assertEqual(res, [(4, 1), '@', (2, 3)])
        return

    def test_5_1(self):
        res = book_print_settings(5, 1)
        self.assertEqual(res, [(0, 1), (0, 3), '@', (2, 0), (4, 5)])
        return

    def test_6_1(self):
        res = book_print_settings(6, 1)
        self.assertEqual(res, [(0, 1), (6, 3), '@', (2, 0), (4, 5)])
        return

    def test_7_1(self):
        res = book_print_settings(7, 1)
        self.assertEqual(res, [(0, 1), (6, 3), '@', (2, 7), (4, 5)])
        return

    def test_8_1(self):
        res = book_print_settings(8, 1)
        self.assertEqual(res, [(8, 1), (6, 3), '@', (2, 7), (4, 5)])
        return

    def test_11_1(self):
        res = book_print_settings(11, 1)
        self.assertEqual(res, [(0, 1), (10, 3), (8, 5), '@', (2, 11), (4, 9), (6, 7)])
        return

    def test_12_1(self):
        res = book_print_settings(12, 1)
        self.assertEqual(res, [(12, 1), (10, 3), (8, 5), '@', (2, 11), (4, 9), (6, 7)])
        return

    #
    def test_1_2(self):
        res = book_print_settings(1, 2)
        self.assertEqual(res, "Error")
        return

    def test_2_4(self):
        res = book_print_settings(2, 4)
        self.assertEqual(res, "Error")
        return

    def test_3_2(self):
        res = book_print_settings(3, 2)
        self.assertEqual(res, "Error")
        return

    def test_4_6(self):
        res = book_print_settings(4, 6)
        self.assertEqual(res, "Error")
        return

    def test_5_2(self):
        res = book_print_settings(5, 2)
        self.assertEqual(res, [(4, 1), '@', (2, 3), '#', (0, 5)])
        return

    def test_6_2(self):
        res = book_print_settings(6, 2)
        self.assertEqual(res, [(4, 1), '@', (2, 3), '#', (0, 5), '@', (6, 0)])
        return

    def test_7_2(self):
        res = book_print_settings(7, 2)
        self.assertEqual(res, [(4, 1), '@', (2, 3), '#', (0, 5), '@', (6, 7)])
        return

    def test_8_2(self):
        res = book_print_settings(8, 2)
        self.assertEqual(res, [(4, 1), '@', (2, 3), '#', (8, 5), '@', (6, 7)])
        return

    def test_11_2(self):
        res = book_print_settings(11, 2)
        self.assertEqual(res, [(8, 1), (6, 3), '@', (2, 7), (4, 5), '#', (0, 9), '@', (10, 11)])
        return

    def test_11_3(self):
        res = book_print_settings(11, 3)
        self.assertEqual(res, [(4, 1), '@', (2, 3), '#',
                               (8, 5), '@', (6, 7), '#',
                               (0, 9), '@', (10, 11)])
        return

    def test_17_4(self):
        res = book_print_settings(17, 4)
        self.assertEqual(res, [(8, 1), (6, 3), '@', (2, 7), (4, 5), '#',
                               (12, 9), '@', (10, 11), '#',
                               (16, 13), '@', (14, 15), '#',
                               (0, 17)])
        return

    def test_17_6(self):
        res = book_print_settings(17, 6)
        self.assertEqual(res, "Error")
        return


if __name__ == '__main__':
    unittest.main()
