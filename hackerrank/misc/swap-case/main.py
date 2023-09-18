def swap_case(s):
    swapped = []
    for item in s:
        if item == item.upper():
            swapped.append(item.lower())
        elif item == item.lower():
            swapped.append(item.upper())
        else:
            swapped.append(item)
    return ''.join(swapped)


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
