def open_file(file_path: str):
    """
    This function opens and returns a file.
    """
    lines = []
    with open(file_path, "r") as file:
        for line in file:
            lines.append(line.strip("\n"))
    return lines

def remove_blanks(input_list: list):
    """
    This function removes blank lines from a list.
    """
    while "" in input_list:
        input_list.remove("")
    return input_list

def remove_non_numeric_characters(input_string: str) -> int:
    """
    This function removes all non-numeric characters from a string.
    """
    numeric_characters = ""
    for character in input_string:
        if character.isnumeric():
            numeric_characters += str(character)
    return int(numeric_characters)