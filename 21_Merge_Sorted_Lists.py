class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #if one is empty return the other
        #if both empty return empty ListNode
        list3 = dummy = ListNode()
        while list1 and list2:
            #if l1 < l2 append l1 to l3
            if list1.val < list2.val:
                list3.next = list1
                list1 = list1.next
            #if l2 > l1 append l2 to l3
            #if equal append l2 to l3 
            else:
                list3.next = list2
                list2 = list2.next
            #moving list3 to the next node
            list3 = list3.next
            #if one is empty return the other
        if list1:
            list3.next = list1
        else:
            list3.next = list2
        return dummy.next