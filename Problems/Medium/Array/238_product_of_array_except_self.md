# 238. Product of Array Except Self

**Difficulty:** Medium  
**LeetCode Link:** [238. Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/)

---

## Description

Given an integer array `nums`, return *an array* `answer` *such that* `answer[i]` *is equal to the product of all the elements of* `nums` *except* `nums[i]`.

The product of any prefix or suffix of `nums` is **guaranteed** to fit in a **32-bit** integer.

You must write an algorithm that runs in `O(n)` time and without using the division operation.

 

Example 1:**

```
**Input:** nums = [1,2,3,4]
**Output:** [24,12,8,6]

```
Example 2:**

```
**Input:** nums = [-1,1,0,-3,3]
**Output:** [0,0,9,0,0]

```

 

**

---

## Constraints

- **
- `2 <= nums.length <= 105`
- `-30 <= nums[i] <= 30`
- The input is generated such that `answer[i]` is **guaranteed** to fit in a **32-bit** integer.
- **Follow up:** Can you solve the problem in `O(1)` extra space complexity? (The output array **does not** count as extra space for space complexity analysis.)

---

## Approach

we do a simple product of the left and from the right and multiply both! this way we can get both in two pass.

---

## Solution Code

```python
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        products = [1] * len(nums)
        run_prod = 1
        for i in range(len(nums)):
            products[i] = run_prod 
            run_prod*=nums[i]
        #set the numbers beforehand! 
        run_prod = 1
        for i in reversed(range(len(nums))):
            products[i] *= run_prod 
            run_prod*=nums[i]
        return products 

```

---

## Time & Space Complexity

- **Time Complexity:** O(N)
- **Space Complexity:** O(N)

---

## Notes


---

## Alternative Solutions

What if we want to do it with constant space? 

<!-- If you have multiple approaches, document them here -->

---

## Related Problems

<!-- Link to related problems if applicable -->
