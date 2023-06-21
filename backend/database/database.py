import sqlite3
from ..utils.math_utils import generate_random_parameters

class Database:
    def __init__(self):
        self.conn = sqlite3.connect('./data/gifs.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS gifs
                               (id INTEGER PRIMARY KEY AUTOINCREMENT,
                                parameters TEXT,
                                image_path TEXT)''')
        self.conn.commit()

    def save_gif(self, parameters, image):
        parameters_str = ','.join([str(p) for p in parameters])
        gif_id = self.cursor.execute(f"INSERT INTO gifs (parameters, image_path) VALUES ('{parameters_str}', '{image_path}')").lastrowid
        self.conn.commit()
        return gif_id

    def get_gif(self, gif_id):
        row = self.cursor.execute(f"SELECT image_path FROM gifs WHERE id = {gif_id}").fetchone()
        if row is None:
            return None
        return row[0]

    def get_random_parameters(self):
        return generate_random_parameters()
