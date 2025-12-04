# 36. Valid Sudoku

**Difficulty:** Medium  
**LeetCode Link:** [36. Valid Sudoku](https://leetcode.com/problems/valid-sudoku/)

---

## Description

Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

- Each row must contain the digits 1-9 without repetition.
- Each column must contain the digits 1-9 without repetition.
- Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

**Note:**

- A Sudoku board (partially filled) could be valid but is not necessarily solvable.
- Only the filled cells need to be validated according to the mentioned rules.

---

## Examples

### Example 1

**Input:**
```
board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
```

**Output:**
```
true
```

### Example 2

**Input:**
```
board = 
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
```

**Output:**
```
false
```

**Explanation:**
Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.

---

## Constraints

<!-- Add constraints if available -->

---

## Approach

We need to check three things for each cell:
1. **Row**: No duplicate digits in the same row
2. **Column**: No duplicate digits in the same column
3. **3x3 Square**: No duplicate digits in the same 3x3 sub-box

We use sets to track seen digits for each row, column, and square. For each cell, we check if the value already exists in any of the three sets. If it does, the board is invalid.

The key challenge is mapping a cell's (row, col) coordinates to the correct 3x3 square index.

---

## Solution Code

```python
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # determine if 9x sudoku board is valid 

        # we have to check row, col, square 
        # check if we have the value in the set already .

        row_sets = {row: set() for row in range(9)}
        col_sets = {col: set() for col in range(9)}
        square_sets = {sq: set() for sq in range(9)}

        ROW = 9
        COL = 9
        WIDTH = 3

        for row in range(ROW):
            for col in range(COL):
                curr_val = board[row][col]
                if curr_val == ".":
                    continue 
                square = row // 3 * WIDTH + col // 3
                if curr_val in row_sets[row] or curr_val in col_sets[col] or curr_val in square_sets[square]:
                    return False 
                row_sets[row].add(curr_val)
                col_sets[col].add(curr_val)
                square_sets[square].add(curr_val)
        return True
```

---

## Time & Space Complexity

- **Time Complexity:** O(1) - We iterate through a fixed 9x9 grid, so constant time
- **Space Complexity:** O(1) - We use fixed-size sets (9 rows, 9 cols, 9 squares), so constant space

---

## Notes

### How does the mapping of the square work?

The formula `square = row // 3 * WIDTH + col // 3` maps a cell's (row, col) coordinates to a square index (0-8).

**Step 1: Determine row block**
```python
row_block = r // 3  # which row block? (0, 1, or 2)
```

**Examples:**
- `r=0` → `0 // 3 = 0` (top row block)
- `r=4` → `4 // 3 = 1` (middle row block)
- `r=8` → `8 // 3 = 2` (bottom row block)

**Step 2: Determine col block**
```python
col_block = c // 3  # which col block? (0, 1, or 2)
```

**Step 3: Combine into a single index**

Think of the squares laid out in **reading order** (left-to-right, top-to-bottom):

```
┌─────┬─────┬─────┐
│  0  │  1  │  2  │  ← row_block = 0
├─────┼─────┼─────┤
│  3  │  4  │  5  │  ← row_block = 1
├─────┼─────┼─────┤
│  6  │  7  │  8  │  ← row_block = 2
└─────┴─────┴─────┘
  ↑     ↑     ↑
col_block: 0  1  2
```

The formula `row_block * 3 + col_block` gives us the square index:
- Top-left square (row_block=0, col_block=0): `0 * 3 + 0 = 0`
- Top-middle square (row_block=0, col_block=1): `0 * 3 + 1 = 1`
- Center square (row_block=1, col_block=1): `1 * 3 + 1 = 4`
- Bottom-right square (row_block=2, col_block=2): `2 * 3 + 2 = 8`

---

## Alternative Solutions

<!-- Add alternative solutions if applicable -->

---

## Related Problems

<!-- Link to related problems if applicable -->

