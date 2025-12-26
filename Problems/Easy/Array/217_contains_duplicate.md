# 217. Contains Duplicate

**Difficulty:** Easy  
**LeetCode Link:** [217. Contains Duplicate](https://leetcode.com/problems/contains-duplicate/)

---

## Description

Given an integer array `nums`, return `true` if any value appears **at least twice** in the array, and return `false` if every element is distinct.

 

Example 1:**

**Input:** nums = [1,2,3,1]

**Output:** true

**Explanation:**

The element 1 occurs at the indices 0 and 3.

Example 2:**

**Input:** nums = [1,2,3,4]

**Output:** false

**Explanation:**

All elements are distinct.

Example 3:**

**Input:** nums = [1,1,1,3,3,4,3,2,4,2]

**Output:** true

 

**

---

## Constraints

- **
- `1 <= nums.length <= 105`
- `-109 <= nums[i] <= 109`

---

## Approach

We must at least iterate everything once to make sure
check for duplicate is simple with O(1) lookup datastructure
---

## Solution Code

```python
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        #if any value appears at least twice
        seen = set()
        for num in nums:
            if num in seen:
                return True 
            seen.add(num)
        return False 
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
