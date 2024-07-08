from tkinter import *

root = Tk()
display = Entry(root, width=60)
display.grid(row=1, column=0, columnspan=6, )

counter = 1

for x in range(3):
    for y in range(3):
        button = Button(root, text = counter, width=20, height=2)
        counter +=1
        button.grid(row=x+2, column=y)

button = Button(root, text = '0', width=20, height=2)
button.grid(row=5, column = 1)

op_count = 0
operations = ['+','-','*','/','*3.14','%','(','**',')','**2']
for x in range(4):
    for y in range (3):
        if op_count <len(operations):
            button = Button(root, text=operations[op_count], width=10, height=2)
            op_count += 1
            button.grid(row = x+2, column = y+3)



root.mainloop()