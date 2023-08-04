class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # base cases
        if not list1:
            return list2
        if not list2:
            return list1
        
        # determine the head of the merged list
        if list1.val <= list2.val:
            head = list1
            list1 = list1.next
        else:
            head = list2
            list2 = list2.next
        
        # pointer to traverse the merged list
        current = head
        
        # merge the lists
        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        
        # append the remaining nodes of list1 or list2
        if list1:
            current.next = list1
        else:
            current.next = list2
        
        return head
