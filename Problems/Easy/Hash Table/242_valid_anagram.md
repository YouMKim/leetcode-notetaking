# 242. Valid Anagram

**Difficulty:** Easy  
**LeetCode Link:** [242. Valid Anagram](https://leetcode.com/problems/valid-anagram/)

---

## Description

Given two strings `s` and `t`, return `true` if `t` is an anagram of `s`, and `false` otherwise.

 

Example 1:**

**Input:** s = "anagram", t = "nagaram"

**Output:** true

Example 2:**

**Input:** s = "rat", t = "car"

**Output:** false

 

**

---

## Constraints

- **
- `1 <= s.length, t.length <= 5 * 104`
- `s` and `t` consist of lowercase English letters.
- **Follow up:** What if the inputs contain Unicode characters? How would you adapt your solution to such a case?

---

## Approach

super simple - simply compare the counts of each char. anagram must have equal value 

---

## Solution Code

```python
from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #are they anagram or not? 
        return Counter(s) == Counter(t)
```

---

## Time & Space Complexity

- **Time Complexity:** O(?)
- **Space Complexity:** O(?)

---

## Notes

<!-- Add any additional notes, insights, optimizations, or pitfalls here -->

---

## Alternative Solutions

<!-- If you have multiple approaches, document them here -->

---

## Related Problems

<!-- Link to related problems if applicable -->
