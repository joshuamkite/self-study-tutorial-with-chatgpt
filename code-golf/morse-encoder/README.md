https://code.golf/morse-encoder#python

## Brief

Using ▄ (U+2584 Lower Half Block) to represent a dot, encode the argument from alphanumeric into International Morse Code.

The length of a dot is one unit.
A dash is three units.
The space between parts of the same letter is one unit.
The space between letters is three units.
The space between words is ten units.

## main.py

This was arrived at without any use of ChatGPT. Here is started with the morse decoder code although here is simpler because we can use the dict conventionally. In this code we:

- loop to get input arguments
- loop to split input by word delimiter
- loop to split word by character delimiter - in this case we simply use the unpack operator treating each word as a list.
- print a look up each character in dict, adding `end="   "` to add the morse character delimiter and prevent newline after each encoded character
- print the morse delimiter between each encoded word
  
The last point above was what threw me a bit, although the delimiter is ten spaces, we only print seven because there are already three from the character's own delimiter and word gaps may only occur after a character.
