from OOPS.LinkedList.LinkedListNode import LinkedListNode  # Ensure correct import
def printLinkedList(head):
    temp = head
    while(temp!= None):
        print(temp.data,"==>", end=" ")
        temp = temp.next

def createLinkedList(list):
    head = LinkedListNode(list[0])
    temp = head
    for i in range(1,len(list)):
        temp.next = LinkedListNode(list[i])
        temp = temp.next
    return head

def RotateRight(head, k):
    if(head is None):
            return head
    if(k == 0):
        return head
    rightPtr = head
    leftPtr = head
    startPtr = head

    count = 0

    while(rightPtr != None):
        count+=1
        rightPtr = rightPtr.next

    rightPtr = head

    if(count<k):
        k = k % count

    if(k == count or count == 1 or k == 0):
        return head
    i= 0

    while(i<k):
        rightPtr = rightPtr.next
        i+=1


    while(rightPtr.next != None):
        rightPtr = rightPtr.next
        leftPtr = leftPtr.next

    head = leftPtr.next
    leftPtr.next = None
    rightPtr.next = startPtr

    return head


def getCount(head):
    temp = head
    count = 0
    while(temp!=None):
        count+=1
        temp=temp.next
    return count

def searchLinkedList(head,x):
    temp = head
    while(temp!=None):
        if(temp.data == x):
            return True
        temp = temp.next
    return False

def deleteNode(head, pos):
    if(pos==1):
        return head.next
    temp = head
    count = 1
    while(count < pos-1):
        temp = temp.next
        count+=1
    if(temp.next!=None):
        temp.next = temp.next.next
    return head

def isSorted(head):
    if not head or not head.next:
        return 1  # A single-node or empty list is considered sorted

    increasing = decreasing = True
    temp = head

    while temp.next:
        if temp.data < temp.next.data:
            decreasing = False
        elif temp.data > temp.next.data:
            increasing = False
        temp = temp.next

    return 1 if increasing or decreasing else 0

def getKthFromLast(head, k):
    temp = head
    count = 0
    while(temp):
        temp = temp.next
        count+=1
    temp = head
    if(count - k < 0):
        return -1

    steps = count - k
    while(steps > 0):
        temp = temp.next
        steps -= 1

    return temp.data

# two pointers approach

def getKthFromLast(head, k):
    first = second = head

    while(k-1>0):
        if(first):
            return -1
        first = first.next
        k-=1

    while(first.next != None):
        first = first.next
        second = second.next

    return second.data


def removeDuplicates(head):
    temp = head
    while(temp.next!=None):
        if(temp.data == temp.next.data):
            temp.next = temp.next.next
        else:
            temp = temp.next
    return head

def areIdentical(head1, head2):
    while(head1 != None and head2 != None):
        if(head1.data != head2.data):
            return False
        head1 = head1.next
        head2 = head2.next

    if(head1 != None or head2 != None):
        return False

    return True


def insertInMiddle( head, x):
    #code here
    if head is None:
        head = LinkedListNode(x)
        return head

    temp = head
    middle = getMiddleElement(temp)
    var = middle.next
    middle.next = LinkedListNode(x)
    middle.next.next = var
    return head


def getMiddleElement(head):
    slow = head
    fast = head
    while(fast.next != None and fast.next.next!=None):
        fast = fast.next.next
        slow = slow.next
    return slow

def insertAtPosition(head, pos, data):
    temp = head
    for i in range(0, pos-1):
        i+=1
        if(temp.next == None):
            return head
        temp = temp.next



    nextNode = temp.next
    temp.next = LinkedListNode(data)
    temp.next.next = nextNode

    return head

def insertInSorted(head,data):
    temp = head
    if(head.data >= data):
        newNode = LinkedListNode(data)
        head = newNode
        head.next = temp
        return head

    while(temp.next !=None):
        if(temp.next.data > data):
            break
        temp = temp.next
    nextNode = temp.next
    temp.next = LinkedListNode(data)
    temp.next.next = nextNode

    return head

def deleteTail(head):
    #code here
    temp = head
    while(temp.next.next!=None):
        temp = temp.next
    temp.next = None
    return head

def reverseList(head):
    if not head:
        return None

    prev = None
    curr = head
    forward = curr.next

    while forward:
        curr.next = prev
        prev = curr
        curr = forward
        forward = forward.next

    curr.next = prev
    return curr

def palindromeLinkedList(head):
    temp = head
    middle = getMiddleElement(temp)
    reverseHead = reverseList(middle)
    middle.next = None
    while(temp!=None):
        print(temp.data, reverseHead.data)
        if(temp.data != reverseHead.data):
            return False
        temp = temp.next
        reverseHead = reverseHead.next
    return True

# 92. Reverse Linked List II



def modifiedList(nums, head):
    numsSet = set(nums)
    curr = head
    while curr is not None and curr.next != None:
        if curr.next.data in numsSet:
            curr.next = curr.next.next
            continue
        curr = curr.next

    if head.data in numsSet:
        head = head.next

    return head

def removeNodes(head):
    curr = head
    reversedHead = reverseList(curr)
    curr = reversedHead
    highest = float("-inf")
    prev = None
    while curr:
        if(curr.data < highest):
            prev.next = curr.next
        else:
            highest = curr.data
            prev = curr
        curr = curr.next
    return reverseList(reversedHead)


#still in progress
def reverseBetween(head, left, right):
    if not head or left == right:
        return head

    startNode = LinkedListNode(-1)
    startNode.next = head
    prev = startNode
    curr = head

    for i in range(left - 1):
        prev = curr
        curr = curr.next

    start = curr

    for j in range(abs(right - left) + 1): 
        nextNode = curr.next
        curr.next = prev
        prev = curr
        curr = nextNode
    
    start.next = curr
    if left > 1:
        prev_left = startNode
        for _ in range(left - 1):
            prev_left = prev_left.next
        prev_left.next = prev 
    else:
        startNode.next = prev 


    return startNode.next

def pairSum(head):
    if not head or not head.next:
        return 0
    temp = head

    middle = getMiddleElement(temp)
    nextElement = middle.next
    middle.next = None
    reversedList = reverseList(nextElement)
    highestElement = 0
    while(temp!=None):
        pair = reversedList.data + temp.data
        if(highestElement < pair):
            highestElement = pair
        reversedList = reversedList.next
        temp = temp.next            
    return highestElement


def pairSumStack(head):
    if not head or not head.next:
        return 0
    temp = head

    stack = []

    middle = getMiddleElement(temp)
    nextElement = middle.next
    middle.next = None

    while nextElement is not None:
        stack.append(nextElement.data)
        nextElement = nextElement.next         

    maxElement = float("-inf")
    print(stack)

    while(len(stack) > 0):
        data =  stack.pop() + temp.data 
        if(data > maxElement):
            maxElement = data
        temp = temp.next

    return maxElement


head = createLinkedList([5,4,2,1])
print(pairSumStack(head))