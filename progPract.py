# sets provide the facility to perform logical operation that are:

# 1) Union 
# 2) Intersection

"""set1 = {"Anuj","solanki","python",200,"solanki"}
set2 = {"learning","Java","python",200}

population = set1.union(set2)
print(population)

population = set1|set2
print(population)


"""






"""   INTERSECTION OPERATION USING SET ---> this can be done using intersection() or & operatior """
"""

testunion = set2.intersection(set1)
print(testunion)


testunion = set2&set1
print(testunion)

"""




"""  Dictionary """
'''
dict ={'Name':'christ University','Branch':'Computational Science'}

print(dict.keys())
print(dict.get('Name'))
print(dict.values())

dict['place']="Delhi-NCR"
print(dict.items())'''


"""   LIST functions """

# list1 = [1,4,3,2,"solanki","Anuj"]



# Adding element in the list
'''
list1.append(5)
print(list1)
'''

# Adding tuple in the list
'''
list1.append((2,3))
print(list1)
'''


# Spliting the string
'''
String1 = "learning Python"
lst = String1.split()
print("the list is :",lst)
'''

# insert method is similar like append method but insert method takes two arguement(position,value).
'''
list1.insert(5,"Python")
print(list1)
'''

# It will extend the list into another list
'''
list1.extend(["New delhi","Thailand","Japan"])
print(list1)
'''

#It will reverse the whole list

'''
list1.reverse()
print(list1)


list1.remove(5)
print(list1)
'''

# for i in range(1,2):
#     list1.remove(i)
# print(list1)






# odd_square = []

# for x in range(1,11):
#     if x % 2 == 1:
#         odd_square.append(x**2)


# print(odd_square)        












""" CONCEPT OF OOPS IN PYTHON """


# class Dog:

#     #class Variable
#     animal = "dog"

    

#     def __init__(self,breed,color):
        
#         #instance Variable
#         self.breed = breed
#         self.color = color




# class Cat:

#     pettype = "cat"

#     def __init__(self,breed,color):
#         self.breed = breed
#         self.color = color

#     def getColor(self):
#         return self.color


# #Objects of the class Test

# roger = Dog("Siberian huskiy","white and black")

# print("roger is a :",roger.animal)
# print("roger breed is: ",roger.breed)
# print("roger color is :",roger.color)


# print("\n")
# melon = Cat("pomelian","white")
# print("Melon is :",melon.pettype)
# print("Melon breed is :",melon.breed)
# print("Melon color is :",melon.color)



# #Get color of the animal

# print(melon.getColor())




### LAMDA FUNCTION ####
"""
divide = lambda x,y : x/y
print(divide(10,5))

def myFunc(n):
    return lambda a: a*n


x = myFunc(5)
print(x(5))"""


## MAP FUNCTION ##
"""
def myFunc(n):
    return n*n

num =(1,2,3,4,5,6)
result = map(myFunc,num)

## Creting Map object ##
output = list(result)
print(output)
"""


######## Filter() Function ############

"""
def mineFunc(var):
    letters = ['a','b','d','e','g']
    if var in letters:
        return True
    else:
        return False



char = ['a','c','d','e','g']
filtered = filter(mineFunc,char)  

print("filtered letters are :")
for s in filtered:
    print(s)"""



## REGEX ####
"""
import re

sequence = "Learning java is more enoyable inJava than python"

x = re.findall("in",sequence)


if x:
    print("Yes we have a match")
else:
    print("No we don't have a match")    

print(x)"""






### GUI PROGRAM ####

"""import tkinter
from tkinter import Label, Menu,Listbox,messagebox,Button

root = tkinter.Tk()
root.title("HAngout Corner")
root.geometry("500x500")
"""

"""
lbl = Label(root,text="---- Food Corner ----", bd=3, bg="Lightgrey",width=15,font="Helvetica")

menubar = Menu(root)


file = Menu(menubar,tearoff=0)
menubar.add_cascade(label="Items",menu=file)
file.add_command(label='chilli potato', command=None)
file.add_command(label="Exit",command=root.destroy)

file.add_separator()


edit = Menu(menubar,tearoff=0)
menubar.add_cascade(label="Edit",menu=edit)

help = Menu(menubar,tearoff=0)
menubar.add_cascade(label="help",menu=help)


lstbox = Listbox(root,background="yellow",fg="black",highlightbackground="grey",highlightthickness=5, selectbackground="grey")
lstbox.insert(1,"very good")
lstbox.insert(2, "bad")


def message():
    messagebox.showinfo("Message ","Thank you")

button = Button(text="submit",command=message,width=10,bg="grey")    
    
root.config(menu=menubar)


button.pack()
lstbox.pack()
lbl.pack()
root.mainloop()"""




### GUI FOR CREATING TABLE ###


"""from tkinter import *

class Table:

    def __init__(self,root):

        for i in range(total_rows):
            for j in range(total_columns):

                self.e = Entry(root,width=20,fg="blue",font=('Arial',18,'bold'))
                self.e.grid(row=i,column=j)
                self.e.insert(END,lst[i][j])


lst = [(1,'Raj','Mumbai',19),
       (2,'Aaryan','Pune',18),
       (3,'Vaishnavi','Mumbai',20),
       (4,'Rachna','Mumbai',21),
       (5,'Shubham','Delhi',21)]

total_rows = len(lst)
total_columns = len(lst[0])

root=Tk()
t=Table(root)
root.mainloop()"""





##### BASICS OF NUMPY ARRAY #####

"""import numpy as np

arr = np.array([[1,2,3,4],[5,0,7,8]])
print(arr)


print("sum of columns :",np.sum(arr,axis=0))
print("sum of rows :",np.sum(arr,axis=1))


print("min function :",np.min(arr))
print("zero function :",np.zeros((5,3),dtype=int))
print("eye function :",np.eye(4,4,k=-2))
print("ones function :",np.ones([4,4],dtype=int))
print("argmax function :",np.argmax(arr,axis=1))


print("Size of array :",arr.size)
print("Shapr of the Array :",arr.shape)
print("Dimension of the Array :",arr.ndim)

print("Change the shape of array :",arr.reshape(8))"""

### --------------- FIND THE NUMBER DIVISIBLE BY 7  ----------- ####


"""import numpy as np
arr = []
for x in (np.arange(50,100)):
    if (x%7==0):
        arr.append(str(x))
print("Number divisible by 7 :",arr)
"""



## ------ BOOLEAN MASKING ------#####

import numpy as np

"""x = np.array([3,4,6,10,24,28,27,43,52,12,53,77,78])

print(x%3!=0)
print(x%5==0)
print(x%3==0,x%5==0)
x[x%3==0]=42
print(x)
"""



## Shoping Store operations ###

"""
arr = np.array([(44,'cranberry',40.0),(22,'tigercrunch',600.0),(55,'AC',900.0)],dtype=[('itemcode','i4'),('itemname','S15'),('itemprice','f4')])
print(arr)

print(arr['itemname'])

print(arr[arr['itemprice']>500])

print(arr[0:2])"""



### ---------------------- PANDAS Series-----------------#####

# import pandas as pd
# import numpy as np

"""data = ['Anuj','solanki','deepak','kumar']
s = pd.Series(data,index=[1,2,3,4])
print(s)
"""

# data2= {'name':'solanki','age':24,'place':'vaishali'}
# sr = pd.Series(data2,index=['name','age','place'])
# print(sr)



"""
data3 = np.array(['a','b','c','d'])
ser = pd.Series(data3,index=[11,12,13,14])
print(ser)

"""


# data4 = pd.Series(['h','y','l','e'],index=[20,21,22,23])
# print(data4)



##### ---------------------  DATAFRAME -------------###

# 1) dataFrame using the list
"""
data1 = ['apple','banana','mango','lichi']
place = ['india','china','afganistan','england']
price = [20,90,120,87]
d1 = pd.DataFrame(list(zip(data1,place,price)),columns=["fruits","country","Price"])
print(d1)
"""

# 2) DataFrame using the Dictionary

"""
data2 = {'fruits':['apple','banana','papaya'],'code':[22,43,53],'price':[24,53,120]}
d2 = pd.DataFrame(data2,index=[12,13,14])
print(d2)
"""


# 3) DataFrame using the Array
"""
data3 = np.array(['Anuj','solanki','learning','java'])
ds = pd.DataFrame(data3,columns=["details"])
print(ds)

"""


# data4 = pd.DataFrame(['a','b','c','d'],columns=['alphabet'])
# print(data4)



### EXCEL file in DATAFRAME ####

"""import pandas as pd

data = pd.read_excel(r'D:\SEMESTER 5\Python Lab\testfile.xlsx')
df = pd.DataFrame(data,columns=['hii','bye','tata'])
print(df)
"""





