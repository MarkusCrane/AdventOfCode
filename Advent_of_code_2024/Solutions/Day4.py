def read_file_to_matrix(filename):
    with open(filename, 'r') as file:
        return [list(line.strip()) for line in file]

input_file = read_file_to_matrix("Advent_of_code_2024/Inputs/Day4.txt")

def part1(matrix, word):
    """
    This function search a text file to find all instances of a given word.
    The word can be written fowards, backwards, vertically or diagonally.
    """
    def search_from_position(x, y, dx, dy):
        for i in range(len(word)):
            if not (0 <= x < len(matrix) and 0 <= y < len(matrix[0])):
                return False
            if matrix[x][y] != word[i]:
                return False
            x += dx
            y += dy
        return True

    def search_all_directions(x, y):
        directions = [(1, 0), (0, 1), (1, 1), (1, -1), (-1, 0), (0, -1), (-1, -1), (-1, 1)]
        words_found = 0
        for dx, dy in directions:
            if search_from_position(x, y, dx, dy):
                words_found += 1
        return words_found

    total_found = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            # For each co-ordinate in the matrix.
            words_found = search_all_directions(i, j)
            total_found += words_found

    return total_found

def part2(matrix, word):
    """
    This function search a text file to find all instances of a given word.
    The word can be written fowards, backwards, vertically or diagonally.
    """
    def search_from_position(x, y, dx, dy):
        letter_a_position = None
        for i in range(len(word)):
            if not (0 <= x < len(matrix) and 0 <= y < len(matrix[0])):
                return False, None
            if matrix[x][y] != word[i]:
                return False, None
            if word[i] == 'A':
                letter_a_position = (x, y)
            x += dx
            y += dy
        return True, letter_a_position

    def search_all_directions(x, y):
        directions = [(1, 1), (1, -1), (-1, -1), (-1, 1)]
        words_found = 0
        a_positions = []
        for dx, dy in directions:
            found, letter_a = search_from_position(x, y, dx, dy)
            if found:
                words_found += 1
                a_positions.append(letter_a)
        return words_found, a_positions

    total_found = 0
    total_letter_a = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            # For each co-ordinate in the matrix.
            words_found, letter_a_positions = search_all_directions(i, j)
            total_found += words_found
            total_letter_a += letter_a_positions

    return total_found, total_letter_a


# print(f"Word XMAS found {part1(input_file, 'XMAS')} times.")
words_found, letter_a_positions = part2(input_file, 'MAS')
print(f"Word MAS found {words_found} times.")
print(f"Letter A found {len(letter_a_positions)} times.")
print(f"{len(set(letter_a_positions))} uniques letter A's meaning {len(letter_a_positions) - len(set(letter_a_positions))} crosses.")


