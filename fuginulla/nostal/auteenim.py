def directionNumberToSymbol(number):
    """
    Converts a direction number to a symbol using a dictionary.

    Args:
        number (int): The direction number.

    Returns:
        str: The symbol.
    """
    direction_map = {
        0: "N", 1: "NE", 2: "E", 3: "SE",
        4: "S", 5: "SW", 6: "W", 7: "NW"
    }

    return direction_map.get(number, "Invalid direction number: {}".format(number))

# Example usage:
print(directionNumberToSymbol(0))  # Output: N
print(directionNumberToSymbol(7))  # Output: NW
print(directionNumberToSymbol(8))  # Output: Invalid direction number: 8
