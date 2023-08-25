for i in range(99, 0, -1):
    if i > 2:
        print(f"{i} bottles of beer on the wall, {i} bottles of beer.")
        print(
            f"Take one down and pass it around, {i - 1} bottles of beer on the wall.\n")
    elif i == 2:
        print(f"{i} bottles of beer on the wall, {i} bottles of beer.")
        print(f"Take one down and pass it around, 1 bottle of beer on the wall.\n")
    elif i == 1:
        print("1 bottle of beer on the wall, 1 bottle of beer.")
        print("Take one down and pass it around, no more bottles of beer on the wall.\n")

print("No more bottles of beer on the wall, no more bottles of beer.")
print("Go to the store and buy some more, 99 bottles of beer on the wall.")
