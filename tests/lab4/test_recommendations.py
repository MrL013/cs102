import unittest
from src.lab4.1.1 import Recommendations_system

class TestRecommendationsSystem(unittest.TestCase):

    def setUp(self):
        self.recSystem = Recommendations_system('src/lab4/1/files/films.txt', 'src/lab4/1/files/history.txt')

    def test_check_films(self):
        self.assertEqual(self.recSystem.check_films('src/lab4/1/files/films.txt'), {1: 'Мстители: Финал', 2: 'Хатико', 3: 'Дюна', 4: 'Унесенные призраками'})
        
    def test_check_history(self):
        self.assertEqual(self.recSystem.check_history('src/lab4/1/files/history.txt'), [[1, 2, 3], [2, 4], [1, 3, 5]])
        
    def test_recomendation_system(self):
        self.assertEqual(self.recSystem.recomendation_system([1, 2]), 'Дюна')
        self.assertEqual(self.recSystem.recomendation_system([2, 4]), 'Дюна')
        self.assertEqual(self.recSystem.recomendation_system([1, 4]), 'Хатико')
        self.assertEqual(self.recSystem.recomendation_system([3, 4]), 'Хатико')
        self.assertEqual(self.recSystem.recomendation_system([2, 3]), 'Мстители: Финал')
        self.assertEqual(self.recSystem.recomendation_system([]), 'no recomendation')
        self.assertEqual(self.recSystem.recomendation_system([5, 7]), 'no recomendation')

if __name__ == '__main__':
    unittest.main()