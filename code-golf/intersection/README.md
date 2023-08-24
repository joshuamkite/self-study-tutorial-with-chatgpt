https://code.golf/intersection#python

## brief

A box is defined via x, y, w and h as

```
  y
  │ ┌───w───┐
  │ │   ┌───┼──┐
  │ h   │▓▓▓│  │
  │ │   │▓▓▓│  │
  │ o───┼───┘  │
  │     o──────┘
  └───────────────x
(0,0)
```
Compute the intersection area between two boxes given as

x1 y1 w1 h1 x2 y2 w2 h2

## main.py

I found this one more challenging. I used ChatGPT early on for some minor syntax stuff such as citing args with "" in my IDE. I wound up basing my solution on the description from a comparable example, rather than the actual code there. For final polishing I had forgottten to include the `print(0)` for negative values and ChatGPT completely misunderstood the requirement.

## main-golfed.py

A golfed version of the above
