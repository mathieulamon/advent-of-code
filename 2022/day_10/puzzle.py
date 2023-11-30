import os


def calculate_signal(data):
    """ Calculate signal strength during precise cycle

    Args:
        data (list): List of instructions and values

    Returns:
        result (int): Sum of the specific signal strengths
    """
    cycle = 0  # Define current cycle
    x = 1  # Start at one
    result = 0  # Contains result of specific signal

    # Iterate over lines
    for line in data:

        if line == 'noop':
            # Take one cycle to complete and do nothing
            cycle += 1

            # Check specific signal
            result = check_specific_signal(cycle, x, result)
        else:
            # Get value
            _, value = line.split()

            # Take two cycles to complete and add value to x
            for _ in range(2):
                # Increase cycle by one
                cycle += 1

                # Check specific signal
                result = check_specific_signal(cycle, x, result)

            x += int(value)

    return result


def check_specific_signal(cycle, x, result):
    """ Check if current signal is a specific

    Args:
        cycle (int): Current cycle
        x (int): Current register value
        result (int): Current value of previous specific cycle

    Returns:
        result (int): New result
    """
    match cycle:
        case 20:
            return result + x * 20
        case 60:
            return result + x * 60
        case 100:
            return result + x * 100
        case 140:
            return result + x * 140
        case 180:
            return result + x * 180
        case 220:
            return result + x * 220
        case _:
            return result


def draw_CRT(data):
    """ Draw a # if CRT is positionned in the right place, else draw a .

    Args:
        data (list): List of instructions and values
    """
    middle_crt = 1  # CRT is 3 wide, keep value of the middle
    crt_raw = ""  # Will contains # or .
    cycle = 0  # Current cycle

    for line in data:

        if line == 'noop':
            # Draw pixel
            crt_raw = draw_pixel(middle_crt, cycle, crt_raw)
            # Increase cycle by one
            cycle += 1
        else:
            # Get value
            _, value = line.split()

            # Take two cycles to complete and add value to x
            for _ in range(2):
                # Draw pixel
                crt_raw = draw_pixel(middle_crt, cycle, crt_raw)
                # Increase cycle by one
                cycle += 1

            middle_crt += int(value)

    print("Drawing from puzzle 2:")
    for i in range(0, len(crt_raw), 40):
        print(crt_raw[i:i+40])


def draw_pixel(middle_crt, cycle, crt_raw):
    """ Add a pixel in the CRT row (either # or .)

    Args:
        middle_crt: Current position of the sprite
        cycle: Current cycle
        crt_raw: Line containing pixels 
    """
    if abs(cycle % 40 - middle_crt) <= 1:
        crt_raw += '#'
    else:
        crt_raw += '.'

    return crt_raw


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
    result = calculate_signal(data)

    # Display solution for puzzle 1
    print("Sum of the signal strengths is {}.".format(result))

    # Solve puzzle 2
    result = draw_CRT(data)
