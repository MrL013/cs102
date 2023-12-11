import unittest
from src.lab4.task2.code import SortGroup


class TestSortGroup(unittest.TestCase):

    def setUp(self):
        self.sort_group = SortGroup([0, 18, 35, 60, 80, 101])

    def test_get_groups_example(self):
        input_lines = [
            'Соколов Андрей Сергеевич 15',
            'Егоров Алан Петрович 7',
            'Кошельков Захар Брониславович 105',
            'Дьячков Нисон Иринеевич 88',
            'Иванов Варлам Якунович 88',
            'Ярилова Розалия Трофимовна 29',
            'Старостин Ростислав Ермолаевич 50',
            'END'
        ]
        result = self.sort_group.get_groups(input_lines)

        expected_output = [
            '101+: Кошельков Захар Брониславович (105)',
            '81-100: Дьячков Нисон Иринеевич (88), Иванов Варлам Якунович (88)',
            '46-60: Старостин Ростислав Ермолаевич (50)',
            '26-35: Ярилова Розалия Трофимовна (29)',
            '0-18: Соколов Андрей Сергеевич (15), Егоров Алан Петрович (7)'
        ]

        self.assertEqual(result, expected_output)

if __name__ == '__main__':
    unittest.main()




# class TestSortGroup(unittest.TestCase):

#     def test_init(self):
#         group_point = [10, 20, 30]
#         valid_group = SortGroup(group_point)
#         self.assertEqual(valid_group.group_point, group_point)
#         self.assertEqual(valid_group.users, [])

#         invalid_group_point = [10, 5]
#         with self.assertRaises(ValueError):
#             SortGroup(invalid_group_point)

#     def test_input(self):
#         group_point = [10, 20, 30]
#         group = SortGroup(group_point)

#         group.input()
#         self.assertGreater(len(group.users), 0)

#         with self.assertRaises(ValueError):
#             group.get_users("Баба зина 140")

#     def test_get_users(self):
#         group_point = [10, 20, 30]
#         group = SortGroup(group_point)

#         valid_user = "Лев Синюков 18"
#         group.get_users(valid_user)
#         self.assertIn(("Лев Синюков", 18), group.users)

#         invalid_user = "Лев Синюков"
#         with self.assertRaises(ValueError):
#             group.get_users(invalid_user)

#     def test_get_groups(self):
#         group_point = [10, 20, 30]
#         group = SortGroup(group_point)

#         group.input()
#         groups = group.get_groups()

#         self.assertIn("10-20", groups)
#         self.assertIn("21-30", groups)
#         self.assertEqual(len(groups["10-20"]), len(groups["21-30"]))

#         group_point = [10, 20, 123]
#         group = SortGroup(group_point)
#         group.input()
#         groups = group.get_groups()

#         self.assertIn("10-20", groups)
#         self.assertIn("21-123", groups)

#     def test_print(self):
#         group_point = [10, 20, 30]
#         group = SortGroup(group_point)

#         group.input()
#         groups = group.get_groups()

#         group.print(groups)


# if __name__ == "__main__":
#     unittest.main()