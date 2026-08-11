class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        curr = head
        res = None
        counter = 1
        start = head
        prev_tail = None

        while curr:
            if counter == k:
                counter = 0

                end = curr
                next_start = end.next

                new_head = self.reverse(start, k, end)

                if not res:
                    res = new_head
                else:
                    prev_tail.next = new_head

                prev_tail = start
                start = next_start
                curr = next_start
            else:
                curr = curr.next

            counter += 1

        return res

    def reverse(self, node, k, tail):
        curr = node
        prev = tail.next

        while k:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            k -= 1

        return prev
