# 347. Top K Frequent Elements

**Difficulty:** Medium  
**LeetCode Link:** [347. Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/)

---

## Description

Given an integer array `nums` and an integer `k`, return *the* `k` *most frequent elements*. You may return the answer in **any order**.

 

Example 1:**

**Input:** nums = [1,1,1,2,2,3], k = 2

**Output:** [1,2]

Example 2:**

**Input:** nums = [1], k = 1

**Output:** [1]

Example 3:**

**Input:** nums = [1,2,1,2,1,2,3,1,3,2], k = 2

**Output:** [1,2]

 

**

---

## Constraints

- **
- `1 <= nums.length <= 105`
- `-104 <= nums[i] <= 104`
- `k` is in the range `[1, the number of unique elements in the array]`.
- It is **guaranteed** that the answer is **unique**.
- **Follow up:** Your algorithm's time complexity must be better than `O(n log n)`, where n is the array's size.

---

## Approach

Its a bucket sort approach! 
first create a dictionary with the Element as key and frequency as the value 

then do a linear time bucketsort since we know the max value -> idx as frequency and elements as content of the list

and then we return the top k 

---

## Solution Code

```python
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #first 
        #key: element 
        #value : freq
        freq_dict = defaultdict(int)
        for num in nums:
            freq_dict[num]+=1 
        
        #go from 0.1.....total nums
        #extreme case of one element frequncies
        freq_list = [[] for _ in range(len(nums)+1)]

        for element, freq in freq_dict.items():
            freq_list[freq].append(element)

        #second do bucket sorting 
        #idx : freq 
        # values : elements 
        answer = []
        for idx in range(len(nums),0,-1):
            for element in freq_list[idx]:
                answer.append(element)
                if len(answer) == k:
                    return answer 

```

---

## Time & Space Complexity

- **Time Complexity:** O(n)
- **Space Complexity:** O(n)

---

## Notes

We can implement this using Quick Select! lets practice 


---

## Alternative Solutions
```python
from collections import Counter 

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #step 1 count frequencies 
        freq_map = Counter(nums)
        unique = list(set(nums))

        #use quickselect to find k most  
        #we are sorting by value of freq!

        def quickselect(left, right, k_smallest):
            #sort the unique [left:right+1] so k_th smallest is in correct position 
            #we want to sort by desecnding in this case 
            if left == right:
                return 
            pivot_index = partition(left,right)
            if k_smallest == pivot_index:
                return 
            
            elif k_smallest < pivot_index:
                quickselect (left, pivot_index-1, k_smallest)
            else:
                quickselect(pivot_index+1, right, k_smallest)
        
        def partition(left, right):
            #partition the unique around random pivot and get random pivot
            #we want higher freq <- left 
            #lower freq -> right
            #pick a random integer as the pivot
            pivot_index = random.randint(left,right)
            #grab the freq of the pivot index
            pivot_freq = freq_map[unique[pivot_index]]
            #so we switch the pivot and the end 
            #so that when we partition its ok 
            unique[pivot_index], unique[right] = unique[right], unique[pivot_index]
            store_index = left #we have the boundary -- everything before has higher freq than pivot 
            for i in range(left,right):
                #check if current element is higher freq than pivot 
                #if it is then it should go left of pivot 
                if freq_map[unique[i]] > pivot_freq:
                    unique[store_index], unique[i] = unique[i], unique[store_index]
                    store_index+=1 
            # we move the pivot (which is currently in the right index )
            #we move it to the final position 
            unique[right], unique[store_index] = unique[store_index], unique[right] 

            return store_index 
        
        #we are selecting for kth index <- k-1 for 0 index 
        #do the select for the entire array 
        quickselect(0, len(unique)-1, k-1)
        return unique[:k]

```


---

## Related Problems

<!-- Link to related problems if applicable -->
