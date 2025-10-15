from typing import List

class NumArray:
    """
    Handles multiple range sum queries efficiently using the Prefix Sum array.
    """
    def __init__(self, nums: List[int]):
        # 1. Initialize the storage for the Prefix Sums
        self.prefix = [0]
        
        # 2. Variable to hold the running sum
        current_sum = 0
        
        # 3. Build the Prefix Sum array (P)
        for x in nums:
            current_sum += x
            self.prefix.append(current_sum)
        
        # O(N) Time for initialization (where N is len(nums))
        

    def sumRange(self, left: int, right: int) -> int:
        """
        Calculates the sum of elements between indices left and right inclusive in O(1) time.
        Formula: P[right + 1] - P[left]
        """
        # The value at self.prefix[right + 1] is the sum of nums[0]...nums[right]
        # The value at self.prefix[left] is the sum of nums[0]...nums[left - 1]
        return self.prefix[right + 1] - self.prefix[left]
        
        # O(1) Time for query