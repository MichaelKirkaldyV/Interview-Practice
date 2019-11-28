class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
     
 
class LinkedList:
    def __init__(self, head=None):
        self.head = head
        self.size = 0

    def insertNode(self, value):
       node = Node(value)
       if self.head is None:
           self.head = node
           return
       else:
           currentNode = self.head
           while currentNode:
               if currentNode.next is None:
                   currentNode.next = node
                   break
               else:
                   currentNode = currentNode.next
       
    def printList(self):
       currentNode = self.head
       while currentNode:
           print(currentNode.value)
           currentNode = currentNode.next

    def detectLoop(self):
       new_set = set()
       if not self.head:
           return None
       else:
           currentNode = self.head
           while currentNode:
               if currentNode in new_set:
                   return True
               else:
                    new_set.add(currentNode)
                    currentNode = currentNode.next
           return False


new_llist = LinkedList()
new_llist.insertNode(50)
new_llist.insertNode(33)
new_llist.insertNode(2)
new_llist.insertNode(111)
new_llist.printList()
print(new_llist.detectLoop())






