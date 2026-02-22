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
    return head      # return head

def printlist(head):
    temp = head
    while temp:
        print(temp.data, "-->", end=" ")
        temp = temp.next


# input: 1 2 3 4 5 
arr = list(map(int, input().split()))

head = createLinkedList(arr)   # store head
printlist(head)                # print list

#output:
    # 1 2 3 4 5
    
    #1 --> 2 --> 3 --> 4 --> 5 --> 