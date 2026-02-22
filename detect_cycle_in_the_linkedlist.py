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
    return head


def detectloop(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return slow
    return None


def findCycleStart(head):
    meet = detectloop(head)
    if meet is None:
        return None

    start = head
    while start != meet:
        start = start.next
        meet = meet.next
    return start


def printCycle(head):
    start = findCycleStart(head)

    if start is None:
        print("No cycle")
        return

    temp = start
    while True:
        print(temp.data, end=" ")
        temp = temp.next
        if temp == start:
            break


arr = list(map(int, input().split()))
head = createLinkedList(arr)

temp = head
while temp.next:
    temp = temp.next

temp.next = head.next.next

print("cycle values:")
printCycle(head)