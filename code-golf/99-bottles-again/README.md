https://code.golf/99-bottles-of-beer#python

## Brief

Print the lyrics to the song 99 Bottles of Beer:

99 bottles of beer on the wall, 99 bottles of beer.
Take one down and pass it around, 98 bottles of beer on the wall.

98 bottles of beer on the wall, 98 bottles of beer.
Take one down and pass it around, 97 bottles of beer on the wall.

…

1 bottle of beer on the wall, 1 bottle of beer.
Take one down and pass it around, no more bottles of beer on the wall.

No more bottles of beer on the wall, no more bottles of beer.
Go to the store and buy some more, 99 bottles of beer on the wall.

## main.py

I attempted to return to the first code golf challenge that I had attempted, without referring to the previous solution or ChatGPT until I had solved it. Whilst I considered implementing conditional logic for special cases, I was concerned that this would not actually gain anything. Comparing to the solution derived with ChatGPT we can see that this is indeed the case- there are the same number of lines of code for the same result.

## main-golfed.py

This is an attempt to golf the above using variable string substitution:

| File       | main.py | main-golfed.py |
| ---------- | ------- | -------------- |
| Lines      | 14      | 8              |
| Characters | 644     | 350            |
    
Whilst it is effective, it's also a great example of why you don't want to golf code in the real world. Even I get to the end and am thinking "no more, no more, no more.." 
