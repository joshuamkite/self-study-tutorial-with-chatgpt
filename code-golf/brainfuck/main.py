def brainfuck_interpreter(bf_code):
    # Initialize the array and pointers
    array = [0] * 30000
    ptr = 0
    i = 0

    # Helper function to find the matching bracket
    def find_matching_bracket(code, index, direction):
        count = 1
        while count > 0:
            index += direction
            if code[index] == '[':
                count += direction
            elif code[index] == ']':
                count -= direction
        return index

    # Execute the Brainfuck code
    while i < len(bf_code):
        char = bf_code[i]
        if char == '>':
            ptr += 1
        elif char == '<':
            ptr -= 1
        elif char == '+':
            array[ptr] += 1
        elif char == '-':
            array[ptr] -= 1
        elif char == '.':
            print(chr(array[ptr]), end="")
        elif char == '[':
            if array[ptr] == 0:
                i = find_matching_bracket(bf_code, i, 1)
        elif char == ']':
            if array[ptr] != 0:
                i = find_matching_bracket(bf_code, i, -1)
        i += 1


if __name__ == "__main__":
    # Receive various Brainfuck programs as arguments
    import sys
    for bf_program in sys.argv[1:]:
        brainfuck_interpreter(bf_program)
