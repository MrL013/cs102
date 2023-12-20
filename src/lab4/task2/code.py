
import sys

class SortGroup:
    def __init__(self, group_point):
        self.group_point = group_point
        self.users = []

    def input_data(self):
        while True:
            input_data = input()
            if input_data == 'END':
                break
            else:
                self.get_users(input_data)

    def get_users(self, respondent_data):
        try:
            name, age_str = respondent_data.rsplit(' ', 1)
            age = int(age_str)
            if age < 0 or age > 123:
                raise ValueError('Only 0 <= n < 123')
            self.users.append((name.strip(), age))
        except ValueError as e:
            print(f'Error: {e}')

    def get_groups(self):
        groups = {}
        for lower, upper in zip(self.group_point, self.group_point[1:]):
            group_name = f"{lower}-{upper}" if upper < 123 else f"{lower}+"
            groups[group_name] = []

            for name, age in sorted(self.users, key=lambda x: (x[1], x[0])):
                if lower <= age <= upper:
                    groups[group_name].append((name, age))

            if upper == self.group_point[-1]:
                last_group_name = f"{self.group_point[-1]}+"
                if last_group_name not in groups:
                    groups[last_group_name] = []
                for name, age in sorted(self.users, key=lambda x: (x[1], x[0])):
                    if age > upper:
                        groups[last_group_name].append((name, age))

        return groups

    def display_groups(self, groups):
        for group, users in sorted(groups.items(), key=lambda x: x[0], reverse=True):
            if users:
                users_f = ", ".join([f"{name} ({age})" for name, age in users])
                print(f"{group}: {users_f}")


def main():
    try:
        bord = list(map(int, input().split()))
        point = SortGroup(bord)
        point.input_data()
        result = point.get_groups()
        point.display_groups(result)
    except ValueError:
        print('Error')
    

if __name__ == "__main__":
    main()
