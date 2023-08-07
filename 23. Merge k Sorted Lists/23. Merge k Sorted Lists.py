import heapq

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
      
        for head in lists:
            if head:
                heapq.heappush(heap, (head.val, id(head), head))

        dummy = ListNode(0)
        curr = dummy

        while heap:

            _, _, node = heapq.heappop(heap)

            curr.next = node
            curr = curr.next

            if node.next:
                heapq.heappush(heap, (node.next.val, id(node.next), node.next))
        
        return dummy.next
