class MinSizeSubArraySum {
  public static int findMinSubArray(int S, int[] arr) {
    int min_sum = arr.length + 1;
    int window_start = 0;
    int curr_sum = 0;

    for (int window_end = 0; window_end < arr.length; window_end++) {
      curr_sum += arr[window_end];

      while (curr_sum >= S) {
        if (window_end - window_start + 1 < min_sum) {
          min_sum = window_end - window_start + 1;
        }
        curr_sum = curr_sum - arr[window_start];
        window_start++;
      }
    }

    if (min_sum > arr.length){
      return -1;
    }
    else {
      return min_sum;
    }
  }
}
