"""
given the hour and the minute hand position return the smaller angle between the two hands in degrees
    keep in mind based on where the minute hand is the hour hand will move between whole hours


we know that there is 360 degrees in the clock
    there are 12 hours total so each our is 360/12 = 30 degrees
        knowing this for each minute that passes the hour hand will move 30/60 = .5 degrees
    
    there are 60 minutes total so each minute is 360/60 = 6 degrees
    
since we know the position of the hands and can convert to degrees and determine the smaller angle
"""

class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        
        hour_hand_angle = 30 * hour + .5 * minutes
        
        minute_hand_angle = 6 * minutes
        
        if abs(hour_hand_angle - minute_hand_angle) <= 180:
            return abs(hour_hand_angle - minute_hand_angle)
        else:
            return 360 - abs(hour_hand_angle - minute_hand_angle)
