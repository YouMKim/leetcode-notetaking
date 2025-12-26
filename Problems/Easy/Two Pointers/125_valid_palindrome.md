# 125. Valid Palindrome

**Difficulty:** Easy  
**LeetCode Link:** [125. Valid Palindrome](https://leetcode.com/problems/valid-palindrome/)

---

## Description

A phrase is a **palindrome** if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string `s`, return `true`* if it is a **palindrome**, or *`false`* otherwise*.

 

Example 1:**

```

**Input:** s = "A man, a plan, a canal: Panama"
**Output:** true
**Explanation:** "amanaplanacanalpanama" is a palindrome.

```

Example 2:**

```

**Input:** s = "race a car"
**Output:** false
**Explanation:** "raceacar" is not a palindrome.

```

Example 3:**

```

**Input:** s = " "
**Output:** true
**Explanation:** s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.

```

 

**

---

## Constraints

- **
- `1 <= s.length <= 2 * 105`
- `s` consists only of printable ASCII characters.

---

## Approach

do a left and right pointer check 
we can skip all the values that are non alphanumeric. 
Also make sure the cases match. go towards middle.

---

## Solution Code

```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        #is palindrom ? 
        #same backwards and forwards 
        l,r = 0, len(s)-1 
        #we don't need to check the middle element 
        while l < r:
            #skip all the non alphanumeric
            while not s[l].isalnum() and l < r:
                l+=1
            while not s[r].isalnum() and l < r:
                r-=1 
            if s[l].lower() != s[r].lower():
                return False 
            l+=1
            r-=1 
        return True 
```

---

## Time & Space Complexity

- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

---

## Notes

<!-- Add any additional notes, insights, optimizations, or pitfalls here -->

---

## Alternative Solutions

<!-- If you have multiple approaches, document them here -->

---

## Related Problems

<!-- Link to related problems if applicable -->
