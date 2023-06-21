import unittest
from ..database.database import Database

class TestDatabase(unittest.TestCase):
    def setUp(self):
        self.database = Database()

    def test_save_gif(self):
        parameters = [0.1, 0.2, 0.3, 0.4, 0.5]
        image_path = 'test.gif'
        gif_id = self.database.save_gif(parameters, image_path)
        self.assertIsNotNone(gif_id)

    def test_get_gif(self):
        parameters = [0.1, 0.2, 0.3, 0.4, 0.5]
        image_path = 'test.gif'
        gif_id = self.database.save_gif(parameters, image_path)
        retrieved_image_path = self.database.get_gif(gif_id)
        self.assertEqual(retrieved_image_path, image_path)

if __name__ == '__main__':
    unittest.main()
