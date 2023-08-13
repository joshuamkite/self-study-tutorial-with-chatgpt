# Brief

[Source](https://code.golf/roman-to-arabic#python)

For each numeric argument in Roman numerals, print the same number in Arabic numerals.

The numbers range from 1 to 3999 inclusive.

Arabic	1	5	10	50	100	500	1000
Roman	Ⅰ	Ⅴ	Ⅹ	Ⅼ	Ⅽ	Ⅾ	Ⅿ


## number.py 

This is an interactive version whilst working on the code golf challenge offline

## list-number.py          

This is an initial version for code golf that passes. Whilst created with assistance from ChatGPT it is very suboptimal. The implementation was misdirected in part because of an initial personal choice of approach.

## list-improved.py        

This is after asking ChatGPT 4 to improve `list-number.py` in a new session. From ChatGPT:

The provided code is a Python program to convert Roman numerals to Arabic numerals. The code uses a unique approach to handle the special cases in Roman numerals like "IV", "IX", etc., by replacing them with tokens and then converting them back.

> Here are some improvements we can make:
> 
> Simplify the spv function: Instead of using a token-based approach, we can directly iterate through the string and handle special cases.
> Use list comprehension: This can make the code more concise.
> Use a main function: This makes the code more organized and easier to understand.
> 
> Changes made:
> 
> 1. The roman_to_arabic function directly checks for two-character Roman numerals and adds their value, otherwise, it adds the value of the single character.
> 1. Removed the spv function as it's no longer needed.
> 1. Added a main function for better organization.

Clearly the improved version is much better than the initial version. It is much easier to readily understand what is going on and the list comprehension obviates the need for additional variables and processes by checking directly. Seems obvious when you see it but that's the benefit of hindsight!

## number-improved.py

This is a retrofitted version of the ChatGPT improvements above, including the `upper()` method to permit lower case input