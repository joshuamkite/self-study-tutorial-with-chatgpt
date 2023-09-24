# Alphabet Rangoli

You are given an integer, `n`. Your task is to print an alphabet rangoli of size `n`. (Rangoli is a form of Indian folk art based on creation of patterns.)

Different sizes of alphabet rangoli are shown below:

## size 3
```
----c----
--c-b-c--
c-b-a-b-c
--c-b-c--
----c----
```

## size 5
```
--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------
```

## size 10
```
------------------j------------------
----------------j-i-j----------------
--------------j-i-h-i-j--------------
------------j-i-h-g-h-i-j------------
----------j-i-h-g-f-g-h-i-j----------
--------j-i-h-g-f-e-f-g-h-i-j--------
------j-i-h-g-f-e-d-e-f-g-h-i-j------
----j-i-h-g-f-e-d-c-d-e-f-g-h-i-j----
--j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j--
j-i-h-g-f-e-d-c-b-a-b-c-d-e-f-g-h-i-j
--j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j--
----j-i-h-g-f-e-d-c-d-e-f-g-h-i-j----
------j-i-h-g-f-e-d-e-f-g-h-i-j------
--------j-i-h-g-f-e-f-g-h-i-j--------
----------j-i-h-g-f-g-h-i-j----------
------------j-i-h-g-h-i-j------------
--------------j-i-h-i-j--------------
----------------j-i-j----------------
------------------j------------------
```

The center of the rangoli has the first alphabet letter `a`, and the boundary has the `n`th alphabet letter (in alphabetical order).

## Function Description

Complete the `rangoli` function in the editor below.

`rangoli` has the following parameters:
- `int size`: the size of the rangoli

### Returns
- `string`: a single string made up of each of the lines of the rangoli separated by a newline character (`\n`)

### Input Format
Only one line of input containing `n`, the size of the rangoli.

### Constraints
*The document does not specify the constraints.*

### Sample Input
```
5
```

### Sample Output
```
--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------
```

## Input from ChatGPT

None for my initial working version but ChatGPT proposed a far more concise version - `main-improved.py`:

> Improvements Made:
> Code Conciseness: The code is made more concise by directly creating the strings for each line in the rangoli within the loop and appending them to a list.
> 
> List Slicing: Used list slicing to create the strings for each line in the rangoli, which reduces the need for additional variables and makes the code more readable.
> 
> Single Print Statement: Instead of printing each line in the loop, the code creates a list of all the lines and then prints the entire rangoli with a single print statement. This is done by concatenating the reversed top half of the rangoli with the bottom half.
> 
> Removed Redundant Comments: Removed comments that were explaining straightforward code, making the code cleaner. Comments are essential for explaining complex logic, but they can be omitted for self-explanatory code.
> 
> This improved version should produce the same output as your original solution but is more concise and readable.