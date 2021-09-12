"""
Recursive BFS to build permutations
  we need to have num amount of open and close to be balanced
  start with an empty array of size 2 * num
    since strings are immutable we will use this to fill in permutation
  we will add the completed permutation into the result array
    a permutation is valid when the count of open parentheses is equal to num and the count of closed parentheses is equal to num
  when we move on to the next index in our builder we are proceeding to the next level of our tree 
  
N = 3
[]
[(]
[((, ()]
[(((, ((), ()(]
[(((, ((), ()(]
[(((), (()(, (()), ()((, ()()]
[((()), (()(), (())(, ()((), ()()(]
[((())), (()()), (())(), ()(()), ()()()]
"""

def generate_valid_parentheses(num):
  result = []
  open_paren_count = 0
  closed_paren_count = 0
  curr_index = 0
  balanced_parentheses_builder = [0 for i in range(2 * num)]
  generate_recurse(num, open_paren_count, closed_paren_count, balanced_parentheses_builder, curr_index, result)
  return result

# recursive helper function
def generate_recurse(num, open_paren_count, closed_paren_count, balanced_parentheses_builder, curr_index, result):
  # check if we are done
    # append to the result, we build a string with an array so we need to join
  if open_paren_count == num and closed_paren_count == num:
    result.append("".join(balanced_parentheses_builder))
  
  # we are not done
  else:
    # if the open count is less than num we are allowed to add a open parentheses
      # when we add one we will recurse to the next index in our builder
    if open_paren_count < num:
      balanced_parentheses_builder[curr_index] = "("
      generate_recurse(num, open_paren_count + 1, closed_paren_count, balanced_parentheses_builder, curr_index + 1, result)
    # if the open count is greater than the closed count we are allowed to add a closed parentheses
      # when we add one we will recurse to the next index in our builder
    if open_paren_count > closed_paren_count:
      balanced_parentheses_builder[curr_index] = ")"
      generate_recurse(num, open_paren_count, closed_paren_count + 1, balanced_parentheses_builder, curr_index + 1, result)

def main():
  print("All combinations of balanced parentheses are: " +
        str(generate_valid_parentheses(2)))
  print("All combinations of balanced parentheses are: " +
        str(generate_valid_parentheses(3)))


main()

# O(N * 2^N) time complexity, where N is nums. At each level of our tree we can either add a '(' or a ')' so that is 2^N permutations. When we are done building we need to concatenate the list into a string. According to Grokking, the worst case time complexity is bounded by the Catalan numbers.
# O(N * 2^N) space complexity since that is the size of our output.
