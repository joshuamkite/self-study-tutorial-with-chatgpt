
def palindrome(b):
    a = list(b)
    c = a.copy()
    a.reverse()
    if a == c:
        return True
    else:
        return False
