https://code.golf/morse-decoder#python

## Brief

Using ▄ (U+2584 Lower Half Block) to represent a dot, decode the argument from International Morse Code to alphanumeric.

The length of a dot is one unit.
A dash is three units.
The space between parts of the same letter is one unit.
The space between letters is three units.
The space between words is ten units.

## main.py

This was arrived at without any use of ChatGPT. Whilst the [advice on how to get a key from a dict by value at geeksforgeeks.org](https://www.geeksforgeeks.org/python-get-key-from-value-in-dictionary/) is correct. The advice at [Stack Overflow](https://stackoverflow.com/questions/8023306/get-key-by-value-in-dictionary) was much more useful. In this code we:

- loop to get input arguments
- loop to split input by word delimiter
- loop to split word by character delimiter
- print a look up each character in dict -
  > [Basically, it separates the dictionary's values in a list, finds the position of the value you have, and gets the key at that position.](https://stackoverflow.com/questions/8023306/get-key-by-value-in-dictionary)
  
  Adding `end=""` to prevent newline after each decoded character
- print a single space between each decoded word
