# You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.
# Return the merged string.

# Example 1:
# Input: word1 = "abc", word2 = "pqr"
# Output: "apbqcr"
# Explanation: The merged string will be merged as so:
# word1:  a   b   c
# word2:    p   q   r
# merged: a p b q c r


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        self.word1 = word1
        self.word2 = word2

        if len(word2) >= len(word1):
            max = word2
            min = word1
        else:
            max = word1
            min = word2

        for v in range(len(max)):
            if(len(min) > v):
                print(word1[v],word2[v],end="",sep="")
                continue
            print(max[v],end="",sep="")


a = input()
b = input()
s = Solution()
s.mergeAlternately(a,b)
print("|")