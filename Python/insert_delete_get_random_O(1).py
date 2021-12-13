import random
class RandomizedSet:

    def __init__(self):
        self.positions = {}
        self.numbers = []
        

    def insert(self, val: int) -> bool:
        if val in self.positions:
            return False
        else:
            self.numbers.append(val)
            self.positions[val] = len(self.numbers) - 1       
            return True

    def remove(self, val: int) -> bool:
        if val not in self.positions:
            return False
        else:
            index = self.positions[val]
            
            if index < len(self.numbers) - 1:
                # overwrite the element to be removed with the last element so we can remove in O(1)
                last = self.positions[len(self.numbers) - 1]
                self.numbers[index] = self.numbers[last]
                self.positions[val] = index
                
            self.numbers.pop()
            del self.positions[len(self.numbers) - 1]
        
            return True
        
    def getRandom(self) -> int:
        return self.numbers[random.randint(0, len(self.numbers) - 1)]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

"""
We have have a hashmap, to quickly search and remove
    we know nothing about the hashing function
        our keys have to be delibrately chosen
        hashmap = {value: index in the array}

random selection
    get a random number from 0 to the total number of values we inserted so far - 1

"""
