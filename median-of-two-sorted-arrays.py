# I don't know what am i doing it can just pass the first 429 tests!! T-T
class Solution(object):
  def findMedianSortedArrays(self, nums1, nums2):
    def do_magic(array):
      length_of_array = len(array)
      if (length_of_array == 0):
        if (array is nums1):
          median = do_magic(nums2)
        else:
          median = do_magic(nums1)
      elif (length_of_array == 1):
        median = array[0]
      elif (length_of_array == 2):
        median = (array[0] + array[1]) / float(2)
      elif (length_of_array % 2 == 0):
        median = array[(length_of_array / 2) - 1] + 0.5
      else:
        median = array[length_of_array / 2]
      return median
    x = do_magic(nums1)
    y = do_magic(nums2)
    print(x)
    print(y)
    if (nums1 != nums2):
      try:
        if (nums1[1] - nums1[0] == nums2[1] - nums2[0]):
          if (x > y):
            return (x - 0.5) - (y - 1)
          else:
            return (y - 0.5) - (x - 1)
      except:
        return (x + y) / float(2)
    return (x + y) / float(2)
