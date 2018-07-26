'''
 Linked list created by vandhiadevan
 '''
from math import ceil

 
class SingleLinkedList:
    def __init__(self):
        self.data = None
        self.next = None
        
def InitNode(head,value):
    head.data = (value)
    head.next = None
    
def Addnode(head,value):
    temp = SingleLinkedList()
    temp.data = (value)
    temphead = head
    if head.next is None:
        head.next = temp
    else:
        while temphead.next is not None:
            temphead = temphead.next
    temphead.next = temp
    
def deletenode(head,value):
    if head.next is None and head.data == value:
        head = None
    
    temp = head
    
    while temp is not None or temp.data != value:
        prev = temp
        temp = temp.next
        prev = prev
    
    if temp == head:
        head = head.next
        return
    else:
        prev.next = temp.next
        return
    
def swap(first, second):
    value = first.data
    first.data = second.data
    second.data = value
    
def sort(head):
    temp = head
    while temp is not None:
        if temp.next is None:
            break
        
        first = int(temp.data)
        second = int(temp.next.data)
        
        if first < second:
            temp.data = second
            temp.next.data = first

        temp = temp.next

    

        