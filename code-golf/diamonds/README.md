https://code.golf/diamonds#python

# Brief

Draw a size ascending range of diamonds using the numbers 1 to 9, ranging from size 1 to size 9, each diamond separated by a blank line.

A size 1 diamond should look like this, a single centered 1:

         1
With the largest size 9 diamond looking like this:

         1
        121
       12321
      1234321
     123454321
    12345654321
   1234567654321
  123456787654321
 12345678987654321
  123456787654321
   1234567654321
    12345654321
     123454321
      1234321
       12321
        121
         1

## diamonds.py

Initial passing version, sadly largely overtaken by ChatGPT jumping the gun

## diamonds-improved.py
 
ChatGPT asked to improve initial version:

> 1. Combine the two inner loops: Both the upper and lower parts of the diamond have two inner loops that print numbers. These can be combined into a single loop by using a list comprehension and then joining the results.
> 
> 2. Use a function for repeated logic: The logic to calculate the leading spaces and print the numbers is repeated for both the upper and lower parts of the diamond. This can be encapsulated into a separate function.


