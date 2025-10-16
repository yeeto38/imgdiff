from PIL import Image as I
import matplotlib.pyplot as plt
import numpy as np

# takes in 2 np arrays and returns one np array
# 2 modes: 'a' absolute (just pure subtraction) and 'h' highlight (highlights different pixels)
def diff(i1: np.ndarray, i2: np.ndarray, mode: str) -> np.ndarray:
    if i1.shape != i2.shape:
        raise ValueError("both arrays need to be same size")
    if mode == 'h':
        mask = i1 != i2
        mdiff = np.zeros_like(i1, dtype=np.uint8)
        mdiff[mask] = 255
        return mdiff
    elif mode == 'a':
        return np.abs(i1 - i2)
    else:
        raise ValueError(f"unknown mode {mode}")
    
def diffshow(diffarray: np.ndarray):
    plt.imshow(diffarray, cmap='gray' if diffarray.ndim == 2 else None)
    plt.show()

def load(filename: str) -> np.ndarray:
    with I.open(filename) as out:
        return np.array(out.convert("L")) if out.mode in ["L", "LA"] else np.array(out.convert("RGB")).astype(np.uint8)
    
# def pickfilename(choice: str) -> str:
#     # ie. 132 for checkpoint 1 task 3 reference image 2 (the first turn sign in the hsv assignment
#     c = int(input("Checkpoint#"))
#     t = int(input("Task#"))
#     i = int(input("Image # (as it shows on website)"))
#     return "hi"