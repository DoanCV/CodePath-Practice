"""
BFS to generate all permutations
  skip numbers only change letters
  we can use .swapcase() to flip the capitalization
"""

def find_letter_case_string_permutations(str):
  permutations = []
  permutations.append(str)
  
  # loop through each character
  for i in range(len(str)):
    # if curr char is a letter
    if str[i].isalpha():
      # go through all the previous permutations
      n = len(permutations)
      for j in range(n):
        # make a copy of each and change the capitalization of the current letter in the copy
          # string is immutable so we need to make the change in a list
        copy = list(permutations[j])
        copy[i] = copy[i].swapcase()        
        # append it to permutations
        permutations.append("".join(copy))
  return permutations



def main():
  print("String permutations are: " +
        str(find_letter_case_string_permutations("ad52")))
  print("String permutations are: " +
        str(find_letter_case_string_permutations("ab7c")))


main()

# O(N * 2^N) time complexity, where N is the length of the given string, since for each character there are two permutations and in the worst case the entire string is all alphabeticals.
# O(N * 2^N) space complexity since that is the size of the output.
