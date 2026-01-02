# 271. Encode and Decode Strings

**Difficulty:** Medium  
**LeetCode Link:** [271. Encode and Decode Strings](https://leetcode.com/problems/encode-and-decode-strings/)

---

## Description

<!-- Insert problem description here -->

---

## Constraints

<!-- Insert constraints here -->

---

## Approach

I encoded and deocded by coding the total length of the string itself. 
so we start with a number value and then tack on a  special charecter 
and then encode it this way to avoid cases of numbers accidentally being read etc
---

## Solution Code

```python
class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        output = [] 
        for s in strs:
            output.append(str(len(s)) + "#" + s)
        return "".join(output)

        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        #first retrieve and get all the numbers out 
        words = [] 
        l = 0 
        while l < len(s):
            r = l 
            while r < len(s) and s[r] != "#":
                r+=1 
            num_letters = int(s[l:r])
            #skip over the special letter 
            l = r+1 
            next_word = s[l:l+num_letters]
            words.append(next_word)
            l += num_letters

        return words
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
