https://code.golf/arrows#python

## Brief

Starting at [0, 0] print the cumulative result of applying each of the given Unicode arrow arguments. The arrows will be a random combination of these:

```json
{
    "↙": [-1, -1], "↲": [-1, -1], "⇙": [-1, -1],
    "←": [-1,  0], "⇐": [-1,  0], "⇦": [-1,  0],
    "↖": [-1,  1], "↰": [-1,  1], "⇖": [-1,  1],
    "↓": [ 0, -1], "⇓": [ 0, -1], "⇩": [ 0, -1],
    "↔": [ 0,  0], "↕": [ 0,  0], "⇔": [ 0,  0],
    "⇕": [ 0,  0], "⥀": [ 0,  0], "⥁": [ 0,  0],
    "↑": [ 0,  1], "⇑": [ 0,  1], "⇧": [ 0,  1],
    "↘": [ 1, -1], "↳": [ 1, -1], "⇘": [ 1, -1],
    "→": [ 1,  0], "⇒": [ 1,  0], "⇨": [ 1,  0],
    "↗": [ 1,  1], "↱": [ 1,  1], "⇗": [ 1,  1]
}
```

## main.py

I got 'almost there' but got stuck with:

- syntax for combining two vectors( I had been working from https://stackoverflow.com/a/846274)
- lack of familiarity with the unpacking operator in Python (`*`)
- And a classic working alone problem - wrong indent for my print line so that I was presenting the result of all arguments rather than for each argument. This was in part because I found the brief unclear and confusing. Here I was able to share the 'correct' output for a given input with ChatGPT and clarify this.