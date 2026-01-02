# 49. Group Anagrams

**Difficulty:** Medium  
**LeetCode Link:** [49. Group Anagrams](https://leetcode.com/problems/group-anagrams/)

---

## Description

Given an array of strings `strs`, group the anagrams together. You can return the answer in **any order**.

 

Example 1:**

**Input:** strs = ["eat","tea","tan","ate","nat","bat"]

**Output:** [["bat"],["nat","tan"],["ate","eat","tea"]]

**Explanation:**

	- There is no string in strs that can be rearranged to form `"bat"`.

	- The strings `"nat"` and `"tan"` are anagrams as they can be rearranged to form each other.

	- The strings `"ate"`, `"eat"`, and `"tea"` are anagrams as they can be rearranged to form each other.

Example 2:**

**Input:** strs = [""]

**Output:** [[""]]

Example 3:**

**Input:** strs = ["a"]

**Output:** [["a"]]

 

**

---

## Constraints

- **
- `1 <= strs.length <= 104`
- `0 <= strs[i].length <= 100`
- `strs[i]` consists of lowercase English letters.

---

## Approach

pretty simple idea, we can organize anagram by freqeuncy.
we can use tuple as the key for the dictionary
then return the values in the dictionary.

---

## Solution Code

```python
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #anagram dict 
        anagram_dict = defaultdict(list)
        #key of counter
        #value of list of strings

        for s in strs:
            key = [0] * 26 
            for c in s:
                key[ord(c)-ord('a')]+=1 
            anagram_dict[tuple(key)].append(s)
        
        return list(anagram_dict.values())
```

---

## Time & Space Complexity

- **Time Complexity:** O(NK), where N is the length of strs, and K is the maximum length of a string in strs. Counting each string is linear in the size of the string, and we count every string.

- **Space Complexity:** O(NK), the total information content stored in ans.
---

## Notes

<!-- Add any additional notes, insights, optimizations, or pitfalls here -->

---

## Alternative Solutions

<!-- If you have multiple approaches, document them here -->

---

## Related Problems

<!-- Link to related problems if applicable -->
