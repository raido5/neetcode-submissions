class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        prev = None
        curr = head

        while curr is not None:
            nextt = curr.next   # sauvegarder le suivant
            curr.next = prev    # inverser le lien
            prev = curr         # avancer prev
            curr = nextt        # avancer curr

        return prev