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
      - [datatypes](#datatypes)
      - [Operators](#operators)
      - [Intro-to-Conditional-Statements](#intro-to-conditional-statements)
      - [loops](#loops)
      - [class-vs-instance](#class-vs-instance)
      - [Let's Review](#lets-review)
      - [arrays](#arrays)
      - [dictionaries\_and\_maps](#dictionaries_and_maps)
      - [recursion](#recursion)
      - [binary-numbers](#binary-numbers)
      - [2D Arrays](#2d-arrays)
      - [Inheritance](#inheritance)
      - [Abstract Classes](#abstract-classes)
      - [scope](#scope)
      - [linked-list](#linked-list)
      - [exceptions-string-to-integer](#exceptions-string-to-integer)
      - [queues-and-stacks](#queues-and-stacks)
      - [interfaces](#interfaces)
      - [binary-search-trees](#binary-search-trees)
    - [Hacker Rank Misc](#hacker-rank-misc)
      - [lists](#lists)
      - [list-comprehensions](#list-comprehensions)
      - [find-second-maximum-number-in-a-list](#find-second-maximum-number-in-a-list)
      - [Nested Lists](#nested-lists)
      - [more-exceptions](#more-exceptions)
      - [string-validators](#string-validators)
    - [bubble-sort](#bubble-sort)
  - [Misc](#misc)
    - [custom\_zip](#custom_zip)
    - [list\_xor](#list_xor)
    - [Counting syllables](#counting-syllables)
    - [counting-parameters](#counting-parameters)
    - [finding-the-percentage](#finding-the-percentage)
    - [swap-case](#swap-case)
    - [designer-door-mat](#designer-door-mat)
    - [string-formatting](#string-formatting)
    - [alphabet-rangoli](#alphabet-rangoli)
    - [Capitalize!](#capitalize)
 
 
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

#### [datatypes](./hackerrank/30-days-of-code/datatypes)

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

#### [recursion](./hackerrank/30-days-of-code/recursion)

Recursive Method for Calculating Factorial

#### [binary-numbers](./hackerrank/30-days-of-code/binary-numbers)

Given a base-10 integer, \( n \), convert it to binary (base-2). Then find and print the base-10 integer denoting the maximum number of consecutive 1's in \( n \)'s binary representation. When working with different bases, it is common to show the base as a subscript.

#### [2D Arrays](./hackerrank/30-days-of-code/2d-arrays)

Given a 2D Array, `A`:

```
1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
```

We define an hourglass in `A` to be a subset of values with indices falling in this pattern in `A`'s graphical representation:

```
a b c
  d
e f g
```

There are 16 hourglasses in `A`, and an hourglass sum is the sum of an hourglass' values.

**Task**

Calculate the hourglass sum for every hourglass in `A`, then print the maximum hourglass sum.

#### [Inheritance](./hackerrank/30-days-of-code/Inheritance)

You are given two classes, **Person** and **Student**, where **Person** is the base class and **Student** is the derived class. Completed code for **Person** and a declaration for **Student** are provided for you in the editor.

Observe that **Student** inherits all the properties of **Person**.

Complete the **Student** class by writing the following:

- A **Student** class constructor, which has 4 parameters:
  1. A string, *firstName*
  2. A string, *lastName*
  3. An integer, *idNumber*
  4. An integer array (or vector) of test scores, *scores*

- A char `calculate()` method that calculates a **Student** object's average and returns the grade character representative of their calculated average.

#### [Abstract Classes](./hackerrank/30-days-of-code/absrtract-classes)

Given a `Book` class and a `Solution` class, write a `MyBook` class that does the following:

- Inherits from `Book`
- Has a parameterized constructor taking these 3 parameters:
  1. string (title)
  2. string (author)
  3. int (price)
  
- Implements the `Book` class' abstract `display()` method so it prints these 3 lines:
  1. `Title:`, a space, and then the current instance's title.
  2. `Author:`, a space, and then the current instance's author.
  3. `Price:`, a space, and then the current instance's price.

#### [scope](./hackerrank/30-days-of-code/scope)

The absolute difference between two integers, \(a\) and \(b\), is written as \(|a - b|\). The maximum absolute difference between two integers in a set of positive integers, \(elements\), is the largest absolute difference between any two integers in \(elements\).

The `Difference` class is started for you in the editor. It has a private integer array (`elements`) for storing non-negative integers, and a public integer (`maximumDifference`) for storing the maximum absolute difference.

**Task**

Complete the `Difference` class by writing the following:

- A class constructor that takes an array of integers as a parameter and saves it to the `elements` instance variable.
- A `computeDifference` method that finds the maximum absolute difference between any two numbers in `elements` and stores it in the `maximumDifference` instance variable.

#### [linked-list](./hackerrank/30-days-of-code/linked-list)

A Node class is provided for you in the editor. A Node object has an integer data field, and a Node instance pointer, pointing to another node (i.e.: the next node in the list).

A Node insert function is also declared in your editor. It has two parameters: a pointer, pointing to the first node of a linked list, and an integer, that must be added to the end of the list as a new Node object.

**Task**

Complete the insert function in your editor so that it creates a new Node (pass constructor argument) and inserts it at the tail of the linked list referenced by the as the Node parameter. Once the new node is added, return the reference to the node.

#### [exceptions-string-to-integer](./hackerrank/30-days-of-code/exceptions-string-to-integer)

Read a string, `S`, and print its integer value; if `S` cannot be converted to an integer, print `Bad String`.

**Note:** You must use the String-to-Integer and exception handling constructs built into your submission language. If you attempt to use loops/conditional statements, you will get a 0 score.

####  [queues-and-stacks](./hackerrank/30-days-of-code/queues-and-stacks)

Welcome to Day 18! Today we're learning about Stacks and Queues. Check out the Tutorial tab for learning materials and an instructional video!

A palindrome is a word, phrase, number, or other sequence of characters which reads the same backwards and forwards. Can you determine if a given string, `s`, is a palindrome?

#### [interfaces](./hackerrank/30-days-of-code/interfaces)

The `AdvancedArithmetic` interface and the method declaration for the abstract `divisorSum(n)` method are provided for you in the editor below.

Complete the implementation of `Calculator` class, which implements the `AdvancedArithmetic` interface. The implementation for the `divisorSum(n)` method must return the sum of all divisors of `n`.

#### [binary-search-trees](./hackerrank/30-days-of-code/binary-search-trees)

The height of a binary search tree is the number of edges between the tree's root and its furthest leaf. You are given a pointer, pointing to the root of a binary search tree. Complete the `getHeight` function provided in your editor so that it returns the height of the binary search tree.

### Hacker Rank Misc

#### [lists](./hackerrank/misc/lists)

Consider a list (`list = []`). You can perform the following commands:

1. `insert i e`: Insert integer `e` at position `i`.
2. `print`: Print the list.
3. `remove e`: Delete the first occurrence of integer `e`.
4. `append e`: Insert integer `e` at the end of the list.
5. `sort`: Sort the list.
6. `pop`: Pop the last element from the list.
7. `reverse`: Reverse the list.

Initialize your list and read in the value of `n` followed by `n` lines of commands where each command will be of the types listed above. Iterate through each command in order and perform the corresponding operation on your list.

#### [list-comprehensions](./hackerrank/misc/list-comprehensions)

You are given three integers `x`, `y`, and `z` representing the dimensions of a cuboid along with an integer `n`. You need to print a list of all possible coordinates given by `(i, j, k)` on a 3D grid where the sum of `i + j + k` is not equal to `n`. Here, `0 <= i <= x`, `0 <= j <= y`, and `0 <= k <= z`. Please use list comprehensions rather than multiple loops, as a learning exercise.

#### [find-second-maximum-number-in-a-list](./hackerrank/misc/find-second-maximum-number-in-a-list)

Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given `n` scores. Store them in a list and find the score of the runner-up.


#### [Nested Lists](./hackerrank/misc/nested-lists)

Given the names and grades for each student in a class of students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

**Note:** If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.

[Tuples](./hackerrank/misc/tuples)

Given an integer, `n`, and `n` space-separated integers as input, create a tuple, `t`, of those `n` integers. Then compute and print the result of `hash(t)`.

#### [more-exceptions](./hackerrank/30-days-of-code/more-exceptions)

Write a Calculator class with a single method: `int power(int,int)`. The power method takes two integers, `n` and `p`, as parameters and returns the integer result of `n^p`. If either `n` or `p` is negative, then the method must throw an exception with the message: "n and p should be non-negative".

#### [string-validators](./hackerrank/misc/string-validators)

You are given a string `S`.  
Your task is to find out if the string `S` contains: alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters.

### [bubble-sort](./hackerrank/30-days-of-code/bubble-sort)

Given an array, `a`, of size distinct elements, sort the array in ascending order using the Bubble Sort algorithm above. Once sorted, print the following lines:
1. `Array is sorted in numSwaps swaps.`
   where `numSwaps` is the number of swaps that took place.
2. `First Element: firstElement`
   where `firstElement` is the first element in the sorted array.
3. `Last Element: lastElement`
   where `lastElement` is the last element in the sorted array.

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

### [finding-the-percentage](./hackerrank/misc/finding-the-percentage)

The provided code stub will read in a dictionary containing key/value pairs of `name:[marks]` for a list of students. Print the average of the marks array for the student name provided, showing 2 places after the decimal.

### [swap-case](./hackerrank/misc/swap-case)

You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.

**For Example:**
```
Www.HackerRank.com → wWW.hACKERrANK.COM
Pythonist 2 → pYTHONIST 2  
```

**Function Description**

Complete the `swap_case` function in the editor below.

`swap_case` has the following parameters:
- string s: the string to modify

**Returns**
- string: the modified string

**Input Format**

A single line containing a string.

### [designer-door-mat](./hackerrank/misc/designer-door-mat)

Mr. Vincent works in a door mat manufacturing company. One day, he designed a new door mat with the following specifications:

- Mat size must be \(N \times M\). (\(N\) is an odd natural number, and \(M\) is \(3\) times \(N\).)
- The design should have 'WELCOME' written in the center.
- The design pattern should only use `|`, `.` and `-` characters.

### [string-formatting](./hackerrank/misc/string-formatting)

Given an integer, `n`, print the following values for each integer from `1` to `n`:

1. Decimal
2. Octal
3. Hexadecimal (capitalized)
4. Binary

### [alphabet-rangoli](./hackerrank/misc/alphabet-rangoli)

You are given an integer, `n`. Your task is to print an alphabet rangoli of size `n`. (Rangoli is a form of Indian folk art based on creation of patterns.)

### [Capitalize!](./hackerrank/misc/capitalize)

You are asked to ensure that the first and last names of people begin with a capital letter in their passports. For example, `alison heck` should be capitalized correctly as `Alison Heck`.

Given a full name, your task is to capitalize the name appropriately.