def check_depth(depth_data):
    """
    Day 1: Sonar Sweep, Advent of Code, 2021.
    https://adventofcode.com/2021/day/1

    :param depth_data: A .txt file of depth readings.
    :return: The number of times that the depth increased from the previous depth reading.
    """

    counter = 0
    file = (open(depth_data, "r"))

    previous_depth = 0
    for i in file.readlines():
        current_depth = int(i)
        if previous_depth == 0:
            previous_depth = current_depth
        elif current_depth > previous_depth:
            counter += 1
            previous_depth = current_depth
        else:
            previous_depth = current_depth
    return counter


if __name__ == "__main__":
    print(check_depth('input.txt'))
