def find_pairs(nums, target):
    pairs = set()
    seen = set()

    for num in nums:
        diff = target - num
        if diff in seen:
            pairs.add((min(num, diff), max(num, diff)))
        seen.add(num)

    return pairs


nums = [2, 4, 5, 3, 7, 8, 1]
print(find_pairs(nums, 9))
