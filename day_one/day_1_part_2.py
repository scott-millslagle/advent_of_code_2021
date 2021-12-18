def check_three_measurement_sliding(depth_data):
    """
    Day 1, Part 2: Sonar Sweep, Advent of Code, 2021.
    https://adventofcode.com/2021/day/1

    '--- Part Two ---
    Considering every single measurement isn't as useful as you expected: there's just too much noise in the data.
    Instead, consider sums of a three-measurement sliding window.'

    :param depth_data: A .txt file of depth readings.
    :return: The number of times that the depth increased from the previous depth reading.
    """

    counter = 0
    file = (open(depth_data, "r"))
    data_list = [int(i) for i in file.readlines()]

    previous_depth = 0
    for i in range(len(data_list)):
        current_depth = sum(data_list[i:i + 3])
        if previous_depth == 0:
            previous_depth = current_depth
        elif current_depth > previous_depth:
            counter += 1
            previous_depth = current_depth
        else:
            previous_depth = current_depth
    return counter

