class Node:
    def __init__(self, val):
        self.data = val
        self.next = None


# Create Linked List
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


# Detect length of cycle
def detectlengthofcycle(head):
    slow = head
    fast = head

    # Step 1: Detect meeting point
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:

            # Step 2: Find start of cycle
            fast = head
            while slow != fast:
                slow = slow.next
                fast = fast.next

            # Step 3: Count cycle length
            fast = fast.next
            count = 1
            while slow != fast:
                fast = fast.next
                count += 1

            return count

    return 0



arr = list(map(int, input().split()))   # Example: 1 2 3 4 5
head = createLinkedList(arr)

# Create cycle 
temp = head
while temp.next:
    temp = temp.next

temp.next = head.next.next

length = detectlengthofcycle(head)

print("Cycle Length:", length)