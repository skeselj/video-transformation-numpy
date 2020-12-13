"""Tests for image_compression_test.py."""


import numpy as np
from unittest import main
from unittest import TestCase
from video_transformation_numpy import image_compression


class TestImageCompresion(TestCase):

    def testGroupRowsByAvgOnSmallNonTrivialImage(self):
        '''Run the function group_rows_by_avg on a small image.'''

        image_np = np.array(
            [
                [
                    [1, 2, 3],
                    [2, 3, 0],
                ],
                [
                    [1, 1, 2],
                    [2, 2, 1],
                ],
            ], 
            dtype=np.uint8)
        
        actual_output_np = image_compression.group_rows_by_avg(image_np)

        expected_output_np = np.array(
            [
                [1, 2, 1],
                [1, 1, 1],
            ],
            dtype=np.uint8)
        
        self.assertTrue((actual_output_np == expected_output_np).all())


if __name__ == '__main__':
    main()