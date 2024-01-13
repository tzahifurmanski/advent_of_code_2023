# Description: Advent of Code - Day 1

# Part 1
# ==============================================
def generate_integers_list_part_1(line):
    return [int(x) for x in line if x.isdigit()]


# Part 2
# ==============================================
def generate_integers_list_part_2(line):
    digits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    list_of_integers = []
    temp_string = ""
    # Scan each character in the line
    for char in line:
        # If digit, save it and zero out saved string
        if char.isdigit():
            list_of_integers.append(int(char))
            temp_string = ""

        # If string, accumulate it and check if you got a written digit
        else:
            temp_string += char
            for num, digit in enumerate(digits, start=1):
                if digit in temp_string:
                    # If you did, save it and zero out saved string
                    list_of_integers.append(num)
                    # There was a really interesting bug here -
                    # In cases of "twone","eightwo", "threeight" I would miss the second number by "cleaning" the temp string  if I would clear out the temp string
                    # Instead, I initiate it to the last char.
                    # (and unless there are two numbers suffixes that are the same as two numbers prefexis, it should work).
                    temp_string = char

    return list_of_integers


def handle_line_part(line):
    # list_of_integers = generate_integers_list_part_1(line) #54081
    list_of_integers = generate_integers_list_part_2(line) #54649

    num = list_of_integers[0] * 10 + list_of_integers[-1]

    return int(num)


if __name__ == '__main__':
    counter = 0

    with open('day1_input.txt') as input_file:
        for line in input_file:
            counter += handle_line_part(line)

    print(counter)


# Other cool ideas:
# * Replace the words with digits, and then just do what I did in part 1 (one becomes o1ne)
# * Use a regex to find all the digits and words, in one go. For example:
# import re
#
# r = '1|2|3|4|5|6|7|8|9|one|two|three|four|five|six|seven|eight|nine'
#
# def f(line):
#   x = [*map({n: i%9+1 for i, n in enumerate(r.split('|'))}.get,
#     re.findall(rf'(?=({r}))', line))]
#   return 10*x[0] + x[-1]
#
# print(sum(map(f, open('data.txt'))))
# * A combination of the two above - for example:
# import re
#
# def f(line):
#     for i, n in enumerate(['one','two','three','four','five','six','seven','eight','nine']):
#         line = line.replace(n, n + str(i+1) + n)
#     x = re.findall(r'(\d)', line)
#     return int(x[0] + x[-1])
#
# print(sum(map(f, open('data.txt'))))