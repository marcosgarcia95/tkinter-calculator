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
root.mainloop()