import sys

class SortGroup:
    def __init__(self, group_point):
        self.group_point = group_point
        self.users = []

    def input(self):
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
                raise ValueError('only 0 <= n <- 123')
            self.users.append((name.strip(), age))
        except ValueError as e:
            print(f'error: {e}')

    def get_groups(self):
        groups = {}
        for lower, upper in zip(self.group_point, self.group_point[1:]):
            group_name = f"{lower}-{upper}" if upper < 123 else f"{lower}+"
            groups[group_name] = []

            for name, age in sorted(self.users, key=lambda x: (x[1], x[0])):
                if lower <= age <= upper:
                    groups[group_name].append((name, age))

        return groups

    def print(self, groups):
        for group, users in sorted(groups.items(), key=lambda x: x[0], reverse=True):
            if users:
                users_f = ", ".join([f"{name} ({age})" for name, age in users])
                print(f"{group}: {users_f}")


def main():
    try:
        bord = [int(arg) for arg in sys.argv[1:]]
        point = SortGroup(bord)
        point.input()
        result = point.get_groups()
        point.print(result)
    except ValueError:
        print('error')

if __name__ == "__main__":
    main()
