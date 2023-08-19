for n in range(1, 8):
    i=n*4
    print(n*" "," ", '\u2588', i*'\u2500', '\u2588', sep='')  # First line
    for j in reversed(range(0, n)):
        print((j+1)*" ", '\u2571', i*' ', '\u2571',
            ((n-j)-1)*" ", '\u2502', sep='')
    print('\u2588', i*'\u2500', '\u2588', (n-j)*" ", '\u2502', sep='')  # front top line
 
    for m in (range(0, (n-1))):
        print('\u2502', i*" ", '\u2502', (n-j)*" ", '\u2502', sep='')

    print('\u2502', i*" ", '\u2502', (n-j)*" ", '\u2588', sep='')  # bottom rear apex

    for k in reversed(range(0, n)):
        print('\u2502', i*" ", '\u2502', k*" ", '\u2571', sep='')
    print('\u2588', i*'\u2500', '\u2588', sep='')
    print("")
