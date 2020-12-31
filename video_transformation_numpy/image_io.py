"""Utilities for reading and writing images from and to file."""

import cv2
import numpy as np


def read_image(path: str) -> np.ndarray:
    """Load an image from file using cv2.
    Args:
        path: path to an image. JPEG format works, other formats probably work too.
    Returns:
        Shape is (H, W, 3). Each element is a uint8 in [0, 255].
    Raises:
        ValueError:
            * If path does not reference an image that can be read by OpenCV.
    """

    try:
        input_image_np = cv2.imread(path)
    except:
        raise ValueError('Inputted path does not reference an image that can be read by OpenCV.')
    if input_image_np is None:
        raise ValueError('Inputted path does not reference an image that can be read by OpenCV.')

    height, width, num_channels = input_image_np.shape

    assert num_channels == 3, f'num_channels = {num_channels} != 3'

    return input_image_np


def write_image(path: str, image_np: np.ndarray) -> np.ndarray:
    """Write an image to a path using cv2.

    TODO(skeselj): make this not fail silently when there is no dir.

    Args:
        path: path to an image. JPEG format works, other formats probably work too.
        image_np: array with shape (H, W, 3). Each element is a uint8 in [0, 255].

    Returns:
        Nothing.
    """

    height, width, num_channels = image_np.shape
    assert num_channels == 3, f'{num_channels}'

    cv2.imwrite(path, image_np)
