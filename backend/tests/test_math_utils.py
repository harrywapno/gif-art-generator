import unittest
from ..utils.math_utils import generate_random_parameters

class TestMathUtils(unittest.TestCase):
    def test_generate_random_parameters(self):
        parameters = generate_random_parameters()
        self.assertEqual(len(parameters), 100)
        self.assertTrue(all(p >= -1 and p <= 1 for p in parameters))

if __name__ == '__main__':
    unittest.main()
