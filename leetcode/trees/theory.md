# Binary Tree Traversal Theory

In a binary tree, there are three primary ways to traverse (visit) all the nodes: **inorder**, **preorder**, and **postorder**. These are all types of depth-first traversal.

## Example Tree

```
      A
     / \
    B   C
   / \
  D   E
```

## Traversal Types

### 1. Inorder Traversal (Left → Root → Right)
- Visit the left subtree
- Visit the root
- Visit the right subtree

**Result:** `D B E A C`

> Commonly used in binary search trees to get values in sorted order.

### 2. Preorder Traversal (Root → Left → Right)
- Visit the root
- Visit the left subtree
- Visit the right subtree

**Result:** `A B D E C`

**Used for:**
- Copying a tree
- Generating prefix expressions

### 3. Postorder Traversal (Left → Right → Root)
- Visit the left subtree
- Visit the right subtree
- Visit the root

**Result:** `D E B C A`

**Used for:**
- Deleting a tree
- Evaluating postfix expressions

## 🧠 Summary Table

| Traversal  | Order                | Use Case                        |
|-----------|----------------------|---------------------------------|
| Inorder   | Left → Root → Right  | Sorted output in BSTs           |
| Preorder  | Root → Left → Right  | Tree copying, prefix notation   |
| Postorder | Left → Right → Root  | Tree deletion, postfix notation |