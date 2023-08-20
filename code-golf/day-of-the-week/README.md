## Brief

https://code.golf/day-of-week#python

Given a date in the YYYY-MM-DD format between 1583-01-01 and 9999-12-31 inclusive, output the English name of the corresponding day of the week.

## date.py

Created manually with a small exception.

Here I ran into a number of 'obvious with hindsight' Python specific problems, e.g. using 'date' as the name for my python file and for a variable within it. I was able to resolve these via stackoverflow.com. Two cases where I referred to ChatGPT:

- Correction to cast output of stringsplit to ints (obvious with hindsight)
- Correction to reference `our_day` as an index in an array using `[]`(again, obvious with hindsight)