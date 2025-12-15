def max_product_pair(nums):
    nums = list(set(nums))
    nums.sort()

    prod1 = nums[-1] * nums[-2]   
    prod2 = nums[0] * nums[1]     

    return (nums[-1], nums[-2]) if prod1 > prod2 else (nums[0], nums[1])


nums = [10, 3, 5, 6, 20]
print(max_product_pair(nums))
