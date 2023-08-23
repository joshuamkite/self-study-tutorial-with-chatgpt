https://code.golf/isbn#python

## Brief

Calculate the check digit for these incomplete ISBNs. If the check digit would be 10, write "X" instead.

The second part of this brief on code.golf is essentially incorrect. I had to look [elsewhere for an explanation](https://www.codingame.com/training/easy/isbn-check-digit):

> International Standard Book Number (ISBN) is a unique numeric commercial book identifier.
> 
> Before year 2007 ISBNs were 10-digit long. After that year ISBNs extended to 13 digits. In both ISBN-10 and ISBN-13 standards, the last digit is the check digit, for error detection.
> 
> ISBN-10 check digit is calculated by Modulus 11 with decreasing weights on the first 9 digits.
> Example: 030640615?
> 0×10 + 3×9 + 0×8 + 6×7 + 4×6 + 0×5 + 6×4 + 1×3 + 5×2 = 130.
> 130 / 11 = 11 remainder 9.
> Check digit is the value needed to add to the sum to make it dividable by 11. In this case it is 2.
> So the valid ISBN is 0306406152.
> In case 10 being the value needed to add to the sum, we use X (upper case X) as the check digit instead of 10.
> 
> ISBN-13 check digit is calculated by Modulus 10 with alternate weights of 1 and 3 on the first 12 digits.
> Example: 978030640615?
> 9×1 + 7×3 + 8×1 + 0×3 + 3×1 + 0×3 + 6×1 + 4×3 + 0×1 + 6×3 + 1×1 + 5×3 = 93.
> 93 / 10 = 9 remainder 3.
> Check digit is the value needed to add to the sum to make it dividable by 10. So the check digit is 7. The valid ISBN is 9780306406157.

The code.golf input appears to be all 10 digit ISBNs

## main.py

I solved this myself without reference to ChatGPT, only 'traditional' generic online help resources

## main-improved.py 

I asked ChatGPT if we could make this more efficient.

> Here's what we've changed:

> We've removed the manual multiplication and addition for each digit. Instead, we use a list comprehension to iterate over the digits and calculate the total.
> We've used Python's f-string for formatting the output, which is more readable and concise.
> This version of the code is more concise and easier to read, and it should also be slightly faster due to the use of list comprehensions.

A block of largely repeated code with predictable iteration is an obvious candidate for improvement as pointed out. I could have bothered to attempt something like this myself.