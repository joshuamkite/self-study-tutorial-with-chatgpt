for i in range(99, 2, -1):
    b = " bottles of beer"
    o = " on the wall"
    t = "Take one down and pass it around, "
    e = "1 bottle of beer"
    print(f"{i}{b}{o}, {i}{b}.\n{t}{i-1}{b}{o}.\n")

print(f"2{b}{o}, 2{b}.\n{t}{e}{o}.\n\n{e}{o}, {e}.\n{t}no more{b}{o}.\n\nNo more{b}{o}, no more{b}.\nGo to the store and buy some more, 99{b}{o}.")
