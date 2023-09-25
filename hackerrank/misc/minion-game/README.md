### The Minion Game

Kevin and Stuart want to play the 'The Minion Game'.

#### Game Rules
- Both players are given the same string, `S`.
- Both players have to make substrings using the letters of the string `S`.
- Stuart has to make words starting with consonants.
- Kevin has to make words starting with vowels.
- The game ends when both players have made all possible substrings.

#### Scoring
- A player gets +1 point for each occurrence of the substring in the string `S`.

#### For Example:
- String `S` = BANANA
- Kevin's vowel beginning word = ANA
- Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points.

#### Your task is to determine the winner of the game and their score.

#### Function Description
Complete the `minion_game` in the editor below.

`minion_game` has the following parameters:
- `string string`: the string to analyze

#### Prints
- `string`: the winner's name and score, separated by a space on one line, or Draw if there is no winner

#### Input Format
- A single line of input containing the string `S`.
- Note: The string `S` will contain only uppercase letters.

#### Constraints
- The length of the input string is constrained to be non-empty and less than or equal to 10^6.

#### Sample Input
```
BANANA
```

#### Sample Output
```
Stuart 12
```

#### Note:
- Vowels are only defined as AEIOU. In this problem, Y is not considered a vowel.

## Input of ChatGPT

Here, pretty much all of it! As can be seen from `main-broken.py` I had distractedly made a number of errors and further misunderstood the original task. `main-chatgpt.py` is clearly better.

On reflection, the passing code does not really calculate substrings, rather it tallies vowels and consonants and their relative positions. I became interested in the statistical odds, which seemed to me greatly in favour of Stuart winning. On interrogating ChatGPT, it seemed there wasn't an 'obvious' or established and ready answer, rather this would need to be my own statistical analysis. I asked ChatGPT to extend the code to perform this analysis using the Python `english_words` package, and specifically the `web2` set of words:

> The 'web2' word list is one of the word lists that originated from the Unix operating system. It is a large list of English words that is often used in various software applications, including spell checkers and word games. The 'web2' list is derived from the "Webster's Second International" dictionary and contains a comprehensive collection of English words, including both common and uncommon words.

Running this code `main-statistical.py` on my Mac was surprisingly quick and the results are unambiguous:

Total Games: 234450
Stuart Wins: 206739 (88.18%)
Kevin Wins: 21991 (9.38%)
Draws: 5720 (2.44%)

Essentially Stuart wins 9 times out of 10 and Kevin only 1 time in 11


