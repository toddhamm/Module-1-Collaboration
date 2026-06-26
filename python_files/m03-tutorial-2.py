'''
Given a sorted array arr[] and an integer k, find the position(0-based indexing) at which k is present in the array using binary search. 
If k doesn't exist in arr[] return -1. 

Note: If multiple occurrences are there, please return the smallest index.

Examples
Input: arr[] = [1, 2, 3, 4, 5], k = 4
Output: 3
Explanation: 4 appears at index 3.
Input: arr[] = [11, 22, 33, 44, 55], k = 445
Output: -1
Explanation: 445 is not present.
Input: arr[] = [1, 1, 1, 1, 2], k = 1
Output: 0
Explanation: 1 appears at index 0.
'''

class Solution:

    # initialize the object, passing it the array and k value
    def __init__(self, arr, k):
        self.arr = arr
        self.k = k

    def firstSearch(self):
        # find the position of the k value in the array and output it
        if self.k in self.arr:
            i = self.arr.index(self.k)
            return i
        else: 
            return -1

# implementation
a1 = [1, 2, 3, 4, 5]
k1 = 4
s1 = Solution(a1, k1)
print(s1.firstSearch())

a2 = [11, 22, 33, 44, 55]
k2 = 455
s2 = Solution(a2, k2)
print(s2.firstSearch())

a3 = [1, 1, 1, 1, 2]
k3 = 1
s3 = Solution(a3, k3)
print(s3.firstSearch())