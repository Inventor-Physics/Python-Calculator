#I hope you have alreaady installed Python and with it you have installed Tkinter
#and if you haven't then copy this link and paste it in your web browser https://www.youtube.com/watch?v=GwCZ2KElNdw
#I hope you enjoy
#Keep Learning


from tkinter import *

root = Tk()
root.title("Calculator")#changes title of GUI

e = Entry(root, width= 35,fg = "black", bg = "white",borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx = 1, pady = 10)#it adds a coloumn span of 3
e.get()

def button_add(number):
    current = e.get()
    e.delete(0, END)#delete everything in the input box
    e.insert(0,str(current) + str(number)) #it will show the number in the enrty/input box

def button_CLEAR():
    e.delete(0, END)

def button_ADD():
    first_number= e.get()
    global f_n 
    global math
    math = "addition"
    f_n = int(first_number)
    e.delete(0, END)

def button_EQUAL():
    second_number = e.get()
    e.delete(0, END)
    if math== "addition":
        e.insert(0, f_n + int(second_number))
    if math == "subtraction":
        e.insert(0, f_n - int(second_number))
    if math=="division":
        e.insert(0, f_n / int(second_number))
    if math=="multiplication":
        e.insert(0, f_n * int(second_number))

def button_sub():
    first_number= e.get()
    global f_n 
    global math
    math = "subtraction"
    f_n = int(first_number)
    e.delete(0, END)

def button_mult():
    first_number= e.get()
    global f_n 
    global math
    math = "multiplication"
    f_n = int(first_number)
    e.delete(0, END)

def button_div():
    first_number= e.get()
    global f_n 
    global math
    math = "division"
    f_n = int(first_number)
    e.delete(0, END)
        
button1 = Button(root, text="1", padx = 30, pady = 15, command=lambda: button_add(1), bg="Grey")
button2 = Button(root, text="2", padx = 30, pady = 15, command=lambda: button_add(2), bg="Grey")
button3 = Button(root, text="3", padx = 30, pady = 15, command=lambda: button_add(3), bg="Grey")
button4 = Button(root, text="4", padx = 30, pady = 15, command=lambda: button_add(4), bg="Grey")
button5 = Button(root, text="5", padx = 30, pady = 15, command=lambda: button_add(5), bg="Grey")
button6 = Button(root, text="6", padx = 30, pady = 15, command=lambda: button_add(6), bg="Grey")
button7 = Button(root, text="7", padx = 30, pady = 15, command=lambda: button_add(7), bg="Grey")
button8 = Button(root, text="8", padx = 30, pady = 15, command=lambda: button_add(8), bg="Grey")
button9 = Button(root, text="9", padx = 30, pady = 15, command=lambda: button_add(9), bg="Grey")
button0 = Button(root, text="0", padx = 30, pady = 15, command=lambda: button_add(0), bg="Grey")

button_addition = Button(root, text="+", padx = 30, pady = 15, command=button_ADD, bg="Grey")
button_subtraction = Button(root, text="-", padx = 30, pady = 15, command=button_sub, bg="Grey")
button_division = Button(root, text="÷", padx = 30, pady = 15, command=button_div, bg="Grey")
button_multiplication = Button(root, text="x", padx = 30, pady = 15, command=button_mult, bg="Grey")
button_equals = Button(root, text="=", padx = 30, pady = 15, command=button_EQUAL, bg="orange")

button_clear = Button(root, text="C", padx = 30, pady = 15, command=button_CLEAR, bg="gray")
button_clear1 = Button(root, text="CE", padx = 25, pady = 15, command=button_CLEAR, bg="gray")

button1.grid(row=1,column=0)
button2.grid(row=1,column=1)
button3.grid(row=1,column=2)
button4.grid(row=2,column=0)
button5.grid(row=2,column=1)
button6.grid(row=2,column=2)
button7.grid(row=3,column=0)
button8.grid(row=3,column=1)
button9.grid(row=3,column=2)
button0.grid(row=4,column=1)

button_addition.grid(row=4, column=3)
button_subtraction.grid(row=1, column=3)
button_equals.grid(row=5, column=1)
button_multiplication.grid(row=2, column=3)
button_division.grid(row=3, column=3)

button_clear.grid(row=4, column=0)
button_clear1.grid(row=4, column=2)


root.mainloop()
