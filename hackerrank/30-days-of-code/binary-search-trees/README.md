### Day 22: Binary Search Trees

#### Objective
Today, we're working with Binary Search Trees (BSTs). Check out the Tutorial tab for learning materials and an instructional video!

#### Task
The height of a binary search tree is the number of edges between the tree's root and its furthest leaf. You are given a pointer, pointing to the root of a binary search tree. Complete the `getHeight` function provided in your editor so that it returns the height of the binary search tree.

#### Input Format
The locked stub code in your editor reads the following inputs and assembles them into a binary search tree:
- The first line contains an integer, \( T \), denoting the number of nodes in the tree.
- Each of the subsequent lines contains an integer, \( data \), denoting the value of an element that must be added to the BST.

#### Output Format
The locked stub code in your editor will print the integer returned by your `getHeight` function denoting the height of the BST.

#### Sample Input
```
7
3
5
2
1
4
6
7
```

#### Sample Output
```
3
```

#### Explanation
The input forms the following BST:
```
    3
   / \
  2   5
 /   / \
1   4   6
         \
          7
```
The longest root-to-leaf path is shown below:
```
3 -> 5 -> 6 -> 7
```
There are 4 nodes in this path that are connected by 3 edges, meaning our BST's height is 3. Thus, we print 3 as our answer.

## Input of ChatGPT

This was in 3 stages:

1. Explain the properties and terminology of a binary tree since I was not very familiar with it.
2. Explain where I had gone wrong in lifting [code found online](https://www.pythonforbeginners.com/data-structures/find-the-height-of-a-binary-tree). Whilst I had renamed the method calls correctly I had neglected the `self.` prefix for recursive function calls
3. Correct the code sample from above (previously returned `0` if `none`):
   > Note that I also made a small adjustment to return -1 when root is None. This is because the height of an empty tree is conventionally considered as -1, and the height of a tree with one node (the root) is 0. This way, the height of the tree is calculated correctly as the number of edges on the longest path from the root to a leaf.
