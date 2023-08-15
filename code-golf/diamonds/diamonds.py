def diamond(k, max_width):
    # Upper part of the diamond
    for i in range(1, k+1):
        total_width_current_line = 2*i - 1
        leading_spaces = (max_width - total_width_current_line) // 2
        print(' ' * leading_spaces, end='')  # Adjusted leading spaces
        for j in range(1, i+1):
            print(j, end='')
        for j in range(i-1, 0, -1):  # Print decreasing numbers
            print(j, end='')
        print()  # Move to the next line

    # Lower part of the diamond
    for i in range(k-1, 0, -1):
        total_width_current_line = 2*i - 1
        leading_spaces = (max_width - total_width_current_line) // 2
        print(' ' * leading_spaces, end='')  # Adjusted leading spaces
        for j in range(1, i+1):
            print(j, end='')
        for j in range(i-1, 0, -1):  # Print decreasing numbers
            print(j, end='')
        print()  # Move to the next line


max_diamond_size = 9
max_width = 2*max_diamond_size + 1
for i in range(1, max_diamond_size+1):
    diamond(i, max_width)
    if i != max_diamond_size:  # Don't print a newline after the last diamond
        print()  # Print a blank line
