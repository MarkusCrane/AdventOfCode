import re

def open_file(file_path: str):
    """
    This function opens and returns a file.
    """
    lines = []
    with open(file_path, "r") as file:
        for line in file:
            lines.append(line.strip("\n"))
    return lines

input_file = open_file("Advent_of_code_2024/Inputs/Day3.txt")

def part1():
    file_contents = ""
    for line in input_file:
        file_contents += line
    # file_contents = file_contents.split("m")

    REGEX_STRING = re.compile("mul\([0-9]{1,3}\,[0-9]{1,3}\)")
    valid_commands = REGEX_STRING.findall(file_contents)
    total = 0
    for item in valid_commands:
        item = item.replace("mul(", "")
        item = item.replace(")", "")
        item = item.split(",")
        total += int(item[0]) * int(item[1])
    
    print(total)

    


def part2():
    file_contents = ""
    for line in input_file:
        file_contents += line
    # file_contents = file_contents.split("m")

    REGEX_STRING = re.compile("mul\([0-9]{1,3}\,[0-9]{1,3}\)|do\(\)|don't\(\)")
    valid_commands = REGEX_STRING.findall(file_contents)

    total = 0
    do = True
    for item in valid_commands:
        if item == "do()":
            do = True
        elif item == "don't()":
            do = False
        elif do:
            item = item.replace("mul(", "")
            item = item.replace(")", "")
            item = item.split(",")
            total += int(item[0]) * int(item[1])
    
    print(total)

# part1()
part2()