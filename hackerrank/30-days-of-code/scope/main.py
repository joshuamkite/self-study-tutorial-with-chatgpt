class Difference:
    def __init__(self, a):
        self.__elements = a
# add your code here
        self.maximumDifference = 0  # Initialize maximumDifference to 0

    def computeDifference(self):
        max_element = max(self.__elements)
        min_element = min(self.__elements)
        self.maximumDifference = max_element - \
            min_element  # Compute the maximum difference

# End of Difference class


_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
