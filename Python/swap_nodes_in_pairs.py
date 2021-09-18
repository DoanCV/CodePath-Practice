"""
Exactly like reverse nodes in k group where k = 2
"""

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head

        curr = head
        prev = None
        while True:
            end_of_pre_sublist = prev
            end_of_new_sublist = curr

            i = 0
            while i < 2 and curr is not None:
                temp = curr.next
                curr.next = prev

                prev = curr
                curr = temp
                i += 1

            if end_of_pre_sublist is not None:
                end_of_pre_sublist.next = prev
            else:
                head = prev

            end_of_new_sublist.next = curr

            if curr is None:
                break

            prev = end_of_new_sublist

        return head
