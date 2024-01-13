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
                    temp_string = ""
                    break

    return list_of_integers


def handle_line_part(line):
    list_of_integers = generate_integers_list_part_1(line) #54081
    # list_of_integers = generate_integers_list_part_2(line) #54627

    if len(list_of_integers) == 0:
        return 0
    elif len(list_of_integers) > 1:
        num = list_of_integers[0].__str__() + list_of_integers[-1].__str__()
    else:
        num = list_of_integers[0].__str__() * 2

    # print(num)
    return int(num)


if __name__ == '__main__':
    counter = 0

    with open('day1_input.txt') as input_file:
        for line in input_file:
            counter += handle_line_part(line)


    print(counter)
