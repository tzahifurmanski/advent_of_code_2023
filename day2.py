from collections import defaultdict
from functools import reduce


def handle_line_part1(game):
    # Strip game ID
    game_split = game.split(':')
    game_id = game_split[0].strip().split(' ')[1]

    # Strip by set ;
    set_split = [x.strip() for x in game_split[1].split(';')]

    # Limits for Part 1
    color_limits = {'red': 12, 'green': 13, 'blue': 14}

    for i, sets in enumerate(set_split):
        array_of_cubes = [x.strip() for x in sets.split(',')]

        # Iterate over cubes
        for j, cube in enumerate(array_of_cubes):
            cube_details = cube.split(' ')

            # Check cubes and limit by color
            if int(cube_details[0]) > color_limits[cube_details[1]]:
                return 0

    # Game is valid, return game ID
    return int(game_id)


def handle_line_part2(game):
    # Strip game ID
    game_split = game.split(':')

    # Strip by set ;
    set_split = [x.strip() for x in game_split[1].split(';')]

    color_min = defaultdict(int)

    for i, sets in enumerate(set_split):
        array_of_cubes = [x.strip() for x in sets.split(',')]

        for cube in array_of_cubes:
            cube_details = cube.split(' ')
            color_min[cube_details[1]] = max(color_min[cube_details[1]], int(cube_details[0]))

    # Calculate the power of all values
    return reduce((lambda x, y: x * y), color_min.values())


if __name__ == '__main__':
    part1_counter, part2_counter = 0, 0

    with open('day2_input.txt') as input_file:
        for line in input_file:
            part1_counter += handle_line_part1(line)
            part2_counter += handle_line_part2(line)

    print("Part1", part1_counter)
    print("Part2", part2_counter)
