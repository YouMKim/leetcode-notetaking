# 20. Valid Parentheses

**Difficulty:** Easy  
**LeetCode Link:** [20. Valid Parentheses](https://leetcode.com/problems/valid-parentheses/)

---

## Description

Given a string `s` containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is valid.

An input string is valid if:

	- Open brackets must be closed by the same type of brackets.

	- Open brackets must be closed in the correct order.

	- Every close bracket has a corresponding open bracket of the same type.

 

Example 1:**

**Input:** s = "()"

**Output:** true

Example 2:**

**Input:** s = "()[]{}"

**Output:** true

Example 3:**

**Input:** s = "(]"

**Output:** false

Example 4:**

**Input:** s = "([])"

**Output:** true

Example 5:**

**Input:** s = "([)]"

**Output:** false

 

**

---

## Constraints

- **
- `1 <= s.length <= 104`
- `s` consists of parentheses only `'()[]{}'`.

---

## Approach

we can use stack to keep track of what the next value needs to be! 

don't fall for the trap opf empty stack or not checking if stack is empty at the end

---

## Solution Code

```python
class Solution:
    def isValid(self, s: str) -> bool:
        paren_map = {"(":")", "{":"}", "[":"]"}
        #when we see open parens
        #we can store closed paren in the stack
        #we can check if closed paren is what we expected 
        stack = []
        for c in s:
            if c in paren_map:
                stack.append(paren_map[c])
            else:
                if not stack or stack.pop() != c:
                    return False 

        return not stack
```

---

## Time & Space Complexity

- **Time Complexity:** O(n)
- **Space Complexity:** O(n)

---

## Notes

<!-- Add any additional notes, insights, optimizations, or pitfalls here -->

---

## Alternative Solutions

<!-- If you have multiple approaches, document them here -->

---

## Related Problems

<!-- Link to related problems if applicable -->
