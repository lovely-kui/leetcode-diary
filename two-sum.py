# Complexity: O(n^2) T-T
# Runtime: 1412ms

# Let's say we have an array goes from one to four and we want seven!! 
# We will use first element as an index and start with the second element!!

# [|1|, 2, 3, 4]
#       ^ 1 + 2 = 3 
### We failed go to next step :c

# [|1|, 2, 3, 4]
#          ^ 1 + 3 = 4 
### Failed again, next step please ;-;

# [|1|, 2, 3, 4]
#             ^ 1 + 4 = 5 
### Fail again, but we reached to end of the array!! So we will change the index and try again :3

# [1, |2|, 3, 4]
#          ^ 2 + 3 = 5
### We started from three because we already did!! 2 + 1

# [1, |2|, 3, 4]
#             ^ 2 + 4 = 6
### We are really close this time, change the index again!!

# [1, 2, |3|, 4]
#             ^ 3 + 4 = 7
# Yippe!! We did it!!! :3

class Solution(object):
  def twoSum(self, nums, target):
    rounds = 0 # To count how many times the loop re-started ^-^
    index  = nums[rounds] # Memorize a number to not use multiple loops!!

    step  = 1 # This will be the steps for the loop!!
    total = len(nums)
    while step < total:
      number = nums[step]

      if (number + index == target):
        return [rounds, step]
      if ((step + 1) == len(nums)):
        # When we reach to end change the index and re-start ^o^!!
        rounds+= 1
        step  = rounds
        index = nums[rounds]
      step += 1
    return []
