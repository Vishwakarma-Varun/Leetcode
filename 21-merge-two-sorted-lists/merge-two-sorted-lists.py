# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        if list1 == None and list2 == None :
            return None
        if list1 == None and list2 != None:
            head = list2
        elif list1 != None and list2 == None:
            head = list1
        else:
            current = list1 
            while current.next:
                current = current.next
            current.next = list2
            head = list1
        ans = []
        current = head
        while current:
            ans.append(current.val)
            current = current.next
        
        ans.sort()
        current = head
        i = 0
        while current:
            current.val = ans[i]
            current = current.next
            i = i + 1
        
        return head
