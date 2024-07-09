from tkinter import *
i = 0

root = Tk()
def get_number(num):
    global i
    display.insert(i,num)
    i+=1


display = Entry(root, width=60)
display.grid(row=1, column=0, columnspan=6, )

numbers = [1,2,3,4,5,6,7,8,9]
counter = 0

for x in range(3):
    for y in range(3):
        button_text = numbers[counter]
        button = Button(root, text = button_text, width=20, height=2, command = lambda x = button_text:get_number(x))
        counter +=1
        button.grid(row=x+2, column=y)

button = Button(root, text = '0', width=20, height=2,command = lambda: get_number(0))
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