# Self-study tutorial with ChatGPT

Original code based on my own designs with assistance from ChatGPT as part of my self-designed tutorial course, as described at [my website](https://www.joshuakite.co.uk/posts/writing_my_own_tutorial_course.html)

- [Self-study tutorial with ChatGPT](#self-study-tutorial-with-chatgpt)
  - [advent-of-code-2022](#advent-of-code-2022)
    - [day-8](#day-8)
  - [code-golf](#code-golf)
    - [roman-to-arabic](#roman-to-arabic)
    - [diamonds](#diamonds)
    - [united-states](#united-states)
    - [christmas-trees](#christmas-trees)
    - [collatz](#collatz)
    - [cubes](#cubes)
    - [fizz-buzz](#fizz-buzz)
    - [day-of-the-week](#day-of-the-week)
    - [abundant-numbers](#abundant-numbers)
    - [abundant-numbers-long](#abundant-numbers-long)
    - [brainfuck](#brainfuck)
    - [arrows](#arrows)
    - [intersection](#intersection)
    - [pangram](#pangram)
    - [divisors](#divisors)
    - [seven-segment](#seven-segment)
    - [isbn](#isbn)
    - [leap years](#leap-years)
    - [morse-decoder](#morse-decoder)
    - [morse-encoder](#morse-encoder)
    - [99-bottles-again](#99-bottles-again)
    - [number-spiral](#number-spiral)
    - [maze](#maze)
      - [Example](#example)
    - [zodic-signs](#zodic-signs)
    - [Rock-paper-scissors-Spock-lizard](#rock-paper-scissors-spock-lizard)
  - [Hacker Rank](#hacker-rank)
    - [Project Euler #1: Multiples of 3 and 5](#project-euler-1-multiples-of-3-and-5)
    - [30 Days of Code](#30-days-of-code)
      - [dataypes](#dataypes)
      - [Operators](#operators)
      - [Intro-to-Conditional-Statements](#intro-to-conditional-statements)
      - [loops](#loops)
      - [class-vs-instance](#class-vs-instance)
      - [Let's Review](#lets-review)
      - [arrays](#arrays)
      - [dictionaries\_and\_maps](#dictionaries_and_maps)
  - [Misc](#misc)
    - [custom\_zip](#custom_zip)
    - [list\_xor](#list_xor)
    - [Counting syllables](#counting-syllables)
    - [counting-parameters](#counting-parameters)
 
 
 ## advent-of-code-2022
 Examples from 'Advent of Code (2022)' Challenges 
 ### [day-8](./advent-of-code-2022/day-8/)

## code-golf

Solutions to problems from [code.golf](https://code.golf)

### [roman-to-arabic](./code-golf/roman-to-arabic)

programs to convert roman numerals to arabic numerals

### [diamonds](./code-golf/diamonds)

Draw a size ascending range of diamonds using the numbers 1 to 9, ranging from size 1 to size 9, each diamond separated by a blank line.

### [united-states](./code-golf/united-states)

Given each US state (and a federal district) print the corresponding US Postal Service abbreviation.

### [christmas-trees](./code-golf/christmas-trees)

Draw a size ascending range of Christmas trees using asterisks, ranging from size 3 to size 9, each tree separated by a blank line.

### [collatz](./code-golf/collatz)

The Collatz conjecture states that, for any positive integer n, it will eventually reach 1 by repeatedly applying the following procedure:

If n is even, divide it by 2.
If n is odd, multiply by 3 and then add 1.
The number of steps needed for n to reach 1 is called its stopping time.

Print the stopping times of all the numbers from 1 to 1,000 inclusive, each on their own line.#

### [cubes](./code-golf/cubes)

Draw 7 cubes in increasing size using "╱" (U+2571) for the diagonal edges, "│" (U+2502) for the vertical edges, "─" (U+2500) for the horizontal edges, and "█" (U+c) for the vertices. The cubes should range from size 1 to size 7 with a blank line between each cube.

### [fizz-buzz](./code-golf/fizz-buzz)

Print the numbers from 1 to 100 inclusive, each on their own line.

If, however, the number is a multiple of three then print Fizz instead, and if the number is a multiple of five then print Buzz.

If multiple conditions hold true then all replacements should be printed, for example 15 should print FizzBuzz.

### [day-of-the-week](./code-golf/day-of-the-week)

Given a date in the YYYY-MM-DD format between 1583-01-01 and 9999-12-31 inclusive, output the English name of the corresponding day of the week.

### [abundant-numbers](./code-golf/abundant-numbers)

An abundant number is a number for which the sum of its proper divisors (divisors not including the number itself) is greater than the number itself. For example 12 is abundant because its proper divisors are 1, 2, 3, 4, and 6 which add up to 16.

Print all the abundant numbers from 1 to 200 inclusive, each on their own line.

### [abundant-numbers-long](./code-golf/abundant-numbers-long)

An abundant number is a number for which the sum of its proper divisors (divisors not including the number itself) is greater than the number itself. For example 12 is abundant because its proper divisors are 1, 2, 3, 4, and 6 which add up to 16.

Print all the abundant numbers from 1 to 10000 inclusive, each on their own line.

### [brainfuck](./code-golf/brainfuck)

Brainfuck is a minimalistic esoteric programming language created by Urban Müller in 1993.

Assuming an infinitely large array, the entire brainfuck alphabet matches the following pseudocode:

```
>	ptr++
<	ptr--
+	array[ptr]++
-	array[ptr]--
.	print(chr(array[ptr]))
[	while(array[ptr]){
]	}
```

Write a program that will receive various brainfuck programs as arguments and execute each program in turn.

### [arrows](./code-golf/arrows)

Starting at [0, 0] print the cumulative result of applying each of the given Unicode arrow arguments. The arrows will be a random combination of these:

```json
{
    "↙": [-1, -1], "↲": [-1, -1], "⇙": [-1, -1],
    "←": [-1,  0], "⇐": [-1,  0], "⇦": [-1,  0],
    "↖": [-1,  1], "↰": [-1,  1], "⇖": [-1,  1],
    "↓": [ 0, -1], "⇓": [ 0, -1], "⇩": [ 0, -1],
    "↔": [ 0,  0], "↕": [ 0,  0], "⇔": [ 0,  0],
    "⇕": [ 0,  0], "⥀": [ 0,  0], "⥁": [ 0,  0],
    "↑": [ 0,  1], "⇑": [ 0,  1], "⇧": [ 0,  1],
    "↘": [ 1, -1], "↳": [ 1, -1], "⇘": [ 1, -1],
    "→": [ 1,  0], "⇒": [ 1,  0], "⇨": [ 1,  0],
    "↗": [ 1,  1], "↱": [ 1,  1], "⇗": [ 1,  1]
}
```

### [intersection](./code-golf/intersection)

A box is defined via x, y, w and h as
```
  y
  │ ┌───w───┐
  │ │   ┌───┼──┐
  │ h   │▓▓▓│  │
  │ │   │▓▓▓│  │
  │ o───┼───┘  │
  │     o──────┘
  └───────────────x
(0,0)
```
Compute the intersection area between two boxes given as

x1 y1 w1 h1 x2 y2 w2 h2

### [pangram](./code-golf/pangram)

A pangram is a sentence that uses every letter of a given alphabet.

Write a program that will receive various sentences as arguments and print those that are valid pangrams, meaning they use all letters from A to Z, case insensitive.

### [divisors](./code-golf/divisors)

A number is a divisor of another number if it can divide into it with no remainder.

Print the positive divisors of each number from 1 to 100 inclusive, on their own line, with each divisor separated by a space.

### [seven-segment](./code-golf/seven-segment)

Using pipes and underscores print the argument as if it were displayed on a seven segment display.

For example the number 0123456789 should be displayed as:

```
 _     _  _     _  _  _  _  _
| |  | _| _||_||_ |_   ||_||_|
|_|  ||_  _|  | _||_|  ||_| _|
```

### [isbn](./code-golf/isbn)

Calculate the check digit for these incomplete ISBNs. If the check digit would be 10, write "X" instead.

### [leap years](./code-golf/leap-years)

In the Gregorian calendar, a leap year is created by extending February to 29 days in order to keep the calendar year synchronized with the astronomical year. These longer years occur in years which are multiples of 4, with the exception of centennial years that aren’t multiples of 400.

### [morse-decoder](./code-golf/morse-decoder)

Using ▄ (U+2584 Lower Half Block) to represent a dot, decode the argument from International Morse Code to alphanumeric.

- The length of a dot is one unit.
- A dash is three units.
- The space between parts of the same letter is one unit.
- The space between letters is three units.
- The space between words is ten units.

### [morse-encoder](./code-golf/morse-encoder)

Using ▄ (U+2584 Lower Half Block) to represent a dot, encode the argument from alphanumeric into International Morse Code.

- The length of a dot is one unit.
- A dash is three units.
- The space between parts of the same letter is one unit.
- The space between letters is three units.
- The space between words is ten units.

### [99-bottles-again](./code-golf/99-bottles-again)

Print the lyrics to the song 99 Bottles of Beer

Solo attempt after some time following [previous solution with ChatGPT assistance](./code-golf/99-bottle-of-beer)

### [number-spiral](,.code-golf/number-spiral)

Print a 10×10 grid of the numbers 0 to 99 inclusive. Starting at the top left the numbers should spiral clockwise towards the centre, be right aligned, and have a space between each number.

The full grid should look like this:
```
 0  1  2  3  4  5  6  7  8  9
35 36 37 38 39 40 41 42 43 10
34 63 64 65 66 67 68 69 44 11
33 62 83 84 85 86 87 70 45 12
32 61 82 95 96 97 88 71 46 13
31 60 81 94 99 98 89 72 47 14
30 59 80 93 92 91 90 73 48 15
29 58 79 78 77 76 75 74 49 16
28 57 56 55 54 53 52 51 50 17
27 26 25 24 23 22 21 20 19 18
```

### [ordinal-numbers](./code-golf/ordinal-numbers)
For each integer argument, print the argument and its ordinal suffix (e.g. 1st, 2nd, 3rd, 112th).

The integers will be in the range of 0 to 999 inclusive.

### [maze](./code-golf/maze)

For a given maze, find the shortest path from Start to End points. Output the path in the maze with dots.

#### Example
Input:
```
###########
#S#      E#
# ### #####
#   #     #
### ##### #
#         #
###########
```

Output:
```
###########
#S#  ....E#
#.###.#####
#...#.....#
###.#####.#
#  .......#
###########
```

Here, `S` is the start point, `E` is the end point, `#` represents walls, and spaces represent open paths. The output should show the shortest path from `S` to `E` using dots (`.`).


### [zodic-signs](./code-golf/zodic-signs)

Given a MM-DD HH:MM date and time, output the corresponding Zodiac sign symbol according to the first table below. If the ascending sign is different from the Zodiac sign (sun sign), output it as well. Approximate the ascending sign using the sun sign and time according to the second table below.

### [Rock-paper-scissors-Spock-lizard](./code-golf/rock-paper-scissors-spock-lizard)

**Details**:

| Emoji 1 | Action    | Emoji 2 |
| ------- | --------- | ------- |
| ✂       | cuts      | 📄       |
| 💎       | crushes   | 🦎       |
| 🖖       | smashes   | ✂       |
| 🦎       | eats      | 📄       |
| 🖖       | vaporizes | 💎       |
| ✂       | ties with | ✂       |

Each argument is a string of two emoji encoded in UTF-8. For each argument, print a line like `🦎 poisons 🖖` describing the game outcome, or `Tie` if they are equal.

| Weapon   | Emoji | Codepoint                                                                                | UTF-8 Sequence |
| -------- | ----- | ---------------------------------------------------------------------------------------- | -------------- |
| Rock     | 💎     | [U+1F48E](https://emojipedia.org/gem-stone/)                                             | `f0 9f 92 8e`  |
| Paper    | 📄     | [U+1F4C4](https://emojipedia.org/page-facing-up/)                                        | `f0 9f 93 84`  |
| Scissors | ✂     | [U+2702](https://emojipedia.org/black-scissors/)                                         | `e2 9c 82`     |
| Spock    | 🖖     | [U+1F596](https://emojipedia.org/raised-hand-with-part-between-middle-and-ring-fingers/) | `f0 9f 96 96`  |
| Lizard   | 🦎     | [U+1F98E](https://emojipedia.org/lizard/)                                                | `f0 9f a6 8e`  |

## Hacker Rank

### [Project Euler #1: Multiples of 3 and 5](./hackerrank/projecteuler)

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below \( N \).

### 30 Days of Code

An attempt to ensure a comprehensive covering of the basics which might otherwise be missed with simple exercises, e.g. classes.These have all been attempted without the use of ChatGPT except where noted, e.g. to demonstrate an alternative to a working solution.

#### [dataypes](./hackerrank/30-days-of-code/datypes)

Declare  variables: one of type int, one of type double, and one of type String.
Read  lines of input from stdin (according to the sequence given in the Input Format section below) and initialize your  variables.
Use the  operator to perform the following operations:
Print the sum of  plus your int variable on a new line.
Print the sum of  plus your double variable to a scale of one decimal place on a new line.
Concatenate  with the string you read as input and print the result on a new line.

#### [Operators](./hackerrank/30-days-of-code/operators)

Given the meal price (base cost of a meal), tip percent (the percentage of the meal price being added as tip), and tax percent (the percentage of the meal price being added as tax) for a meal, find and print the meal's total cost. Round the result to the nearest integer.

#### [Intro-to-Conditional-Statements](./hackerrank/30-days-of-code/Intro-to-Conditional-Statements)

Given an integer \( n \), perform the following conditional actions:

- If \( n \) is odd, print `Weird`
- If \( n \) is even and in the inclusive range of 2 to 5, print `Not Weird`
- If \( n \) is even and in the inclusive range of 6 to 20, print `Weird`
- If \( n \) is even and greater than 20, print `Not Weird`
- 
#### [loops](./hackerrank/30-days-of-code/loops)

Given an integer \( n \), print its first 10 multiples. Each multiple \( (i) \) should be printed on a new line in the form: `n x i = result`.

#### [class-vs-instance](./hackerrank/30-days-of-code/class-vs-instance)

Write a `Person` class with an instance variable `age`, and a constructor that takes an integer `initialAge` as a parameter. The constructor must assign `initialAge` to `age` after confirming the argument passed as `initialAge` is not negative; if a negative argument is passed as `initialAge`, the constructor should set `age` to 0 and print "Age is not valid, setting age to 0.". In addition, you must write the following instance methods:

1. `yearPasses()` should increase the `age` instance variable by 1.
2. `amIOld()` should perform the following conditional actions:
    - If `age < 13`, print "You are young."
    - If `age >= 13` and `age < 18`, print "You are a teenager."
    - Otherwise, print "You are old."

#### [Let's Review](./hackerrank/30-days-of-code/lets_review)

Given a string, S, of length N that is indexed from 0 to N-1, print its even-indexed and odd-indexed characters as  space-separated strings on a single line.

Note: 0 is considered to be an even index.

#### [arrays](./hackerrank/30-days-of-code/arrays)

Given an array, `A`, of integers, print `A`'s elements in reverse order as a single line of space-separated numbers.

#### [dictionaries_and_maps](./hackerrank/30-days-of-code/dictionaries_and_maps)

Given names and phone numbers, assemble a phone book that maps friends' names to their respective phone numbers. You will then be given an unknown number of names to query your phone book for. For each queried, print the associated entry from your phone book on a new line in the form name=phoneNumber; if an entry for is not found, print Not found instead.

Note: Your phone book should be a Dictionary/Map/HashMap data structure.

## Misc

### [custom_zip](./misc/custom_zip)

The built-in zip function "zips" two lists. Write your own implementation of this function.

Define a function named zap. The function takes two parameters, a and b. These are lists.

Your function should return a list of tuples. Each tuple should contain one item from the a list and one from b.

You may assume a and b have equal lengths.

### [list_xor](./misc/list_xor)

Define a function named list_xor. Your function should take three parameters: `n`, `list1` and `list2`.

Your function must return whether n is exclusively in `list1` or `list2`.

In other words, if `n` is in both lists or in none of the lists, return `False`. If `n` is in only one of the lists, return `True`.


### [Counting syllables](./misc/counting-syllables)

Define a function named count that takes a single parameter. The parameter is a string. The string will contain a single word divided into syllables by hyphens, such as these:

`"ho-tel"`
`"cat"`
`"met-a-phor"`
`"ter-min-a-tor"`

Your function should count the number of syllables and return it.

For example, the call `count("ho-tel"` should return `2`.

### [counting-parameters](./misc/counting-parameters)

Define a function param_count that takes a variable number of parameters. The function should return the number of arguments it was called with.

For example, param_count() should return 0, while param_count(2, 3, 4) should return 3.
