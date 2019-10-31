import unittest
from cycle_finder import CycleFinder

class test_get_neighbors(unittest.TestCase):

    # empty input (0,0)
    def test1(self):
        cf = CycleFinder('testfiles/test3')
        # 0, 0 is undefined if our matrix is empty
        self.assertRaises(IndexError, cf.get_neighbors, (0, 0))

    # small input, top left
    def test2(self):
        cf = CycleFinder('testfiles/test2')
        neighbors = cf.get_neighbors((0, 0))
        self.assertEqual(len(neighbors), 1)
        self.assertIn((0, 1), neighbors)

    # larger input, top right
    def test3(self):
        cf = CycleFinder('testfiles/test4')
        neighbors = cf.get_neighbors((0, 2))
        self.assertEqual(len(neighbors), 2)
        self.assertIn((0, 1), neighbors)
        self.assertIn((1, 2), neighbors)

    # larger input, out of bounds
    def test4(self):
        cf = CycleFinder('testfiles/test5')
        self.assertRaises(IndexError, cf.get_neighbors, (3,1))

    # larger input, bottom edge
    def test5(self):
        cf = CycleFinder('testfiles/test6')
        neighbors = cf.get_neighbors((3, 4))
        self.assertEqual(len(neighbors), 2)
        self.assertIn((3, 5), neighbors)
        self.assertIn((3, 3), neighbors)

    # larger input, somewhere in the middle
    def test6(self):
        cf = CycleFinder('testfiles/test7')
        neighbors = cf.get_neighbors((2, 1))
        self.assertEqual(len(neighbors), 2)
        self.assertIn((1, 1), neighbors)
        self.assertIn((3, 1), neighbors)

    # larger input, somewhere in the middle without neighbors
    def test7(self):
        cf = CycleFinder('testfiles/test7')
        neighbors = cf.get_neighbors((2, 4))
        self.assertEqual(len(neighbors), 0)


class test_find_cycle(unittest.TestCase):

    # minimal cycle
    def test1(self):
        cf = CycleFinder('testfiles/test1')
        self.assertTrue(cf.find_cycle())

    # input too small to form a cycle
    def test2(self):
        cf = CycleFinder('testfiles/test2')
        self.assertFalse(cf.find_cycle())

    # empty input
    def test3(self):
        cf = CycleFinder('testfiles/test3')
        self.assertFalse(cf.find_cycle())

    # cycle length 8
    def test4(self):
        cf = CycleFinder('testfiles/test4')
        self.assertTrue(cf.find_cycle())

    # no cycle
    def test5(self):
        cf = CycleFinder('testfiles/test5')
        self.assertFalse(cf.find_cycle())

    # large cycle that's not just rectangular
    def test6(self):
        cf = CycleFinder('testfiles/test6')
        self.assertTrue(cf.find_cycle())

    # large input, no cycle
    def test7(self):
        cf = CycleFinder('testfiles/test7')
        self.assertFalse(cf.find_cycle())

if __name__ == '__main__':
    unittest.main()
