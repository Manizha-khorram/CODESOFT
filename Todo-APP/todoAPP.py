from tkinter import *

root = Tk()
root.title('Todo APP')
root.geometry('500x500')


#Create frame
myFrame = Frame(root)
myFrame.pack(pady = 10)

#Created listbox
myList = Listbox(myFrame,
     width=25,
     height= 5,
     bg="SystemButtonFace",
     bd=0,
     fg="black",           
     highlightthickness= 0,
     selectbackground="#a6a6a6" ,
     activestyle='none',           
                 )

myList.pack(side=LEFT , fill= BOTH)

stuff = ['Take a Nap', "learn tkinter", 'Buy Groceries']

for item in stuff:
    myList.insert(END, item)

#Created scrollbar
myScrollbar = Scrollbar(myFrame)    
myScrollbar.pack(side=RIGHT , fill= BOTH)

#Added scrollbar
myList.config(yscrollcommand= myScrollbar.set)
myScrollbar.config(command=myList.yview)


#Created entery box to add item to the list
myEntry = Entry(root, font=('Helvetica', 24))
myEntry.pack(pady = 20)

#Created a button frame
buttonFram = Frame(root)
buttonFram.pack(pady=20)

#Functions
def deleteButton():
    myList.delete(ANCHOR) #ANCHOR just delete what is highlighted!

def addButton():
    myList.insert(END, myEntry.get())
    myEntry.delete(0, END)

def crossOffButton():
    myList.itemconfig(
        myList.curselection(),
        fg= "blue"
    )
    #get rid of selection bar
    myList.select_clear(0, END)

def uncrossButton():
     myList.itemconfig(
        myList.curselection(),
        fg= "black"
    )
    #get rid of selection bar
     myList.select_clear(0, END)

def deleteCrossOffButton():
    count = 0
    while count < myList.size(): # myList.size() : size shows the num of items in the list
        if myList.itemcget(count, "fg") == "blue":   #itemcget: when we want to have info about an item
            myList.delete(myList.index(count))
        else:    
         count +=1    


#Add buttons
deleteButton = Button(buttonFram, text="Delete Item" , command=deleteButton)
addButton = Button(buttonFram, text="Add Item" , command=addButton)
crossOffButton = Button(buttonFram, text="Cross Off Item" , command=crossOffButton)
uncrossButton = Button(buttonFram, text="Uncross Item" , command=uncrossButton)
deleteCrossOffButton = Button(buttonFram, text="Delete Crossed" , command=deleteCrossOffButton)


deleteButton.grid(row=0 , column=0)
addButton.grid(row=0, column=1, padx=20)
crossOffButton.grid(row=0 , column=2)
uncrossButton.grid(row=0 , column=3, padx=10 )
deleteCrossOffButton.grid(row=0 , column=4, padx=10 )

root.mainloop()
