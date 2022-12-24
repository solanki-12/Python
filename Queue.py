from multiprocessing.sharedctypes import Value
import re


# class Node:

#     def __init__(self,value):
#         self.value = value
#         self.next = None




# class Queue:

#     def __init__(self):
#         self.first = None
#         self.last = None


#     def enqueue(self,value):
#         newNode = Node(value)
#         if(self.first == None):
#             self.first = newNode
#             self.last = newNode
#             return
#         self.last.next = newNode
#         self.last = newNode


#     def dequeue(self):
#         temp = self.first
#         if(self.first == None):
#             return None

#         if(self.first == None):
#             self.first = None
#             self.last = None    
#         else:
#             self.first = self.first.next
#             temp.next = None


#     def printQ(self):
#         temp = self.first
#         while(temp != None):
#             print(temp.value,"->", end=" ")
#             temp = temp.next




# objQ = Queue()
# objQ.enqueue(5)
# objQ.enqueue(15)
# objQ.dequeue()

# objQ.printQ()





#############################################################













