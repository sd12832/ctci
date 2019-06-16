from LinkedList import *
import unittest

# find the intersection of the two lists
def find_intersection(list1, list2):

    difference = find_difference(list1, list2)

    if len(list1) > len(list2):
        current = list1.head
        for i in range(difference):
            list1.head = current.next
            current = list1.head
    else:
        current = list2.head
        for i in range(difference):
            list2.head = current.next
            current = list2.head

    while list1.head:
        current1 = list1.head
        current2 = list2.head

        if str(current1) == str(current2):
            return current1

        if list1.head.next:
            list1.head = current1.next
            list2.head = current2.next

        else:
            return None

# Find the difference in lengths between two lists
def find_difference(list1, list2):
    return abs(len(list1) - len(list2))

class TestLL(unittest.TestCase):

    def test_tail_case(self):

        # Generate the first linked list
        ll1 = LinkedList()
        ll1.generate(7, 0, 99)

        # Generate the second linked list
        ll2 = LinkedList()
        ll2.generate(10, 0, 99)

        new_node = LinkedListNode(125)

        print('Address of new node is: ' + hex(id(new_node)))

        ll1.add(new_node)
        ll2.add(new_node)

        self.assertEqual(hex(id(find_intersection(ll1, ll2))), hex(id(new_node)))

    def test_head_case(self):

        # Generate the first linked list
        ll1 = LinkedList()
        ll1.generate(10, 0, 99)

        # Generate the second linked list
        ll2 = LinkedList()
        ll2.generate(15, 0, 99)

        new_node = LinkedListNode(125)

        ll1_prev_head = ll1.head
        ll1.head = new_node
        ll1.head.next = ll1_prev_head

        ll2_prev_head = ll2.head
        ll2.head = new_node
        ll2.head.next = ll2_prev_head

        self.assertEqual(hex(id(find_intersection(ll1, ll2))), hex(id(new_node)))

    def test_middle_case(self):

        new_node = LinkedListNode(125)

        # Constructing the first list
        ll1_a = LinkedList()
        ll1_a.generate(10, 0, 99)
        ll1_b = LinkedList()
        ll1_b.generate(5, 0, 99)

        ll1_a_prev_tail = ll1_a.tail
        ll1_b_prev_head = ll1_b.head

        ll1_a.tail = new_node
        ll1_b.head = new_node

        ll1_a_prev_tail.next = ll1_a.tail
        ll1_b.head.next = ll1_b_prev_head

        # Constructing the second list
        ll2_a = LinkedList()
        ll2_a.generate(15, 0, 99)
        ll2_b = LinkedList()
        ll2_b.generate(2, 0, 99)

        ll2_a_prev_tail = ll2_a.tail
        ll2_b_prev_head = ll2_b.head

        ll2_a.tail = new_node
        ll2_b.head = new_node

        ll2_a_prev_tail.next = ll2_a.tail
        ll2_b.head.next = ll2_b_prev_head

        #testing
        self.assertEqual(hex(id(find_intersection(ll1_a, ll2_a))), hex(id(new_node)))

if __name__ == '__main__':
    unittest.main()