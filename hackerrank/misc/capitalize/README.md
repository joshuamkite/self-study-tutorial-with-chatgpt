# [Capitalize!](https://www.hackerrank.com/challenges/capitalize/problem)

You are asked to ensure that the first and last names of people begin with a capital letter in their passports. For example, `alison heck` should be capitalized correctly as `Alison Heck`.

Given a full name, your task is to capitalize the name appropriately.

## Input Format

A single line of input containing the full name, `s`.

### Constraints

- The string consists of alphanumeric characters and spaces.
- Note: in a word only the first character is capitalized. Example `12abc` when capitalized remains `12abc`.

## Output Format

Print the capitalized string, `s`.

## Sample Input

```
chris alan
```

## Sample Output

```
Chris Alan
```

### INput from ChatGPT

Essentially total - I was trying to do a complex `.upper()` partial string swap in a line comprehension with broken syntax. ChatGPT used `.capitalize()` and then handled the variable length whitespace extended test case.