# Note that this function should return a ListNode, not an int
def getIntersectionNode(list1, list2):
    if not list1 or not list2:
        return None
    
    tail1 = list1
    while tail1.next is not None:
        tail1 = tail1.next
    tail1.next = list2
    
    hare = list1
    tortoise = list1
    
    while True:
        if not hare.next or not hare.next.next:
            tail1.next = None
            return None
        else:
            tortoise = tortoise.next
            hare = hare.next.next
            if hare == tortoise:
                hare = list1
                break
                
    while hare != tortoise:
        hare = hare.next
        tortoise = tortoise.next
    
    tail1.next = None
    return hare
