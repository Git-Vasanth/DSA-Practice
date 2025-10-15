from typing import List 


def minSubArrayLen(target: int, nums: List[int]):

    left = 0
    n = len(nums)
    current_length_sub_array  = 0
    current_sum = 0
    min_length_subarray = n + 1

    for right in range(0 , n):
        
        current_sum = current_sum + nums[right]

        while current_sum >= target :

            current_length_sub_array = right - left + 1

            min_length_subarray = min(min_length_subarray , current_length_sub_array)

            current_sum = current_sum - nums[left]

            left = left + 1

    if min_length_subarray == n + 1:

        return 0
    
    else :

        return min_length_subarray

