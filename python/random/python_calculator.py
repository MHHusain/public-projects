from tkinter import *
from math import *
from PIL import Image, ImageTk

# import tkinter.messagebox
# tkinter.messagebox.showinfo('this is the title', 'this is a calculator')
# question = tkinter.messagebox.askquestion('this is the title of the question', 'do you want to open the calculator')

#question = yes or no

muntathar = Tk()
muntathar.title('calculator')

image_of_delete_button = Image.open(r"C:\Users\NS\Desktop\images.png")
image_of_delete_button = image_of_delete_button.resize((50, 50), Image.ANTIALIAS)
image_of_delete_button = ImageTk.PhotoImage(image_of_delete_button)

mm = Menu(muntathar)
muntathar.config(menu=mm)
firstM = Menu(mm)
mm.add_cascade(label='File', menu=firstM)
firstM.add_command(label='New Window')

myFrame = Frame(muntathar, padx=0, pady=0)
the_entry_frame = Frame(muntathar)
the_entry_frame.grid(row=0, column=0)  # side=TOP,fill=X
myFrame.grid(row=1, column=0)  # anchor=SW,fill=Y

# an = Entry(myFrame,borderwidth=5)
# an.grid(row=0,column=6,sticky='e',ipadx=300)
eu = Entry(the_entry_frame, relief=SUNKEN, font=('', 20), width=25, borderwidth=5, fg='purple', bg='gold')
eu.grid(row=0, column=0, pady=5)
# eu.bell()
# eu.grid_configure(sticky=N)


def p(n, r):
    permutation = factorial(int(n)) / factorial(int(n - r))
    return permutation


def c(n, r):
    computation = factorial(n) / (factorial(n - r)) * factorial(r)
    return computation


def deleted(optional=''):
    cach = eu.get()[0:-1]
    eu.delete(0, END)
    eu.insert(0, cach)


def clear():
    eu.delete(0, END)

# number_of_delete = 0


def ins(number, other=''):
    the_number_now = eu.get()
    eu.delete(0, END)
    eu.insert(0, the_number_now + number)
# def ins(number,deleteP=''):
#     global number_of_delete
#     if number == "clearH":
#         eu.delete(0,END)
#     if not(number == "clearH"):
#
#         if an.get()=='':
#             pass
#         else:
#
#
#             number_of_delete += 1
#             history = an.get()
#             globals()[f'button_history{str(number_of_delete)}'] = Entry(myFrame,width=30,borderwidth=5)
#
#             exec(f"button_history{str(number_of_delete)}.grid(row={number_of_delete},column=6)")
#             exec(f"button_history{str(number_of_delete)}.insert({number_of_delete+1},{history})")
#             def delete_button():
#
#                 globals()[f'button_history{str(number_of_delete)}'].destroy()
#             globals()[f'button_history{str(number_of_delete)}clear'] = Button(myFrame,text='clear',command=delete_button)
#             exec(f"button_history{str(number_of_delete)}clear.grid(row={number_of_delete},column=7)")
#             an.delete(0,END)
#
#         the_number_now=str(eu.get())
#         if deleteP=='delete':
#             the_number_now = eu.get()[0:-1]
#         eu.delete(0,END)
#         last=str(the_number_now)+str(number)
#         eu.insert(0,last)
#     else:
#         for num in range(1,number_of_delete+1):
#                 exec(f"button_history{str(num)}.destroy()")
#


def equal():
    resolt = eval(eu.get())
    eu.delete(0, END)
    eu.insert(0, resolt)
    # if an.get()=='':
    #     an.insert(1,resolt)
    # else:
    #     an.delete(0,END)
    #     an.insert(1,resolt)

# anchor=E
# buttons____________________________________________________________________________________________________________________________________________________________


button7 = Button(myFrame, bg='yellow', text='7', relief=RIDGE, command=lambda: ins('7'), font=('bold', 20), width=3)
button8 = Button(myFrame, bg='yellow', text='8', relief=RIDGE, command=lambda: ins('8'), font=('bold', 20), width=3)
button9 = Button(myFrame, bg='yellow', text='9', relief=RIDGE, command=lambda: ins('9'), font=('bold', 20), width=3)
button4 = Button(myFrame, bg='yellow', text='4', relief=RIDGE, command=lambda: ins('4'), font=('bold', 20), width=3)
button5 = Button(myFrame, bg='yellow', text='5', relief=RIDGE, command=lambda: ins('5'), font=('bold', 20), width=3)
button6 = Button(myFrame, bg='yellow', text='6', relief=RIDGE, command=lambda: ins('6'), font=('bold', 20), width=3)
button3 = Button(myFrame, bg='yellow', text='3', relief=RIDGE, command=lambda: ins('3'), font=('bold', 20), width=3)
button2 = Button(myFrame, bg='yellow', text='2', relief=RIDGE, command=lambda: ins('2'), font=('bold', 20), width=3)
button1 = Button(myFrame, bg='yellow', text='1', relief=RIDGE, command=lambda: ins('1'), font=('bold', 20), width=3)
button0 = Button(myFrame, bg='yellow', text='0', relief=RIDGE, command=lambda: ins('0'), font=('bold', 20), width=6)

button_point = Button(myFrame, bg='yellow', text='.', relief=RIDGE, command=lambda: ins('.'), font=('bold', 20), width=3)
button_comma = Button(myFrame, bg='yellow', text=',', relief=RIDGE, command=lambda: ins(','), font=('bold', 20), width=3)

button_equal = Button(myFrame, bg='green', text='=', relief=RIDGE, command=equal, font=('bold', 20), width=6)
button_add = Button(myFrame, bg='green', text='+', relief=RIDGE, command=lambda: ins('+'), font=('bold', 20), width=3)
button_sub = Button(myFrame, bg='green', text='-', relief=RIDGE, command=lambda: ins('-'), font=('bold', 20), width=3)
button_mul = Button(myFrame, bg='green', text='*', relief=RIDGE, command=lambda: ins('*'), font=('bold', 20), width=3)
button_div = Button(myFrame, bg='green', text='/', relief=RIDGE, command=lambda: ins('/'), font=('bold', 20), width=3)

button_open = Button(myFrame, bg='gray', text='(', relief=RIDGE, command=lambda: ins('('), font=('bold', 20), width=3)
button_end = Button(myFrame, bg='gray', text=')', relief=RIDGE, command=lambda: ins(')'), font=('bold', 20), width=3)

button_sin = Button(myFrame, bg='blue', text='sin', relief=RIDGE, command=lambda: ins('sin'), font=('bold', 20), width=3)
button_cos = Button(myFrame, bg='blue', text='cos', relief=RIDGE, command=lambda: ins('cos'), font=('bold', 20), width=3)
button_tan = Button(myFrame, bg='blue', text='tan', relief=RIDGE, command=lambda: ins('tan'), font=('bold', 20), width=3)
button_ln = Button(myFrame, bg='blue', text='ln', relief=RIDGE, command=lambda: ins('log'), font=('bold', 20), width=3)
button_log = Button(myFrame, bg='blue', text='log', relief=RIDGE, font=('bold', 20), width=3, command=lambda: ins('log'))

button_factorial = Button(myFrame, bg='blue', text='x!', relief=RIDGE, command=lambda: ins('factorial'), font=('bold', 20), width=3)

button_Permutation = Button(myFrame, bg='blue', text='P', relief=RIDGE, command=lambda: ins('p'), font=('bold', 20), width=3)
button_computation = Button(myFrame, bg='blue', text='C', relief=RIDGE, command=lambda: ins('c'), font=('bold', 20), width=3)

button_pi = Button(myFrame, bg='orange', text='pi', relief=RIDGE, command=lambda: ins('pi'), font=('bold', 20), width=3)
button_e = Button(myFrame, bg='orange', text='e', relief=RIDGE, command=lambda: ins('e'), font=('bold', 20), width=3)

button_asin = Button(myFrame, text='asin', relief=RIDGE, bg='blue', command=lambda: ins('asin'), font=('bold', 20), width=3)
button_acos = Button(myFrame, text='acos', relief=RIDGE, bg='blue', command=lambda: ins('acos'), font=('bold', 20), width=3)
button_atan = Button(myFrame, text='atan', relief=RIDGE, bg='blue', command=lambda: ins('atan'), font=('bold', 20), width=3)

button_clear = Button(myFrame, text='C', relief=RIDGE, command=clear, bg='red', font=('bold', 20), width=3)
button_delete = Button(myFrame, relief=RIDGE, bg='white', command=deleted, font=('bold', 20), width=51, image=image_of_delete_button, compound=CENTER)

# end of buttons_______________________________________________________________________________________________________________________________________________


# d = StringVar()
# d.set('radian')
# def jk():
#     print(d.get())
# radio_button1 = Radiobutton(myFrame, text='degrees', variable=d, value='degrees', command=jk)
# radio_button2 = Radiobutton(myFrame, text='radian', variable=d, value='radian', command=jk)
# # button_clear_history = Button(myFrame,text='clear history',command=lambda:ins('clearH'),width=10,borderwidth=5)
# radio_button1.grid(row=0, column=7)
# radio_button2.grid(row=1, column=7)


# grids__________________________________________________________________________________________________________________________________________________

button7.grid(row=1, column=0, pady=1, padx=1, sticky=W)
button8.grid(row=1, column=1, pady=1, padx=1, sticky=W)
button9.grid(row=1, column=2, pady=1, padx=1, sticky=W)

button4.grid(row=2, column=0, pady=1, padx=1, sticky=W)
button5.grid(row=2, column=1, pady=1, padx=1, sticky=W)
button6.grid(row=2, column=2, pady=1, padx=1, sticky=W)

button0.grid(row=4, column=0, pady=1, padx=1, columnspan=2, ipadx=6)

button3.grid(row=3, column=0, pady=1, padx=1, sticky=W)
button2.grid(row=3, column=1, pady=1, padx=1, sticky=W)
button1.grid(row=3, column=2, pady=1, padx=1, sticky=W)


button_equal.grid(row=6, column=0, pady=1, padx=1, columnspan=2, ipadx=6)

button_sub.grid(row=2, column=3, pady=1, padx=1, sticky=W)
button_add.grid(row=2, column=4, pady=1, padx=1, sticky=W)
button_div.grid(row=3, column=3, pady=1, padx=1, sticky=W)
button_mul.grid(row=3, column=4, pady=1, padx=1, sticky=W)
button_point.grid(row=4, column=2, pady=1, padx=1, sticky=W)
button_open.grid(row=4, column=3, pady=1, padx=1, sticky=W)
button_end.grid(row=4, column=4, pady=1, padx=1, sticky=W)
button_comma.grid(row=5, column=2, pady=1, padx=1, sticky=W)
button_log.grid(row=5, column=3, pady=1, padx=1, sticky=W)
button_factorial.grid(row=5, column=4, pady=1, padx=1, sticky=W)
button_ln.grid(row=6, column=2, pady=1, padx=1, sticky=W)
button_Permutation.grid(row=6, column=4, pady=1, padx=1, sticky=W)
button_computation.grid(row=6, column=3, pady=1, padx=1, sticky=W)


button_sin.grid(row=1, column=5, pady=1, padx=1, ipadx=4, sticky=W)
button_cos.grid(row=2, column=5, pady=1, padx=1, ipadx=4, sticky=W)
button_tan.grid(row=3, column=5, pady=1, padx=1, ipadx=4, sticky=W)

button_acos.grid(row=4, column=5, pady=1, padx=1, ipadx=4, sticky=W)
button_atan.grid(row=5, column=5, pady=1, padx=1, ipadx=4, sticky=W)
button_asin.grid(row=6, column=5, pady=1, padx=1, ipadx=4, sticky=W)

button_pi.grid(row=5, column=0, pady=1, padx=1, sticky=W)
button_e.grid(row=5, column=1, pady=1, padx=1, sticky=W)
button_clear.grid(row=1, column=3, pady=1, padx=1, sticky=W)
button_delete.grid(row=1, column=4, pady=1, padx=1, sticky=W)
# eu.focus_set()
# end of grids________________________________________________________________________________________________________________________________________________


# button0.grid_forget()


# button_clear_history.grid(row=0,column=7,sticky='E')
# print(eu.keys())

mainloop()
