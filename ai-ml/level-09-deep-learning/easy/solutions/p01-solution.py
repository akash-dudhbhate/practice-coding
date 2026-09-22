"""Level 09 — Deep Learning — Easy P01 Solution"""

import numpy as np

def convolve(image, kernel):
    h, w = image.shape
    kh, kw = kernel.shape
    out_h, out_w = h - kh + 1, w - kw + 1
    out = np.zeros((out_h, out_w))
    for i in range(out_h):
        for j in range(out_w):
            out[i, j] = np.sum(image[i:i+kh, j:j+kw] * kernel)
    return out

if __name__ == "__main__":
    img = np.array([[1,2,3,0],[4,5,6,0],[7,8,9,0],[0,0,0,0]])
    kernel = np.array([[1,0,-1],[1,0,-1],[1,0,-1]])
    print(convolve(img, kernel))
