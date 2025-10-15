def findMaxAverage(nums, k) -> float:

    if len(nums) == 1 or len(nums) < k:
        return float(nums[0])

    current_sum = float(sum(nums[:k]))
    max_sum = current_sum

    # Step 2: Slide the window
    for i in range(k, len(nums)):

        current_sum = current_sum - nums[i - k] + nums[i]

        if current_sum > max_sum:
            max_sum = current_sum


    return float(max_sum / k)