# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        start=head
        previous = None 

        while start:
            next_node= start.next
            start.next=previous 

            previous = start
            start=next_node

            head=previous
        return previous    
        