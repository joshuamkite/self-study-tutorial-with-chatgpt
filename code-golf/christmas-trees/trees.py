def print_line(numbers, max_width):
    """Prints a line of the tree with leading spaces."""
    line = ''.join(map(str, numbers))
    leading_spaces = (max_width - len(line)) // 2
    print(' ' * leading_spaces + line)

def tree(k, max_width):
    # Upper part of the tree
    for i in range(1, k+1):
        numbers = list(range(1, i+1)) + list(range(i-1, 0, -1))
        print_line("*"* len(numbers), max_width)

max_tree_size = 9
for i in range(3, max_tree_size+1):
    width = 2*i +2
    tree(i, width)
    print_line("*", width) # tree trunk
    if i != max_tree_size:  # Don't print a newline after the last tree
        print()  # Print a blank line
