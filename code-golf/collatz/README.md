https://code.golf/collatz#python

## Brief

The Collatz conjecture states that, for any positive integer n, it will eventually reach 1 by repeatedly applying the following procedure:

If n is even, divide it by 2.
If n is odd, multiply by 3 and then add 1.
The number of steps needed for n to reach 1 is called its stopping time. For example, the stopping time of 10 is six:

10 → 5 → 16 → 8 → 4 → 2 → 1

Print the stopping times of all the numbers from 1 to 1,000 inclusive, each on their own line.

## collatz.py

This is a debugged version of my original design approach using recursion and if/else. There were some errors cause by not passing the result of each recursive call was passed back up the chain correctly but initially ChatGPT recommended a wholly different approach based on the buggy code (see below) and I had to specifically go back and ask to fix within this design pattern

## collatz-improved.py

This is ChatGPT racing ahead. It's certainly better code as ChatGPT explains but it has gone straight to the solution using a totally different design pattern:

> [Me] Ok, this works well but why the change from if/else to a while loop?
> 
> [ChatGPT]
> The change from a recursive approach using if/else statements to a while loop was made to simplify the logic and make the code easier to follow. Let me explain the rationale behind this change:
> 
> **Simplicity and Readability:**
> 
> - A `while` loop makes it clear that we are repeatedly applying a process until a certain condition is met—in this case, until `n` becomes `1`. This is a straightforward way to express an iterative process, which is what the Collatz sequence is.
> - Recursive functions can be harder to understand and reason about, especially for those who are new to recursion. A loop-based approach is often more intuitive.
> 
> **Efficiency:**
> 
> - Each recursive call adds a new layer to the call stack, which consumes memory. For large inputs, this can lead to a stack overflow error.
> - A `while` loop doesn't have this issue, as it operates within a constant stack frame, making it more memory-efficient.
> 
> **Avoiding Stack Overflow Errors:**
> 
> - For large inputs, a recursive approach can lead to a stack overflow error due to the deep call stack.
> - The while loop avoids this problem entirely, as it doesn't use the call stack in the same way.
> 
> **Explicit Counter Variable:**
> 
> - In the loop-based approach, we have an explicit counter variable `i` that we increment at each step of the process. This makes it clear that we are counting the number of steps needed to reach `1`.
> - In the recursive approach, this counting was done by passing an additional argument i through the recursive calls, which can be a bit harder to follow.
> 
> **General Practice:**
> 
> - For problems that involve simple repetition until a condition is met, loops are often the more conventional choice. Recursion is typically used for problems that have a naturally recursive structure, like tree traversals or divide-and-conquer algorithms.
>   
> That being said, the recursive approach is not wrong; it's just a different way to solve the problem. Both approaches have their use cases, and the choice between them can depend on various factors, including readability, efficiency, and personal or team coding style preferences.