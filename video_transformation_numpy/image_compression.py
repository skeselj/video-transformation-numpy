"""Functions that map images to simpler representations."""

import numpy as np


def group_rows_by_avg(image_np: np.ndarray) -> np.ndarray:
    """Averages the rows of an image and returns the output. 
    
    Args:
        image_np: np.ndarray of shape (H, W, 3). Represents an image.
            Each element is a uint8 in [0, 255].

    Returns:
        A np.ndarray of shape (H, 3). Each element is the average of a
        single row in <image_np> and is a uint8 [0, 255]

    """

    return image_np.mean(axis=1).astype(np.uint8)
