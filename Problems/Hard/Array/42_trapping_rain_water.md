# 42. Trapping Rain Water

**Difficulty:** Hard  
**LeetCode Link:** [42. Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/)

---

## Description

Given `n` non-negative integers representing an elevation map where the width of each bar is `1`, compute how much water it can trap after raining.

 

Example 1:**

```

**Input:** height = [0,1,0,2,1,0,1,3,2,1,2,1]
**Output:** 6
**Explanation:** The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

```

Example 2:**

```

**Input:** height = [4,2,0,3,2,5]
**Output:** 9

```

 

**

---

## Constraints

- **
- `n == height.length`
- `1 <= n <= 2 * 104`
- `0 <= height[i] <= 105`

---

## Approach

<!-- Explain your approach to solving this problem -->

---

## Solution Code

```python
class Solution:
    def trap(self, height: List[int]) -> int:
        max_left = 0
        max_right = 0
        l,r = 0, len(height)-1 
        total_water = 0 
        while l <= r:
            if height[l] < height[r]:
                total_water += max(0, max_left - height[l])
                max_left = max(max_left, height[l])
                l+=1
            else:
                total_water += max(0, max_right- height[r])
                max_right = max(max_right, height[r])
                r-=1 
        return total_water

```

---

## Time & Space Complexity

- **Time Complexity:** O(?)
- **Space Complexity:** O(?)

---

## Notes

TWo pointer appraoch.

Concentually realize that the water height depends on the max. But the minimum of the maximum of the two sides!
and we only care about that if the water spills. and so we can keep reducing from the shorter side towards center
---

## Alternative Solutions

<!-- If you have multiple approaches, document them here -->

---

## Related Problems

<!-- Link to related problems if applicable -->
