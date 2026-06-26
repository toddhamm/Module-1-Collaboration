class Solution:

    # initialize the object and array (list)
    def __init__(self, arr):
        self.arr = arr

    # custom method to sort the list of numbers without using the built-in sort() function
    def sort012(self):
        low = 0
        mid = 0
        high = len(self.arr) - 1

        while mid <= high:
            if self.arr[mid] == 0:
                self.arr[low], self.arr[mid] = self.arr[mid], self.arr[low]
                low += 1
                mid += 1
            elif self.arr[mid] == 1:
                mid += 1
            else: 
                self.arr[mid], self.arr[high] = self.arr[high], self.arr[mid]
                high -= 1
                
        return self.arr

# the array (or list)
l = [0, 1, 2, 0, 1, 2]

# create the object and pass it the list (array)
s = Solution(l)

# output the sorted list 
print("Sorted:", s.sort012())

# result should be Sorted: [0, 0, 1, 1, 2, 2]