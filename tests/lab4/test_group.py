
import unittest
from src.lab4.task2.code import SortGroup

class TestSortGroup(unittest.TestCase):
    def test_get_users_valid_input(self):
        group = SortGroup([0, 18, 35, 80, 101])
        group.get_users("Максим Максимов 25")
        self.assertEqual(group.users, [("Максим Максимов", 25)])

    def test_get_users_invalid_input(self):
        group = SortGroup([0, 18, 35, 80, 101])
        group.get_users("Invalid Input")
        self.assertEqual(group.users, [])

    def test_get_groups(self):
        group = SortGroup([0, 18, 35, 80, 101])
        group.users = [("Соколов Андрей Сергеевич", 15), ("Ярилова Розалия Трофимовна", 29), ("Старостин Ростислав Ермолаевич", 50), ("Дьячков Нисон Иринеевич", 88), ("Иванов Варлам Якунович", 88), ("Кошельков Захар Брониславович", 105)]
        result = group.get_groups()
        self.assertEqual(result, {
            '101+': [('Кошельков Захар Брониславович', 105)],
            '80-101': [('Дьячков Нисон Иринеевич', 88), ('Иванов Варлам Якунович', 88)],
            '35-80': [('Старостин Ростислав Ермолаевич', 50)],
            '18-35': [('Ярилова Розалия Трофимовна', 29)],
            '0-18': [('Соколов Андрей Сергеевич', 15)]
        })

if __name__ == "__main__":
    unittest.main()
