"""Utilities for reading and writing videos from and to files."""

import cv2
import numpy as np
from typing import Tuple


def decode_fourcc(fourcc_enum: int) -> str:
    '''Convert an integer encoding of a fourcc codec code to its string name.'''

    fourcc_str = ''

    for i in range(4):
        fourcc_value = fourcc_enum >> 8 * i & 0xFF
        fourcc_str += chr(fourcc_value)

    return fourcc_str


def read_video(path: str) -> Tuple[np.ndarray, int, float]:
    '''Reads RGB video bytes from a file.

    Args:
        path: a file path to a video.

    Returns:
        Raw video bytes. Shape is (N, H, W, 3), each element is a uint8 in [0, 255].
        fourcc codec (in string form) that was was used to decode the video bytes.
        frames-per-second of video bytes.
    '''

    video_capture = cv2.VideoCapture(path)

    num_frames = int(video_capture.get(cv2.CAP_PROP_FRAME_COUNT))
    if num_frames == 0:
        return None, None, None

    fps = int(video_capture.get(cv2.CAP_PROP_FPS))

    width = int(video_capture.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT))

    codec_enum = int(video_capture.get(cv2.CAP_PROP_FOURCC))
    codec = decode_fourcc(codec_enum)

    video_np = np.empty((num_frames, height, width, 3), np.dtype('uint8'))
    frame_idx, not_done = 0, True

    # Fill in video_np, frame-by-frame.
    while (frame_idx < num_frames and not_done):
        not_done, content = video_capture.read()

        video_np[frame_idx, :, :, :] = content
        frame_idx += 1

    video_capture.release()

    return video_np, codec, fps


def write_video(path: str,
                video_np: np.ndarray,
                codec: str,
                fps: float) -> bool:
    '''Writes an RGB video, from NumPy bytes, to a file path.

    TODO(skeselj): make this not fail silently when there is no dir.

    Args:
        path: the filepath to write to.
        video_np: raw video bytes. Shape is (N, H, W, 3), each element is a uint8 in in [0, 255].
        codec: fourcc codec (in string form) to use to encode the video bytes. e.g. 'mp4v'.
        fps: frames-per-second of video bytes.

    Returns:
        Status: True if success, False if failure.
    '''

    num_frames, frame_height, frame_width, num_channels = video_np.shape
    assert num_channels == 3

    is_color = True
    video_writer = cv2.VideoWriter(path, cv2.VideoWriter_fourcc(*codec),
                                   fps, (frame_width, frame_height), is_color)

    for frame_idx in range(num_frames):
        frame_np = video_np[frame_idx, :, :, :]
        video_writer.write(frame_np)

    video_writer.release()

    return True

