
class Node:

    def __init__(self,value):
        self.value = value
        self.next = None




class Stack:

    def __init__(self):
        self.top = None
        

   
    def push(self,value):
        
        if(self.top == None):
            self.top = Node(value)
        else:
            newNode = Node(value)
            newNode.next = self.top
            self.top = newNode


    def pop(self):
        if(self.top == None):
            return None
        else:
            temp = self.top
            self.top = self.top.next
            temp.next = None
            return temp.value


                

    def printStack(self):
        temp = self.top
        while(temp != None):
            print(temp.value)
            temp = temp.next





objStack = Stack()
objStack.push(5)
objStack.push(10)
objStack.pop()
objStack.printStack()



###############################################################################
    
    




