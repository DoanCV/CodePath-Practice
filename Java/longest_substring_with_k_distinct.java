import java.util.*;

class LongestSubstringKDistinct {
  public static int findLength(String str, int k) {

    if (k < 1 || k > str.length() || str.length() == 0) {
      return 0;
    }

    int max_length = 0;
    int window_start = 0;
    Map<Character, Integer> char_frequency_map = new HashMap<>();

    for (int window_end = 0; window_end < str.length(); window_end++) {
      char right_char = str.charAt(window_end);
      char_frequency_map.put(right_char, char_frequency_map.getOrDefault(right_char, 0) + 1);

      while (char_frequency_map.size() > k) {
        char left_char = str.charAt(window_start);
        char_frequency_map.put(left_char, char_frequency_map.get(left_char) - 1);

        if (char_frequency_map.get(left_char) == 0) {
          char_frequency_map.remove(left_char);
        }

        window_start++;
      }

      max_length = Math.max(max_length, window_end - window_start + 1);
    }

    return max_length;
  }
}
