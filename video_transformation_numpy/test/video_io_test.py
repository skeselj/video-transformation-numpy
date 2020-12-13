"""Tests for the video_io.py."""

import numpy as np
import os
from unittest import main
from unittest import TestCase
from video_io import read_video
from video_io import write_video


TEMP_DIR = './tmp'

class TestVideoIo(TestCase):

    def setUp(self):
        os.mkdir(TEMP_DIR)

    def tearDown(self):
        os.rmdir(TEMP_DIR)

    def testNonExistent(self):
        '''Given a path that doesn't contain a video, read_video outputs should be Nones.'''

        input_path = os.path.join(TEMP_DIR, 'nonexistent.mp4')
        video_np, codec, fps = read_video(input_path)

        self.assertIsNone(video_np)
        self.assertIsNone(codec)
        self.assertIsNone(fps)

    def testAllZeroReadThenWrite(self):
        '''Write a NumPy array of all zeros to file, then read it.'''

        path = os.path.join(TEMP_DIR, 'all_zero.mp4')

        # Write video bytes to file.
        num_frames_in, frame_height_in, frame_width_in, num_channels_in = 1800, 360, 640, 3
        fps_in, codec_in = 60, 'mp4v'
        video_np_in = np.zeros((num_frames_in, frame_height_in, frame_width_in, num_channels_in),
                               dtype='uint8')

        self.assertTrue(write_video(path, video_np_in, codec_in, fps_in))

        # Read video bytes, and associate metadata from the same file.
        video_np_out, codec_out, fps_out = read_video(path)

        num_frames_out, frame_height_out, frame_width_out, num_channels_out = video_np_out.shape

        self.assertEqual(num_frames_in, num_frames_out)
        self.assertEqual(frame_height_in, frame_height_out)
        self.assertEqual(frame_width_in, frame_width_out)
        self.assertEqual(num_channels_in, num_channels_out)
        self.assertEqual(num_channels_in, 3)
        self.assertEqual(codec_in, codec_out)
        self.assertEqual(fps_in, fps_out)

        os.remove(path)


if __name__ == '__main__':
    main()