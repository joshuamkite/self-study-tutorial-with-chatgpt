### Day 18: Queues and Stacks

Welcome to Day 18! Today we're learning about Stacks and Queues. Check out the Tutorial tab for learning materials and an instructional video!

A palindrome is a word, phrase, number, or other sequence of characters which reads the same backwards and forwards. Can you determine if a given string, `s`, is a palindrome?

To solve this challenge, we must first take each character in `s`, enqueue it in a queue, and also push that same character onto a stack. Once that's done, we must dequeue the first character from the queue and pop the top character off the stack, then compare the two characters to see if they are the same; as long as the characters match, we continue dequeueing, popping, and comparing each character until our containers are empty (a non-match means `s` isn't a palindrome).

Write the following declarations and implementations:

1. Two instance variables: one for your `stack`, and one for your `queue`.
2. A `void pushCharacter(char ch)` method that pushes a character onto a stack.
3. A `void enqueueCharacter(char ch)` method that enqueues a character in the `queue` instance variable.
4. A `char popCharacter()` method that pops and returns the character at the top of the `stack` instance variable.
5. A `char dequeueCharacter()` method that dequeues and returns the first character in the `queue` instance variable.

#### Input Format

You do not need to read anything from stdin. The locked stub code in your editor reads a single line containing string `s`. It then calls the methods specified above to pass each character to your instance variables.

#### Constraints

- `s` is composed of lowercase English letters.

#### Output Format

You are not responsible for printing any output to stdout.

If your code is correctly written and `s` is a palindrome, the locked stub code will print:

```
The word, racecar, is a palindrome.
```

Otherwise, it will print:

```
The word, racecar, is not a palindrome.
```

#### Sample Input

```
racecar
```

#### Sample Output

```
The word, racecar, is a palindrome.
```

## Input of ChatGPT

I had had to breakaway after struggling with this when I was tired. I came back to this a couple of days later and was still stuck. Predictably my errors were largely syntactical. As ChatGPT advised, I needed to:

> Make sure to use self to access class attributes. This means prefixing myStack and myQueue with self. to make them instance variables.
> The methods pushCharacter, enqueueCharacter, popCharacter, and dequeueCharacter should also be instance methods, so they should have self as their first argument.

I also had not realised that:

> The pop method of a list doesn't require an argument to pop the last element. Similarly, to dequeue the first element, you can use pop(0) without specifying the element itself.

I also and perhaps most importantly, hadn't understood why I should 
> Remove the s argument from the __init__ method of the Solution class since it's not required.
I think this last is as much a challenge of the HackerRank challenges attempting to be language agnostic, and here based around Java for the tutorials. I had not understood about the class init function being needed to initialise the stack and queue without needing the variable
