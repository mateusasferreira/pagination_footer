import unittest
from footer import create_pagination_footer


class TestPaginationFooter(unittest.TestCase):

    def test_create_footer(self):
        test_cases = [
            ((4,5,1,0), '1 ... 4 5'),
            ((4,10,2,2), '1 2 3 4 5 6 ... 9 10'),
            ((1,1,0,0), '1'),
            ((1,1,2,2), '1'),
            ((6,12,2,2), '1 2 ... 4 5 6 7 8 ... 11 12'),
            ((8,10,2,2), '1 2 ... 6 7 8 9 10'),
            ((1,10,0,0), '1 ... 10'),
            ((10,10,0,2), '1 ... 8 9 10'),
        ]
        
        for args, result in test_cases:
            self.assertEqual(create_pagination_footer(*args), result)

    def test_create_footer_current_page_gt_total(self):
        with self.assertRaises(ValueError):
            create_pagination_footer(2, 1, 1, 1)


if __name__ == '__main__':
    unittest.main()