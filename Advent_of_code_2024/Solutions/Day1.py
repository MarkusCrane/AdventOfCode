def open_file(file_path: str):
    """
    This function opens and returns a file.
    """
    lines = []
    with open(file_path, "r") as file:
        for line in file:
            lines.append(line.strip("\n"))
    return lines

input_file = open_file("Inputs/Day1.txt")

def part1():
    list1 = []
    list2 = []
    for item in input_file:
        split_locations = item.split("   ")
        list1.append(split_locations[0])
        list2.append(split_locations[1])

    total = 0
    for item in range(len(list1)):
        smallest_item1 = min(list1)
        smallest_item2 = min(list2)

        total += abs(int(smallest_item1) - int(smallest_item2))

        list1.remove(smallest_item1)
        list2.remove(smallest_item2)

    print(total)

def part2():
    list1 = []
    list2 = []
    for item in input_file:
        split_locations = item.split("   ")
        list1.append(split_locations[0])
        list2.append(split_locations[1])

    total = 0
    for item in list1:
        total += int(item) * int(list2.count(item))

    print(total)
part1()
part2()