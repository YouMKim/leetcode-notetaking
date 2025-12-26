# 128. Longest Consecutive Sequence

**Difficulty:** Medium  
**LeetCode Link:** [128. Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/)

---

## Description

Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

---

## Examples

### Example 1

**Input:**
```
nums = [100,4,200,1,3,2]
```

**Output:**
```
4
```

**Explanation:**
The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

### Example 2

**Input:**
```
nums = [0,3,7,2,5,8,4,6,0,1]
```

**Output:**
```
9
```

### Example 3

**Input:**
```
nums = [1,0,1,2]
```

**Output:**
```
3
```

---

## Constraints

<!-- Add constraints if available -->

---

## Approach

The key insight is to use a set for O(1) lookup and only start counting sequences from the beginning of a sequence (i.e., when `num-1` is not in the set). This ensures we only traverse each sequence once, achieving O(n) time complexity.

**Key optimization:** Iterate over `num_set` instead of `nums` to avoid duplicate work, and only start counting when we're at the beginning of a sequence.

---

## Solution Code

```python
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        answer = 0 
        # note the optimization of iterating the num_set
        for num in num_set:
            # guarantee that we start at beginning of seq
            if num-1 not in num_set:
                length = 0 
                while num+length in num_set:
                    length+=1 
                answer = max(answer, length)
        return answer
```

---

## Time & Space Complexity

- **Time Complexity:** O(n) - We visit each number at most twice (once in the outer loop, once when counting sequences)
- **Space Complexity:** O(n) - For the set storing all numbers

---

## Notes

### Initial Pitfall

Here's an initial approach that had a problem:

```python
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        seen = set()
        answer = 0 
        for num in nums:
            if num in seen:
                continue 
            length = 0 
            while num+length in num_set:
                seen.add(num+length)
                length+=1 
            
            answer = max(answer, length)
        return answer
```

**Problem with this approach:** We cannot guarantee the order in which the sequence can be found. The optimization of iterating over `num_set` and only starting from sequence beginnings (when `num-1` not in set) is crucial for correctness and efficiency.

---

## Alternative Solutions

<!-- Add alternative solutions if applicable -->

---

## Related Problems

<!-- Link to related problems if applicable -->

