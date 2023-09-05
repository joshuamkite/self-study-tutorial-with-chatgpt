class Person:
    def __init__(self, initialAge):
        # Add some more code to run some checks on initialAge
        if initialAge <= 0:
            self.age = 0
            print(f"Age is not valid, setting age to 0.")
        else:
            self.age = initialAge

    def amIOld(self):
        # Do some computations in here and print out the correct statement to the console
        if self.age < 13:
            print(f"You are young.")
        elif 13 <= self.age < 18:
            print(f"You are a teenager.")
        else:
            print(f"You are old.")

    def yearPasses(self):
        # Increment the age of the person in here
        self.age += 1


t = int(input())
