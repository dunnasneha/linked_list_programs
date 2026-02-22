class Node:
    def __init__(self, val):
        self.data = val
        self.next = None


def createLinkedList(arr):
    head = None
    for val in arr:
        if head is None:
            head = Node(val)
            temp = head
        else:
            temp.next = Node(val)
            temp = temp.next
    return head   # return head node


def middleNode(head):
    slow = head
    fast = head

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

    return slow


# INPUT: 1 2 3 4 5
#output:mid_value: 3
arr = list(map(int, input().split()))

head = createLinkedList(arr)
mid = middleNode(head)              

print("mid_value:",mid.data)                     