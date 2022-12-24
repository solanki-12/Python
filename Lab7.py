

class Stack:

    def __init__(self):
        self.top = None
        self.height = None

    class Node:
            
        def __init__(self,value):
            self.value = value
            self.next = None

    def push(self,value):
        newNode = Node(value)
        
        if(self.top == None):
            self.top = newNode
        else:
            newNode.next = self.top
            self.top = newNode
            self.height = 1

    def printStack(self):
        temp = self.top
        while(temp != None):
            print(temp.value)
            temp = temp.next






obj = Stack(2)
obj.push(5)
obj.printStack()
