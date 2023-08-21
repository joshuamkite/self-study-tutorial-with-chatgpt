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

  y
  │ ┌───w───┐
  │ │   ┌───┼──┐
  │ h   │▓▓▓│  │
  │ │   │▓▓▓│  │
  │ o───┼───┘  │
  │     o──────┘
  └───────────────x
(0,0)
Compute the intersection area between two boxes given as

x1 y1 w1 h1 x2 y2 w2 h2