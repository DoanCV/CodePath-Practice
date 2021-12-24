"""
U
We have k servers labeled 0 to k-1
    Each server cannot handle more than one request at a time
    
We take in one request at a time, index i (zero index)    
    if all servers are busy the request is dropped
    if the (i % k)th server is available assign the request
    otherwise assign the request to the next available server, i+1 and so on, wrap around is fine

Find the busiest servers, the servers that handled the most number of requests sucessfully
    return the server IDs

M
use two heaps

P
use two heaps (both min heaps)
    available - keep track of available servers
    busy - priority is done time
    
go through each request
    check if any in busy are done and move to available if so
        the priority of the available is index + (busy[0] - index) % k
            this is just circular routing and it will force available[0] to be at least i and at most i + k - 1
    
    add the current request to an available server
    
IR

E
size of the heaps are at most k

O(Nlogk) time complexity where N is the number of requests in arrival and k is the number of servers. We loop through each request that arrives and insert into min heaps of size k and remove from the heaps as well.
O(k) space complexity where k is the number of servers since that is the size of the heaps.
"""
from heapq import *
class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        
        available = [i for i in range(k)] # already a min heap
        busy = []
        
        result = [0 for _ in range(k)]
        
        for index, request_num in enumerate(arrival):
            
            # check if any jobs are done
            while busy and busy[0][0] <= request_num:
                _, x = heappop(busy)
                heappush(available, index + (x-index) % k)
            
            if available:
                i = heappop(available) % k
                heappush(busy, (request_num + load[index], i))
                result[i] += 1
        
        busiest = max(result)
        return [i for i in range(k) if result[i] == busiest]
