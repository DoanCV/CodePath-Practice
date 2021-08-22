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
      # go through all the previous permutations
        # make a copy of each and change the capitalization of the current letter in the copy
        # append it to permutations
  
  return permutations


def main():
  print("String permutations are: " +
        str(find_letter_case_string_permutations("ad52")))
  print("String permutations are: " +
        str(find_letter_case_string_permutations("ab7c")))


main()
