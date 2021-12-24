"""
U
we are given a list of file names
  in typical file systems if adding a name creates a duplicate then we add "(x)" to the name where x is the smallest possible integer that makes the new name unique

return a list of all the names after processing the given list of file name requests


M
Use a hashmap to store the frequency of used names


P
Visit each name in the given name list
  if the name is not in the hashmap 
    add it as a key and initialize the value to 1
    add to result list of final names
  else
    get the count of the existing name
    
    keep incrementing the count until it is unique
      update the name with the format "name(count)"
    
    update the count of the old name and create a new key with the newly created unique name and its value will be 1
    
    add to result list of final names
    
return the list of final names 
    
IR

E
O(N) time complexity where N is the length of the given list of name requests. We loop through all the requests once. Even though we have a while loop inside the name list traversal, we have a hashmap that keeps track of the last count that was used to create a unique file name. This means we will not start from 1. In the worst case, we have a list with the same names. When we visit each name we will have the last number used so accessing and incrementing by 1 is constant time.
O(N) space complexity where N is the length of the given list of name requests. We are using a hashmap to store all of the unique names as keys. If the names are not unique then they each will take up another key but that grows linearly with the size of the input.

"""

class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        names_map = {}
        result = []
        
        for name in names:
            
            if name not in names_map:
                names_map[name] = 1
                result.append(name)
                
            else:
                count = names_map[name]
                temp = name + "(" + str(count) + ")"
                
                while temp in names_map:
                    count += 1
                    temp = name + "(" + str(count) + ")"
                
                names_map[temp] = 1
                names_map[name] = count
                result.append(temp)
                
        return result
            
