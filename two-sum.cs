// 🎀 Runtime: 143 Milliseconds **⸜(｡ ˃ ᵕ ˂ )⸝♡**
// 💞 Memory : 47.10 MB ( • ̀ω•́ )✧
/*
  I have a silly idea! It is not optimized well,
  but it was fun to think about it ^-^ 

  | Num1 | Num2 | Target |
  |------|------|--------|
  | Odd  + Even = Odd    |  (3 + 2 = 5)
  | Even + Even = Even   |  (6 + 8 = 14)
  | Odd  + Odd  = Even   |  (1 + 9 = 10)
  |----------------------|
  
  If the target is an even number, the other numbers should be equal when you mod them with two!!
  The for loop will the skip the number if it is not possible to get the target! ^-^

  
*/
public class Solution {
  public int[] TwoSum(int[] nums, int target) {
    int rounds = 0; // To count how many times the loop re-started ^-^
    int index  = nums[rounds]; // Memorize a number to not use multiple loops!!
    
    bool index_is_even  = index  % 2 == 0;
    bool target_is_even = target % 2 == 0;

    for (int n = 1; n < nums.Length; n++) {
      int number = nums[n];

      bool number_is_even = number % 2 == 0;
      bool should_skip = target_is_even ^ (index_is_even == number_is_even);

      if (!should_skip && (number + index == target)) {
        return new int[] { rounds, n };
      }

      if ((n + 1) == nums.Length) { // When the loop reached to end... switch index and do setup, then do it again! ^-^
        rounds++;
        n = rounds;

        index = nums[rounds];
        index_is_even = index % 2 == 0;
      }
    }
    return null;
  }
}
