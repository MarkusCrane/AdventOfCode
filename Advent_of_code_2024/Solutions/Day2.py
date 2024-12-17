def open_file(file_path: str):
    """
    This function opens and returns a file.
    """
    lines = []
    with open(file_path, "r") as file:
        for line in file:
            lines.append(line.strip("\n"))
    return lines

input_file = open_file("Inputs/Day2.txt")

def part1():
    safe_reports = 0
    for report in input_file:
        report = report.split(" ")
        differences = []
        for item in range(len(report)-1):
            differences.append(int(report[item]) - int(report[item+1]))
        if set(differences) <= {1, 2, 3} or set(differences) <= {-1, -2, -3}:
            safe_reports += 1

    print(safe_reports)

def part2():
    safe_reports = 0
    for report in input_file:
        report = report.split(" ")
        differences = []
        for item in range(len(report)-1):
            differences.append(int(report[item]) - int(report[item+1]))

        if set(differences) <= {1, 2, 3} or set(differences) <= {-1, -2, -3}:
            safe_reports += 1
        else:
            possible_dampened_reports = []
            for item in range(len(report)):
                possible_dampened_reports.append(report.copy())
            x=0
            for item in possible_dampened_reports:
                item.pop(x)
                x+=1
            for report in possible_dampened_reports:
                differences = []
                for item in range(len(report)-1):
                    differences.append(int(report[item]) - int(report[item+1]))
                if set(differences) <= {1, 2, 3} or set(differences) <= {-1, -2, -3}:
                    safe_reports += 1
                    break

    print(safe_reports)
# part1()
part2()