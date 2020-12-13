"""Tests for the image_io.py."""

from video_transformation_numpy import image_io
import numpy as np
import os
import shutil
from unittest import main
from unittest import TestCase


TEMP_DIR = './tmp'

class TestImageIo(TestCase):

    def setUp(self):
        try:
            os.mkdir(TEMP_DIR)
        except:
            pass

    def tearDown(self):
        shutil.rmtree(TEMP_DIR)

    def testNonExistent(self):
        '''Given a path that doesn't contain a image, read_image should raise ValueError.'''

        input_path = os.path.join(TEMP_DIR, 'nonexistent.jpg')
        with self.assertRaises(ValueError):
            _ = image_io.read_image(input_path)

    def testAllZeroReadThenWrite(self):
        '''Write a NumPy array of all zeros to file, then read it.'''

        path = os.path.join(TEMP_DIR, 'all_zero.jpg')

        # Write image bytes to file.
        height_in, width_in = 360, 640
        image_np_in = np.zeros((height_in, width_in, 3), dtype='uint8')

        image_io.write_image(path, image_np_in)

        # Read image bytes.
        image_np_out = image_io.read_image(path)

        height_out, width_out, num_channels_out = image_np_out.shape

        self.assertEqual(height_in, height_out)
        self.assertEqual(width_in, width_out)
        self.assertEqual(num_channels_out, 3)
        self.assertTrue((image_np_in == image_np_out).all())

        os.remove(path)


if __name__ == '__main__':
    main()