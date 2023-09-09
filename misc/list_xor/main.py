def list_xor(n, list1, list2):
    if n in list1:
        if n not in list2:
            return True
        else:
            return False
    else:
        if n in list2:
            return True
        else:
            return False
