# 567. Permutation in String

**Difficulty:** Medium  
**LeetCode Link:** [567. Permutation in String](https://leetcode.com/problems/permutation-in-string/)

---

## Description

Given two strings `s1` and `s2`, return `true` if `s2` contains a permutation of `s1`, or `false` otherwise.

In other words, return `true` if one of `s1`'s permutations is the substring of `s2`.

 

Example 1:**

```

**Input:** s1 = "ab", s2 = "eidbaooo"
**Output:** true
**Explanation:** s2 contains one permutation of s1 ("ba").

```

Example 2:**

```

**Input:** s1 = "ab", s2 = "eidboaoo"
**Output:** false

```

 

**

---

## Constraints

- **
- `1 <= s1.length, s2.length <= 104`
- `s1` and `s2` consist of lowercase English letters.

---

## Approach

<!-- Explain your approach to solving this problem -->

---

## Solution Code

```python
from collections import Counter, defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False 
        
        s_counter = Counter(s1)
        window_counter = defaultdict(int)

        for i in range(len(s2)):
            curr_char = s2[i]
            window_counter[curr_char]+=1 

            #we check if current window idx hit same size as s1
            if i >= len(s1)-1:
                if s_counter == window_counter:
                    return True 
                char_to_del = s2[i-len(s1)+1]
                window_counter[char_to_del] -=1
                if window_counter[char_to_del] == 0:
                    del window_counter[char_to_del]
        return False 
                

```

---

## Time & Space Complexity

- **Time Complexity:** O(n)
- **Space Complexity:** O(n)

---

## Notes

we simply compare the frequnecies in the same window! so it is easy to compare.
one note about dictionary vs list is that for dictionary we could run into non alphabe char out side of 26!
if assumption is only known alphabets then yeah we can do list of 26.
---

## Alternative Solutions

<!-- If you have multiple approaches, document them here -->

---

## Related Problems

<!-- Link to related problems if applicable -->
