# Brute-force solution: compare each element with every other element
# Time complexity:O(n^2)
# Space complexity:O(1)
def contains_duplicate (nums):
    for i, x in enumerate(nums):
        for j, y in enumerate (nums):
            if x == y and i != j:
                return True
    return False

print(contains_duplicate([1,2,3,3]))
print(contains_duplicate([1,2,3,4]))
print(contains_duplicate([1,8,9]))