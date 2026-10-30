class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head):
        temp = head
        while temp is not None and temp.next is not None:
            if temp.val == temp.next.val:
                temp.next = temp.next.next
            else:
                temp = temp.next

        return head
head = ListNode(1)
head.next = ListNode(1)
head.next.next = ListNode(2)
head.next.next.next = ListNode(3)
head.next.next.next.next = ListNode(3)
obj = Solution()
head = obj.deleteDuplicates(head)
# Print the linked list
temp = head
while temp is not None:
    print(temp.val, end=" -> ")
    temp = temp.next

print("None")
