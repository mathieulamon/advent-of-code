import os


class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_tuple(self):
        return (self.x, self.y)


class Rope():
    def __init__(self, nb_knots):
        self.knots = [Point(0, 0) for _ in range(nb_knots)]
        self.head = self.knots[0]
        self.tail = self.knots[-1]
        self.index = 0

    def has_next(self):
        return self.index + 1 < len(self.knots)

    def next(self):
        self.index += 1

        return self.knots[self.index]

    def reset(self):
        self.index = 0


def execute_moves(data, nb_knots):
    """ Move Up, Down, Left or Right the head based on the instruction
        The tail always need to be touching the head

    Args:
        data (list): Instructions about motions
        nb_knots (int): Number of knots of the rope

    Returns:
        result (int): Number of position the tail visit at least once
    """
    # Keep actual coordinates
    rope = Rope(nb_knots)

    # Use set to save distinct position
    positions = set()

    # Append starting position (arbitrary set to (0, 0))
    positions.add(rope.tail.get_tuple())

    # Iterate over instructions
    for value in data:
        # Get direction and number of steps
        direction, steps = value.split()
        steps = int(steps)

        match direction:
            case 'U':
                # Move up
                rope, positions = move(
                    rope, False, steps, 1, positions)
            case 'D':
                # Move down
                rope, positions = move(
                    rope, False, steps, -1, positions)
            case 'L':
                # Move left
                rope, positions = move(
                    rope, True, steps, -1, positions)
            case 'R':
                # Move right
                rope, positions = move(
                    rope, True, steps, 1, positions)

    # Return
    return len(positions)


def move(rope: Rope, move_x: bool, nb_steps: int, motion: int, positions: set):
    """ Execute motion

    Args:
        x_tail (int): value of x for the tail
        y_tail (int): value of y for the tail
        nb_steps (int): number of steps for the motion
        motion (int): +1 if it's to the right/up, -1 if it's to the left/down

    Returns:

    """

    for _ in range(nb_steps):
        current_node = rope.head  # Leader node
        next_node = rope.next()  # Node who need to move
        need_check = True  # True if current_node has moved (by default yes)

        # Move one step
        if move_x:
            current_node.x += motion
        else:
            current_node.y += motion

        while need_check:
            # Check if tail need to be moved
            if abs(current_node.x - next_node.x) > 1 or abs(current_node.y - next_node.y) > 1:
                # It means head and tail are not touching anymore

                diff_x = current_node.x - next_node.x
                diff_y = current_node.y - next_node.y

                if move_x:
                    if diff_y == 0:
                        # Move one point forward
                        next_node.x += 1 if diff_x > 0 else -1
                    elif diff_y == 1:
                        next_node.y += 1
                        next_node.x += 1 if diff_x > 0 else -1
                    elif diff_y == -1:
                        next_node.y -= 1
                        next_node.x += 1 if diff_x > 0 else -1
                    elif diff_y == 2:
                        next_node.y += 1
                        if diff_x == 2:
                            next_node.x += 1
                        elif diff_x == -2:
                            next_node.x -= 1
                        elif diff_x == 1:
                            next_node.x += 1
                        elif diff_x == -1:
                            next_node.x -= 1
                    elif diff_y == -2:
                        next_node.y -= 1
                        if diff_x == 2:
                            next_node.x += 1
                        elif diff_x == -2:
                            next_node.x -= 1
                        elif diff_x == 1:
                            next_node.x += 1
                        elif diff_x == -1:
                            next_node.x -= 1
                else:
                    if diff_x == 0:
                        # Move one point forward
                        next_node.y += 1 if diff_y > 0 else -1
                    elif diff_x == 1:
                        next_node.x += 1
                        next_node.y += 1 if diff_y > 0 else -1
                    elif diff_x == -1:
                        next_node.x -= 1
                        next_node.y += 1 if diff_y > 0 else -1
                    elif diff_x == 2:
                        next_node.x += 1
                        if diff_y == 2:
                            next_node.y += 1
                        elif diff_y == -2:
                            next_node.y -= 1
                        elif diff_y == 1:
                            next_node.y += 1
                        elif diff_y == -1:
                            next_node.y -= 1
                    elif diff_x == -2:
                        next_node.x -= 1
                        if diff_y == 2:
                            next_node.y += 1
                        elif diff_y == -2:
                            next_node.y -= 1
                        elif diff_y == 1:
                            next_node.y += 1
                        elif diff_y == -1:
                            next_node.y -= 1

                # Swap nodes
                if rope.has_next():
                    current_node = next_node
                    next_node = rope.next()
                else:
                    need_check = False

            else:
                need_check = False

        # Reset rope
        rope.reset()

        # Add last position
        positions.add(rope.tail.get_tuple())

    return rope, positions


def read_input():
    """ Read input from file

    Returns:
        data (list): List of all data
    """
    script_path = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_path, 'input.txt')

    with open(file_path, 'r') as file:
        data = file.read().splitlines()
    file.close()

    return data


if __name__ == '__main__':
    # Read input
    data = read_input()

    # Solve puzzle 1
    result = execute_moves(data, 2)

    # Display solution for puzzle 1
    print("The tail has visited {} different positions.".format(result))

    # Solve puzzle 2
    result = execute_moves(data, 10)

    # Display solution for puzzle 2
    print("The tail has visited {} different positions.".format(result))
