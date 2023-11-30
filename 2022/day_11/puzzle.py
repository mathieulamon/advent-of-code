import os


class Monkey():
    def __init__(self, id, items, operator, value, divisible_by, throw_to_true, throw_to_false):
        self.id = id
        self.items = items
        self.operator = operator
        self.value = value
        self.divisible_by = divisible_by
        self.throw_to_true = throw_to_true
        self.throw_to_false = throw_to_false
        self.inspected_times = 0

    def add_item(self, item):
        self.items.append(item)

    def has_items(self):
        return len(self.items) > 0

    def get_item(self):
        if self.has_items():
            self.inspected_times += 1
            return self.items.pop(0)
        else:
            raise ValueError

    def print_items(self):
        print("Monkey {} inspected items {} times".format(
            self.id, self.inspected_times))


def parse_data(data):
    """ Extract values from data and put them in a dictionary of monkeys

    Args:
        data (list): All data

    Returns:
        monkeys (dict): Dictionary of monkeys
    """
    monkeys = {}  # Contains monkeys
    # Parse data
    for i in range(0, len(data), 7):
        # First line is monkey number
        monkey_number = int(data[i].split()[1][0])

        # Second line is items list
        all_items = data[i+1].split(':')[1]
        items = list(map(int, all_items.split(',')))

        # Third line is operator and value
        operator = data[i+2].split()[4]
        value = data[i+2].split()[5]
        value = -1 if value == 'old' else int(value)

        # Fourth line is divisible by
        divisible_by = int(data[i+3].split()[3])

        # Fifth line is throw if true
        throw_to_true = int(data[i+4].split()[5])

        # Sixth line is throw if false
        throw_to_false = int(data[i+5].split()[5])

        # At the end, create Monkey
        monkey = Monkey(monkey_number, items, operator, value, divisible_by,
                        throw_to_true, throw_to_false)

        # Append to dictionary
        monkeys[monkey_number] = monkey

    return monkeys


def read_input():
    """ Read data from file

    Returns:
        data (list): All data
    """
    script_path = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_path, 'input.txt')

    with open(file_path, 'r') as file:
        data = file.read().splitlines()
    file.close()

    return data


def solve_puzzle(data, nb_rounds, is_puzzle_1):
    """ Execute operations

    Args:
        data (list): List of data
        is_puzzle_1 (bool): Worry reduction change between puzzles
    """
    # Parse data
    monkeys = parse_data(data)

    if not is_puzzle_1:
        worry_reduction = 1
        for _, monkey in monkeys.items():
            worry_reduction *= monkey.divisible_by

    # Execute operations
    for i in range(nb_rounds):
        for _, monkey in monkeys.items():
            # Iterate over each item
            while monkey.has_items():
                # Get values
                worry = monkey.get_item()
                value = monkey.value if monkey.value > 0 else worry

                # Match operator
                match monkey.operator:
                    case '+':
                        new_worry = worry + value
                    case '*':
                        new_worry = worry * value

                # Divise by 3 because no damage (round down)
                new_worry = new_worry // 3 if is_puzzle_1 else new_worry % worry_reduction

                # Add item to right monkey
                if new_worry % monkey.divisible_by == 0:
                    monkeys[monkey.throw_to_true].add_item(new_worry)
                else:
                    monkeys[monkey.throw_to_false].add_item(new_worry)

    for _, monkey in monkeys.items():
        monkey.print_items()


if __name__ == '__main__':
    # Read input
    data = read_input()

    # Solve puzzle 1
    print("PUZZLE 1")
    solve_puzzle(data, 20, True)

    # Solve puzzle 2
    print("PUZZLE 2")
    solve_puzzle(data, 10000, False)
