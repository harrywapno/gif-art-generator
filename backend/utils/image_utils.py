import imageio
import numpy as np

def load_image(path):
    return np.array(imageio.imread(path))[:, :, :1] / 255.0

def save_image(image, path):
    imageio.mimsave(f'./frontend/img/{path}', [image], duration=0.1)
