
## Brief

https://code.golf/cubes#python

Draw 7 cubes in increasing size using "╱" (U+2571) for the diagonal edges, "│" (U+2502) for the vertical edges, "─" (U+2500) for the horizontal edges, and "█" (U+c) for the vertices. The cubes should range from size 1 to size 7 with a blank line between each cube. A size 1 cube should look like:
```
  █────█
 ╱    ╱│
█────█ │
│    │ █
│    │╱
█────█
```

And a size 7 cube should look like:
```

        █────────────────────────────█
       ╱                            ╱│
      ╱                            ╱ │
     ╱                            ╱  │
    ╱                            ╱   │
   ╱                            ╱    │
  ╱                            ╱     │
 ╱                            ╱      │
█────────────────────────────█       │
│                            │       │
│                            │       │
│                            │       │
│                            │       │
│                            │       │
│                            │       │
│                            │       █
│                            │      ╱
│                            │     ╱
│                            │    ╱
│                            │   ╱
│                            │  ╱
│                            │ ╱
│                            │╱
█────────────────────────────█
```

## cubes.py

This was arrived at entirely manually and without reference to ChatGPT or to previous code