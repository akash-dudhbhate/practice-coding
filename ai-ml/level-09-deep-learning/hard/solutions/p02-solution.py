"""Level 09 — Deep Learning — Hard P02 Solution"""

from torchvision import transforms

def augment_pipeline():
    return transforms.Compose([
        transforms.RandomHorizontalFlip(),
        transforms.RandomRotation(15),
        transforms.RandomCrop(32, padding=4),
        transforms.ColorJitter(brightness=0.2, contrast=0.2),
        transforms.ToTensor(),
        transforms.Normalize((0.5,), (0.5,))
    ])

if __name__ == "__main__":
    t = augment_pipeline()
    print(t)
    from PIL import Image
    import numpy as np
    img = Image.fromarray(np.random.randint(0, 255, (32, 32, 3), dtype=np.uint8))
    out = t(img)
    print(out.shape)
