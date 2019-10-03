# importing the tkinter module 
from tkinter import *

# the function to be called when the user click any numbers or operators
def btnClick(fromButtons):
    global operator
    operator = operator + str(fromButtons)
    text_input.set(operator)

# the function to be called when the user click C button to clear 
def btnClear():
    global operator
    operator = ""
    text_input.set("")

# the function to be called when the user click Equal to
def btnEquals():
    global operator
    sumup = str(eval(operator))
    text_input.set(sumup)
    operator = ""


cal = Tk()
cal.title("Standard Calculator")
operator = ""
text_input = StringVar()

txtDisplay = Entry(cal, font=('arial', 20, 'bold'), textvariable=text_input, bd=30, insertwidth=4,
                   bg="light blue", justify='right').grid(columnspan=4)

#====================================== Number Buttons ================================================================


btn0 = Button(cal, padx=16, pady=13, bd=8, fg='black', font=('arial', 20, 'bold'), text='0', bg="light blue", command=lambda:btnClick(0)).grid(row=4, column=0)
btn1 = Button(cal, padx=16, pady=13, bd=8, fg='black', font=('arial', 20, 'bold'), text='1', bg="light blue", command=lambda:btnClick(1)).grid(row=3, column=0)
btn2 = Button(cal, padx=16, pady=13, bd=8, fg='black', font=('arial', 20, 'bold'), text='2', bg="light blue", command=lambda:btnClick(2)).grid(row=3, column=1)
btn3 = Button(cal, padx=16, pady=13, bd=8, fg='black', font=('arial', 20, 'bold'), text='3', bg="light blue", command=lambda:btnClick(3)).grid(row=3, column=2)
btn4 = Button(cal, padx=16, pady=13, bd=8, fg='black', font=('arial', 20, 'bold'), text='4', bg="light blue", command=lambda:btnClick(4)).grid(row=2, column=0)
btn5 = Button(cal, padx=16, pady=13, bd=8, fg='black', font=('arial', 20, 'bold'), text='5', bg="light blue", command=lambda:btnClick(5)).grid(row=2, column=1)
btn6 = Button(cal, padx=16, pady=13, bd=8, fg='black', font=('arial', 20, 'bold'), text='6', bg="light blue", command=lambda:btnClick(6)).grid(row=2, column=2)
btn7 = Button(cal, padx=16, pady=13, bd=8, fg='black', font=('arial', 20, 'bold'), text='7', bg="light blue", command=lambda:btnClick(7)).grid(row=1, column=0)
btn8 = Button(cal, padx=16, pady=13, bd=8, fg='black', font=('arial', 20, 'bold'), text='8', bg="light blue", command=lambda:btnClick(8)).grid(row=1, column=1)
btn9 = Button(cal, padx=16, pady=13, bd=8, fg='black', font=('arial', 20, 'bold'), text='9', bg="light blue", command=lambda:btnClick(9)).grid(row=1, column=2)


#======================================== Operator buttons ============================================================

Add = Button(cal, padx=16, pady=13, bd=8, fg='black', font=('arial', 20, 'bold'), text='+', bg="light blue", command=lambda:btnClick('+')).grid(row=1, column=3)
Sub = Button(cal, padx=16, pady=13, bd=8, fg='black', font=('arial', 20, 'bold'), text='-', bg="light blue", command=lambda:btnClick('-')).grid(row=2, column=3)
Mlt = Button(cal, padx=16, pady=13, bd=8, fg='black', font=('arial', 20, 'bold'), text='*', bg="light blue", command=lambda:btnClick('*')).grid(row=3, column=3)
Div = Button(cal, padx=16, pady=13, bd=8, fg='black', font=('arial', 20, 'bold'), text='/', bg="light blue", command=lambda:btnClick('/')).grid(row=4, column=3)

btnClear = Button(cal, padx=16, pady=13, bd=8, fg='black', font=('arial', 20, 'bold'), text='C', bg="light blue", command= btnClear).grid(row=4, column=1)
btnEqual = Button(cal, padx=16, pady=13, bd=8, fg='black', font=('arial', 20, 'bold'), text='=', bg="light blue", command=btnEquals).grid(row=4, column=2)


cal.mainloop()