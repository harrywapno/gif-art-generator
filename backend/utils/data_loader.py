import pandas as pd
import numpy as np
from .image_utils import load_image

class DataLoader:
    def __init__(self):
        self.data = pd.read_csv('./data/gif_data.csv')

    def get_image(self, gif_id):
        return load_image(f'./data/gif_images/{gif_id}.gif')

    def get_parameters(self, gif_id):
        row = self.data.loc[self.data['gif_id'] == gif_id]
        parameters = np.array(row.iloc[:, 1:])
        return parameters
