class PairWithTargetSum {

  public static int[] search(int[] arr, int targetSum) {
    int left = 0;
    int right = arr.length - 1;

    while (left < right) {
      if (arr[left] + arr[right] == targetSum) {
        return new int[] {left, right} ;
      }
      if (arr[left] + arr[right] > targetSum) {
        right--;
      }
      if (arr[left] + arr[right] < targetSum) {
        left++;
      }
    }

    return new int[] { -1, -1 };
  }
}
