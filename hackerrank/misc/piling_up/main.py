# Enter your code here. Read input from STDIN. Print output to STDOUT

def list_sort(a_list):
    new_list = []
    while a_list:  # while list has elements remaining
        if a_list[0] > a_list[-1]:  # if first item > last item
            # pop first item and append to new_list
            new_list.append(a_list.pop(0))
        else:
            # pop last item and append to new_list
            new_list.append(a_list.pop(-1))
    return new_list


if __name__ == "__main__":
    t = int(input())  # a single integer , the number of test cases.
    # for line in input():

    data_list = []
    for _ in range(t):  # for each test case
        key = int(input())  # key for tuple
        # value is a list formed from splitting this line on space and casting to int
        value = [int(x) for x in input().split(' ')]
        # append result to our new list of tuples
        data_list.append((key, value))

    for item in data_list:  # for each entry in our list of tuples
        test_list = list_sort(item[1])  # run our function
        # Check if previous element is greater or equal in List Using zip() + list comprehension, casting to 'set' to ensure we have only one of each value
        res = set([int(sub1) >= int(sub2)
                  for sub1, sub2 in zip(test_list, test_list[1:])])
        if False in res:  # values are bools so check for bool value in set. Any occurrence of 'False' means "no"
            print("No")
        else:
            print("Yes")
