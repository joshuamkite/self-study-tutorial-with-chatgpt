def print_line(numbers, max_width):
    """Prints a line of the diamond with leading spaces."""
    line = ''.join(map(str, numbers))
    leading_spaces = (max_width - len(line)) // 2
    print(' ' * leading_spaces + line)

def diamond(k, max_width):
    # Upper part of the diamond
    for i in range(1, k+1):
        numbers = list(range(1, i+1)) + list(range(i-1, 0, -1))
        print_line(numbers, max_width)

    # Lower part of the diamond
    for i in range(k-1, 0, -1):
        numbers = list(range(1, i+1)) + list(range(i-1, 0, -1))
        print_line(numbers, max_width)

max_diamond_size = 9
max_width = 2*max_diamond_size +2
for i in range(1, max_diamond_size+1):
    diamond(i, max_width)
    if i != max_diamond_size:  # Don't print a newline after the last diamond
        print()  # Print a blank line
