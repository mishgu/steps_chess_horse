from unittest.case import TestCase
from steps_horse import steps_horse

class TestCalc(TestCase):
    def test_calc(self):
        test_data_simple = [
            (20, 0, 10),
            (20, 1, 11),
            (20, 8, 10),
            (20, 9, 11),
            (0, 19, 11),
            (19, 1, 10),
            (19, 9, 10),
            (8, 19, 11),
            (0, 17, 9),
            (1, 17, 10),
            (1, 18, 9),
            #(1123, 342, 561),
            (34, 865, 433),
            (2, 14764, 7382),
            (1, 3, 2),
            (6, 1234, 618),
            (-24523, 2643, 12262),
            (-745, -10000, 5001),
            (6, 7, 5),
            (2, 2, 4),
            (2, 1, 1),
        ]

        for input_x, input_y, expected_result in test_data_simple:
            self.assertEquals(steps_horse(input_x,input_y), expected_result)
