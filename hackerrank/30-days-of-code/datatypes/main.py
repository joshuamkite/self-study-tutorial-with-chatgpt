import sys
i = 4
d = 4.0
s = 'HackerRank '
# Declare second integer, double, and String variables.

# These are not really needed because in Python there is no need to declare them before they are assigned

j = int()
k = float()  # no double in Python AFAIK
l = ""

# Read and save an integer, double, and String to your variables.

msg = sys.stdin.read()
lines = msg.split('\n')
j = int(lines[0])
k = float(lines[1])
l = lines[2]


# Print the sum of both integer variables on a new line.
print(i+j)

# Print the sum of the double variables on a new line.
print(d+k)

# Concatenate and print the String variables on a new line
# The 's' variable above should be printed first.
print(f"{s}{l}")
