def stopping_time(n, i):
    if n==1:# condition changed from `if n>1` by ChatGPT
        return i #`return` and moving to top suggested by ChatGPT
    else:
        if n % 2 == 0:  # If n is even
            n=n/2  # divide it by 2
        else:  # otherwise
            n= (n*3)+1  # multiply by 3 and then add 1.
        i+=1
        return stopping_time(n, i)#`return` suggested by ChatGPT


for n in range(1, 1001):
    print(stopping_time(n, 0))