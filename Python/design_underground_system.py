class UndergroundSystem:

    def __init__(self):
        self.checkInMap = {}
        self.checkOutMap = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkInMap[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start_station, start_time = self.checkInMap[id]
        
        route_time = t - start_time
        route_name = start_station + "_" + stationName
        
        # if the route has not been taken yet then we can get a default value of 0 total time on the route and 0 people in total who took the route
        if route_name not in self.checkOutMap:
            total_time_on_route, total_customers_on_route = 0, 0
        else:
            total_time_on_route, total_customers_on_route = self.checkOutMap[route_name]
        
        self.checkOutMap[route_name] = (total_time_on_route + route_time, total_customers_on_route + 1)
        
        # we do not need the checkIn information anymore, delete to save space
        del self.checkInMap[id]

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        route_name = startStation + "_" + endStation
        
        total_time_on_route, total_customers_on_route = self.checkOutMap[route_name]
        
        return total_time_on_route / total_customers_on_route

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)

"""
U
we have a customers who check into a station at some time
    then they checkout at another station at another time
    
for each route we need to find the average times based on the times that we have seen so far
    we are guaranteed that every request to calculate will have already processed a start and end time

a customer can be checked into only one station at a time


M/P
we need to map the end - start time to a route
    that way we can take the average
    each time a route is taken that means a customer took the route so we need the total number of customers
    
average = total time taken for the route / number of customers that took the route

we can use hashmaps to store the information we need and update for each call to checkIn and checkOut

checkIn
    will store {customer id: (start station, time)}
    
    in the checkIn function we will use the start time

checkOut
    in the checkOut function we will store the end - start time as well as the entire route, start station + end station
        this way we can calculate the average time on the route
    
    instead of storing each time in a list
        we can just keep track of the number of people who have taken this route and the total amount of time spent on this route across all customers
    {route: (totalTime, number of customers who finished the route)}
    
getAverageTime
    we are given the start and end stations so we can use this as our key to find the times
        return the result when we divide the values in our tuple for the given route


I
See class above

R
The given test cases work after manually running through them

E
O(1) time complexity for each of the functions
O(N + M) space complexity, where N is the number of checkIns and M is the number of checkouts.
"""
