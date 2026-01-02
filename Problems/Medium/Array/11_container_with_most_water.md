# 11. Container With Most Water

**Difficulty:** Medium  
**LeetCode Link:** [11. Container With Most Water](https://leetcode.com/problems/container-with-most-water/)

---

## Description

You are given an integer array `height` of length `n`. There are `n` vertical lines drawn such that the two endpoints of the `ith` line are `(i, 0)` and `(i, height[i])`.

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return *the maximum amount of water a container can store*.

**Notice** that you may not slant the container.

 

Example 1:**

```

**Input:** height = [1,8,6,2,5,4,8,3,7]
**Output:** 49
**Explanation:** The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

```

Example 2:**

```

**Input:** height = [1,1]
**Output:** 1

```

 

**

---

## Constraints

- **
- `n == height.length`
- `2 <= n <= 105`
- `0 <= height[i] <= 104`

---

## Approach

<!-- Explain your approach to solving this problem -->

---

## Solution Code

```python
class Solution:
    def maxArea(self, height: List[int]) -> int:
        #get the max area 

        #idea is we maximize the area with the width
        #and then we can reduce but its always the min 
        max_area = 0 
        l,r = 0, len(height)-1 
        while l < r:
            curr_area = (r-l) * min(height[l], height[r])
            max_area = max(curr_area, max_area)
            if height[l] < height[r]:
                l+=1
            else:
                r-=1 

        return max_area 
```

---

## Time & Space Complexity

- **Time Complexity:** O(n)
- **Space Complexity:** O(1) if we don't count the input 

---

## Notes

<!-- Add any additional notes, insights, optimizations, or pitfalls here -->

two pointer solution. The idea is that we have a max area. We reduce the parts that are lower because we cannot get larger area if we make that one fixed.

---

## Alternative Solutions

<!-- If you have multiple approaches, document them here -->

---

## Related Problems

<!-- Link to related problems if applicable -->
