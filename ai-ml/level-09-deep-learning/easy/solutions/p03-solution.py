"""Level 09 — Deep Learning — Easy P03 Solution"""

import numpy as np

def max_pool(image):
    h, w = image.shape
    out = np.zeros((h // 2, w // 2))
    for i in range(0, h, 2):
        for j in range(0, w, 2):
            out[i // 2, j // 2] = image[i:i+2, j:j+2].max()
    return out

if __name__ == "__main__":
    img = np.array([[1,3,2,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
    print(max_pool(img))
