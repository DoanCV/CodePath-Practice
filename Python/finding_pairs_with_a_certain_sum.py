from collections import Counter
class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1 = nums1
        self.nums2 = nums2
        
        self.freq_map = Counter(nums2)

    def add(self, index: int, val: int) -> None:
        # since we are adding a value the old value frequency of course goes down
        self.freq_map[self.nums2[index]] -= 1
        
        # add the new number and increase its frequency
        self.nums2[index] += val
        self.freq_map[self.nums2[index]] += 1

    def count(self, tot: int) -> int:
        """
        we traverse each element a in nums1 and check if we found b where a + b = tot => b = tot - a
        """
        count = 0
        for num in self.nums1:
            count += self.freq_map[tot - num]
        return count


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)

"""
add elements
    at given index in nums2 add the given value

count
    get the number of pairs that sum to a target
    a pair is a number from nums1 and another from nums2
    just store the frequency of nums2 elements in hashmap and find the complement by looping through nums1

Count
O(M) time complexity where M is the length of nums1 since we loop through all elements of nums1 to see if the complement, i.e. tot - num_from_nums1, exists in the nums2 frequency map.

Constructor
O(N) time complexity where N is the length of nums2 since we get the frequency of all the elements with loop and add to a hashmap. Adding to the hashmap is constant time.
O(N) space complexity where N is the length of nums2 since we are using a hashmap to store the frequency of elements in nums2 to get the total number of pairs. In the worst case each element in nums2 is unique so there are N keys in the hashmap.
"""
