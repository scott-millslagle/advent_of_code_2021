def final_depth(commands):
    """
    Day 2: Dive! Advent of Code, 2021.
    https://adventofcode.com/2021/day/2

    :param commands: A .txt file listing navigation commands and their corresponding units of movement.
    :return: The number representing the final depth position by the final horizontal position.
    """
    final_destination = {
        "horizontal": 0,
        "vertical": 0
    }

    file = open(commands, "r")

    for command in file.readlines():
        command = command.strip()
        direction, distance = command.split()
        distance = int(distance)

        if direction == "up":
            final_destination["vertical"] -= distance
        elif direction == "down":
            final_destination["vertical"] += distance
        else:
            final_destination["horizontal"] += distance
    return final_destination["horizontal"] * final_destination["vertical"]