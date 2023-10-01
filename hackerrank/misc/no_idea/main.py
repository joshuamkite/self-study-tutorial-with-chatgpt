# Enter your code here. Read input from STDIN. Print output to STDOUT


if __name__ == "__main__":

    our_ints = [int(x) for x in input().split()]
    our_elements = [int(x) for x in input().split()]
    i_like = set([int(x) for x in input().split()])
    i_dislike = set([int(x) for x in input().split()])

    happiness = 0

    for n in our_elements:
        if n in i_like:
            happiness += 1
        if n in i_dislike:
            happiness -= 1
    print(happiness)
