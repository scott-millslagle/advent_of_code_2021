def final_location(commands):
    """
    Day 2: Dive! Advent of Code, 2021.
    https://adventofcode.com/2021/day/2

    :param commands: A .txt file listing navigation commands and their corresponding  of movement.
    :return: The number representing the final depth position by the final horizontal position.
    """
    final_destination = {
        "aim": 0,
        "horizontal": 0,
        "vertical": 0
    }

    file = open(commands, "r")

    for command in file.readlines():
        command = command.strip()

        direction, units = command.split()
        units = int(units)

        if direction == "up":
            final_destination["aim"] -= units
        elif direction == "down":
            final_destination["aim"] += units
        elif direction == "forward":
            final_destination["horizontal"] += units
            final_destination["vertical"] += final_destination["aim"] * units
    return final_destination["horizontal"] * final_destination["vertical"]




print(final_location("day_2_input.txt"))