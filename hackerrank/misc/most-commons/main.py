#!/bin/python3

if __name__ == '__main__':
    s = list(input())
    score_map = {}  # empty map to store key: values
    for c in s:  # for each char in string
        if c in score_map:  # if char in map already
            score_map[c] += 1  # increase its score by 1
        else:
            score_map[c] = 1  # add char as key to map with a score of 1

    sorted_list = sorted(
        score_map.items(), key=lambda item: (-item[1], item[0]))

    for entry in (sorted_list[0:3]):  # first 3 items on list
        print(*entry)
