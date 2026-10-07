# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        def countNode(head):
            current = head
            count = 0
            while current:
                count += 1
                current = current.next
            return count
        
        count = countNode(head)
        if count == 1 or count == n:
            return head.next
        
        node = head
        while count != n+1:
            count = count - 1
            node = node.next
        
        node.next = node.next.next

        return head
