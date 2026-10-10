# Brute-force solution
# Time complexity: O(n^2)
# Space complexity: O(1)

def two_sum(nums, target):
    for i, x in enumerate(nums):
        for j, y in enumerate(nums):
            if x + y == target and i != j:
                return (i, j)

print(two_sum([1, 2, 3, 4, 5], 5))
print(two_sum([4, 7, 8, 2, 5], 10))
print(two_sum([11, 4, 3, 1, 2], 15))
