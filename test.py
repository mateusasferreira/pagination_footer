import unittest
from footer import create_pagination_footer


class TestPaginationFooter(unittest.TestCase):

    def test_single_page(self):
        args = (1, 1, 0, 0)
        expected_result = '1'
        self.assertEqual(create_pagination_footer(*args), expected_result)

    def test_single_page_with_ignored_boundaries(self):
        args = (1, 1, 2, 2)
        expected_result = '1'
        self.assertEqual(create_pagination_footer(*args), expected_result)

    def test_ellipses_before_current_page(self):
        args = (4, 5, 1, 0)
        expected_result = '1 ... 4 5'
        self.assertEqual(create_pagination_footer(*args), expected_result)

    def test_one_ellipses_after_around_and_before_total_boundary(self):
        args = (4, 10, 2, 2)
        expected_result = '1 2 3 4 5 6 ... 9 10'
        self.assertEqual(create_pagination_footer(*args), expected_result)

    def test_ellipses_before_and_after_arounds(self):
        args = (6, 12, 2, 2)
        expected_result = '1 2 ... 4 5 6 7 8 ... 11 12'
        self.assertEqual(create_pagination_footer(*args), expected_result)

    def test_one_ellipses_before_around_and_after_boundary(self):
        args = (8, 10, 2, 2)
        expected_result = '1 2 ... 6 7 8 9 10'
        self.assertEqual(create_pagination_footer(*args), expected_result)

    def test_last_page_with_around_no_boundary(self):
        args = (10, 10, 0, 2)
        expected_result = '... 8 9 10'
        self.assertEqual(create_pagination_footer(*args), expected_result)

    def test_last_but_one_with_around_no_boundary(self):
        args = (9, 10, 0, 1)
        expected_result = '... 8 9 10'
        self.assertEqual(create_pagination_footer(*args), expected_result)
    
    def test_boundaries_sum_gt_total_pages(self):
        args = (1, 10, 6, 1)
        expected_result = '1 2 3 4 5 6 7 8 9 10'
        self.assertEqual(create_pagination_footer(*args), expected_result)
    
    def test_boundaries_sum_gt_total_page_with_current_at_middle(self):
        args = (5, 10, 6, 1)
        expected_result = '1 2 3 4 5 6 7 8 9 10'
        self.assertEqual(create_pagination_footer(*args), expected_result)
    
    def test_around_sum_gt_total_pages(self):
        args = (3, 5, 0, 4)
        expected_result = '1 2 3 4 5'
        self.assertEqual(create_pagination_footer(*args), expected_result)

    def test_ellipses_after_around_no_boundaries(self):
        args = (2, 4, 0, 1)
        expected_result = '1 2 3 ...'
        self.assertEqual(create_pagination_footer(*args), expected_result)

    def test_create_footer_current_page_gt_total(self):
        with self.assertRaises(ValueError):
            create_pagination_footer(2, 1, 1, 1)

if __name__ == '__main__':
    unittest.main()