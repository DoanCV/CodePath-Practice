"""
codesignal :sadge:

we know that the elements when rotating the box 90 degrees clockwise just turn from row to column and are subject to "gravity"
    one row will not affect another row with a rotation

for each row just move the stones as far right as possible
    this is gravity after the rotation
    
    to do this we traverse from right to left and keep a pointer to see where we can move the stone
        if we find an obstacle move the position pointer one space before since that is the "lowest" place a stone can be
        
        if we find a stone just swap the stone with the pointer position value and move the pointer to the left for potentially the next stone
    

once we move we can rotate to reflect the changes
"""

class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        for row in box:
            move_position = len(row) - 1             # initialize with the last position in row
            for j in range(len(row) - 1, -1, -1):    # iterate from the end of the row
                if row[j] == "*":                    # we cannot move stones behind obstacles,
                    move_position = j - 1            # so update move position to the first before obstacle
                elif row[j] == "#":                  # if stone, move it to the "move_position"
                    row[move_position], row[j] = row[j], row[move_position]
                    move_position -= 1

        return zip(*box[::-1])                       # rotate array
