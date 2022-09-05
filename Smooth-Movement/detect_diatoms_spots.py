from pathlib import Path
import cv2
import numpy as np
from typing import List


IMG_PATH = Path("Smooth-Movement/data/40x_100fps_b5/img-0001.png")
RESULTS_DIR = Path("Smooth-Movement/data/corner_params")
BLOCK_SIZE_RANGE = range(5, 11, 3)
# BLOCK_SIZE_RANGE = [2]
# APERTURE_SIZE_RANGE = range(3,21,2)
APERTURE_SIZE_RANGE = [3, 7, 19]
# K_RANGE = np.linspace(0.19, 0.2, 2)
# K_RANGE = np.linspace(0.17, 0.23, int((0.23-0.17)/0.01)+1)
K_RANGE = [0.1, 0.19, 0.4]
IMG_CROP_RANGE = [300, 400, 400, 600]


def detect_diatoms_spots(
    img_path: Path,
):
    img = cv2.imread(str(img_path))
    img = img[300:400, 400:600, :]
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = np.float32(gray)
    dst = cv2.cornerHarris(gray, 2, 3, 0.04)
    dst = cv2.dilate(dst, None)
    img[dst > 0.01 * dst.max()] = [0, 0, 255]
    cv2.imshow("dst", dst)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def check_corner_params_range(
    img_path: Path,
    results_dir: Path,
    block_size_range: List[int],
    aperture_size_range: List[int],
    k_range: List[float],
    img_crop_range: List[int],
):
    results_dir.mkdir(parents=True, exist_ok=True)
    c = img_crop_range
    img = cv2.imread(str(img_path))
    img = img[c[0] : c[1], c[2] : c[3], :]
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = np.float32(gray)
    cv2.imwrite(str(results_dir / "orig_crop.png"), img)
    cv2.imwrite(str(results_dir / "gray_crop.png"), gray)
    for blo in block_size_range:
        for aper in aperture_size_range:
            for k in k_range:
                dst = cv2.cornerHarris(gray, blo, aper, k)
                dst = cv2.dilate(dst, None)
                cur_img = img.copy()
                cur_img[dst > 0.5 * dst.max()] = [0, 0, 255]
                filepath = results_dir / f"block_{blo}_aperture_{aper}_k_{k:.2f}.png"
                cv2.imwrite(str(filepath), cur_img)

    return
    cv2.imshow("dst", cur_img[40:80, 105:120, :])
    # cv2.imshow('dst',cur_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    pass


if __name__ == "__main__":
    # detect_diatoms_spots(IMG_PATH)
    check_corner_params_range(
        IMG_PATH,
        RESULTS_DIR,
        BLOCK_SIZE_RANGE,
        APERTURE_SIZE_RANGE,
        K_RANGE,
        IMG_CROP_RANGE,
    )
    pass
