"""Utilities for reading and writing images from and to file."""

import cv2
import numpy as np
import matplotlib.pyplot as plt


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


def write_small_greyscale_image(image: np.ndarray, file_path: str):
    """Save greyscale <image> to <file_path>.

    This will work best with small images. For larger ones, should use
    write_image.

    Args:
        image: np.ndarray with element type np.uint8 and shape (28, 28).
        file_path: path to write image to.
    """

    image_len_1, image_len_2 = image.shape

    # Maps np.ndarray elements from an unbound range to [0, 1]. 
    pixel_normalization_op = plt.Normalize(image.min(), image.max())
    # Expands the dimensionality of an np.ndarray to have an RGBA column.
    gray_color_map = plt.cm.gray
    
    image = gray_color_map(pixel_normalization_op(image))


    ax = plt.gca()
    
    ax.set_xlabel('dim 2')
    ax.set_ylabel('dim 1')

    ax.set_xticks(np.arange(-1, image_len_1-1, 5))
    ax.set_yticks(np.arange(-1, image_len_2-1, 5))
    
    ax.set_xticklabels(np.arange(0, image_len_1, 5))
    ax.set_yticklabels(np.arange(0, image_len_2, 5))

    ax.grid(color='w', linestyle='-', linewidth=0.5)

    ax.xaxis.tick_top()
    ax.xaxis.set_label_position('top') 

    ax.imshow(image)

    plt.savefig(file_path, bbox_inches='tight')
