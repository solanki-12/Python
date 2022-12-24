from tkinter import*


top = Tk()

lb1 = Listbox(top)
lb1.insert(1, 'Python')
lb1.insert(2, 'Perl')
lb1.insert(3, 'C')
lb1.insert(4, 'Php')
lb1.insert(5, 'JSP')
lb1.insert(6, 'Ruby')

# lb1.delete(1,3)

lb1.pack()
top.mainloop()