class MaxSumSubArrayOfSizeK {
  public static int findMaxSumSubArray(int k, int[] arr) {
    int window_start = 0;
    int max_sum = 0;
    int curr_sum = 0;

    for (int window_end = 0; window_end < arr.length; window_end++) {
      curr_sum += arr[window_end];

      if (window_end - window_start + 1 > k) {
        curr_sum -= arr[window_start];
        window_start++;  
      }

      if (curr_sum > max_sum) {
        max_sum = curr_sum;
      }
    }
    return max_sum;
  }
}