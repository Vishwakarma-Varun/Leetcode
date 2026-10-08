# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode | None) -> bool:
        value = ""
        current = head
        while current:
            value = value + str(current.val)
            current = current.next
        return value == value[::-1]