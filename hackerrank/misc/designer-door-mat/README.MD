### Designer Door Mat

Mr. Vincent works in a door mat manufacturing company. One day, he designed a new door mat with the following specifications:

- Mat size must be \(N \times M\). (\(N\) is an odd natural number, and \(M\) is \(3\) times \(N\).)
- The design should have 'WELCOME' written in the center.
- The design pattern should only use `|`, `.` and `-` characters.

#### Sample Designs

**Size: 7 x 21**
```
---------.|.---------
------.|..|..|.------
---.|..|..|..|..|.---
-------WELCOME-------
---.|..|..|..|..|.---
------.|..|..|.------
---------.|.---------
```

**Size: 11 x 33**
```
---------------.|.---------------
------------.|..|..|.------------
---------.|..|..|..|..|.---------
------.|..|..|..|..|..|..|.------
---.|..|..|..|..|..|..|..|..|.---
-------------WELCOME-------------
---.|..|..|..|..|..|..|..|..|.---
------.|..|..|..|..|..|..|.------
---------.|..|..|..|..|.---------
------------.|..|..|.------------
---------------.|.---------------
```

#### Input Format

A single line containing the space-separated values of \(N\) and \(M\).

#### Constraints

- \(5 \leq N \leq 101\)
- \(15 \leq M \leq 303\)

#### Output Format

Output the design pattern.

#### Sample Input
```
9 27
```

#### Sample Output
```
------------.|.------------
---------.|..|..|.---------
------.|..|..|..|..|.------
---.|..|..|..|..|..|..|.---
----------WELCOME----------
---.|..|..|..|..|..|..|.---
------.|..|..|..|..|.------
---------.|..|..|.---------
------------.|.------------
```

## Input from ChatGPT

I had been having a tough time with this challenge before breaking off for the day. When I returned to it later I realised that my initial plan was going to be difficult to get working and moved to a structure based on the [Diamonds](code-golf/diamonds) challenge- with different sections. I got as far as the first, middle, and last lines together with the section between the first and middle lines but was struggling with the maths to generate the correct patterns and gave in to ChatGPT. 

ChatGPT suggested the code in `main-improved.py` which makes use of the `center()` method. I had not thought to use this, although I have encountered other challenges using it, and of course it is a much better pattern. Nonetheless I also had ChatGPT complete a solution according to my original pattern.