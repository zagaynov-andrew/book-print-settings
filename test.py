import unittest
import lab


class TestPrintPages(unittest.TestCase):

    def test_negative(self):
        res = lab.book_print_settings(-2)
        self.assertEqual(res, 'Error')
        return

    def test_0(self):
        res = lab.book_print_settings(0)
        self.assertEqual(res, [])
        return

    def test_1(self):
        res = lab.book_print_settings(1)
        self.assertEqual(res, [(0, 1)])
        return

    def test_2(self):
        res = lab.book_print_settings(2)
        self.assertEqual(res, [(0, 1), '@', (2, 0)])
        return

    def test_3(self):
        res = lab.book_print_settings(3)
        self.assertEqual(res, [(0, 1), '@', (2, 3)])
        return

    def test_4(self):
        res = lab.book_print_settings(4)
        self.assertEqual(res, [(4, 1), '@', (2, 3)])
        return

    def test_5(self):
        res = lab.book_print_settings(5)
        self.assertEqual(res, [(0, 1), (0, 3), '@', (2, 0), (4, 5)])
        return

    def test_6(self):
        res = lab.book_print_settings(6)
        self.assertEqual(res, [(0, 1), (6, 3), '@', (2, 0), (4, 5)])
        return

    def test_7(self):
        res = lab.book_print_settings(7)
        self.assertEqual(res, [(0, 1), (6, 3), '@', (2, 7), (4, 5)])
        return

    def test_8(self):
        res = lab.book_print_settings(8)
        self.assertEqual(res, [(8, 1), (6, 3), '@', (2, 7), (4, 5)])
        return

    def test_11(self):
        res = lab.book_print_settings(11)
        self.assertEqual(res, [(0, 1), (10, 3), (8, 5), '@', (2, 11), (4, 9), (6, 7)])
        return

    def test_12(self):
        res = lab.book_print_settings(12)
        self.assertEqual(res, [(12, 1), (10, 3), (8, 5), '@', (2, 11), (4, 9), (6, 7)])
        return


if __name__ == '__main__':
    unittest.main()


