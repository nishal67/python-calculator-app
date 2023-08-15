from tkinter import *
from tkinter.messagebox import *
import math as m

font = ('ariel', 20)

def clear():
    ex = textField.get()
    ex = ex[0:len(ex)-1]
    textField.delete(0,END)
    textField.insert(0,ex)

def all_clear():
    textField.delete(0,END)

def click_btn_function(event):
    print("btn clicked")
    b = event.widget
    text = b['text']
    print(text)

    if text=="×":
        textField.insert(END,"*")
        return
    if text=="÷":
        textField.insert(END,"/")
        return


    if text == "=":
     try:
        ex = textField.get()
        answer = eval(ex)
        textField.delete(0, END)
        textField.insert(0, answer)
     except Exception as e:
        print("Error", e)
        showerror("Error", e)
     return

    textField.insert(END, text)
#Creating a window
window = Tk()
window.title('My Calculator')
window.geometry('400x520')

#picture label
pic = PhotoImage(file='Images/cal2.png')
headingLabel = Label(window, image=pic)
headingLabel.pack(side=TOP, pady=15)

#heading label
heading = Label(window, text='My Calculator', font=font)
heading.pack(side=TOP)

#text field
textField = Entry(window, font=font, justify=CENTER)
textField.pack(side=TOP, pady=5, fill=X, padx=5)

#buttons
buttonFrame = Frame(window)
buttonFrame.pack(side=TOP)

#adding button
temp =1
for i in range(0,3):
    for j in range(0,3):
        btn = Button(buttonFrame, text=str(temp), font=font, width=5, relief="ridge", activebackground="gray", activeforeground="white")
        btn.grid(row=i, column=j, padx=5, pady=5)
        temp = temp + 1
        btn.bind('<Button-1>', click_btn_function)

zeroBtn = Button(buttonFrame, text="0", font=font, width=5, relief="ridge", activebackground="gray", activeforeground="white")
zeroBtn.grid(row=3, column=0, padx=5, pady=5)

dotBtn = Button(buttonFrame, text=".", font=font, width=5, relief="ridge", activebackground="gray", activeforeground="white")
dotBtn.grid(row=3, column=1, padx=5, pady=5)

equalBtn = Button(buttonFrame, text="=", font=font, width=5, relief="ridge", activebackground="gray", activeforeground="white")
equalBtn.grid(row=3, column=2, padx=5, pady=5)

plusBtn = Button(buttonFrame, text="+", font=font, width=5, relief="ridge", activebackground="gray", activeforeground="white")
plusBtn.grid(row=0, column=3, padx=5, pady=5)

minusBtn = Button(buttonFrame, text="-", font=font, width=5, relief="ridge", activebackground="gray", activeforeground="white")
minusBtn.grid(row=1, column=3, padx=5, pady=5)

multiplyBtn = Button(buttonFrame, text="×", font=font, width=5, relief="ridge", activebackground="gray", activeforeground="white")
multiplyBtn.grid(row=2, column=3, padx=5, pady=5)

divBtn = Button(buttonFrame, text="÷", font=font, width=5, relief="ridge", activebackground="gray", activeforeground="white")
divBtn.grid(row=3, column=3, padx=5, pady=5)

clearBtn = Button(buttonFrame, text="C", font=font, width=11, relief="ridge", activebackground="gray", activeforeground="white", command=clear)
clearBtn.grid(row=4, column=0, padx=5, pady=5, columnspan=2)

allclearBtn = Button(buttonFrame, text="AC", font=font, width=11, relief="ridge", activebackground="gray", activeforeground="white", command=all_clear)
allclearBtn.grid(row=4, column=2, padx=5, pady=5, columnspan=2)

#binding all buttons
plusBtn.bind('<Button-1>', click_btn_function)
minusBtn.bind('<Button-1>', click_btn_function)
multiplyBtn.bind('<Button-1>', click_btn_function)
divBtn.bind('<Button-1>', click_btn_function)
dotBtn.bind('<Button-1>', click_btn_function)
zeroBtn.bind('<Button-1>', click_btn_function)
equalBtn.bind('<Button-1>', click_btn_function)

##################################################################################################################################

scFrame = Frame(window)

sqrtBtn = Button(scFrame, text="√", font=font, width=5, relief="ridge", activebackground="gray", activeforeground="white")
sqrtBtn.grid(row=0, column=0, padx=5, pady=5)

powBtn = Button(scFrame, text="^", font=font, width=5, relief="ridge", activebackground="gray", activeforeground="white")
powBtn.grid(row=0, column=1, padx=5, pady=5)

factBtn = Button(scFrame, text="!", font=font, width=5, relief="ridge", activebackground="gray", activeforeground="white")
factBtn.grid(row=0, column=2, padx=5, pady=5)

radBtn = Button(scFrame, text="rad", font=font, width=5, relief="ridge", activebackground="gray", activeforeground="white")
radBtn.grid(row=0, column=3, padx=5, pady=5)

degBtn = Button(scFrame, text="°", font=font, width=5, relief="ridge", activebackground="gray", activeforeground="white")
degBtn.grid(row=1, column=0, padx=5, pady=5)

sinBtn = Button(scFrame, text="sinΘ", font=font, width=5, relief="ridge", activebackground="gray", activeforeground="white")
sinBtn.grid(row=1, column=1, padx=5, pady=5)

cosBtn = Button(scFrame, text="cosΘ", font=font, width=5, relief="ridge", activebackground="gray", activeforeground="white")
cosBtn.grid(row=1, column=2, padx=5, pady=5)

tanBtn = Button(scFrame, text="tanΘ", font=font, width=5, relief="ridge", activebackground="gray", activeforeground="white")
tanBtn.grid(row=1, column=3, padx=5, pady=5)



normalcalc = True

def calculate_sc(event):
    print("btn")
    btn = event.widget
    text = btn['text']
    print(text)
    ex = textField.get()
    answer = ''
    if text == '°':
        print("cal degree")
        answer = str(m.degrees(float(ex)))

    elif text == 'rad':
        print("cal radian")
        answer = str(m.radians(float(ex)))
    elif text == '^':
        print("cal power")
        base, pow = ex.split(',')
        print(base)
        print(pow)
        answer = str(m.pow(int(base), int(pow)))
    elif text == '!':
        print("cal factorial")
        answer = str(m.factorial(int(ex)))
    elif text == '√':
        print("cal squareRoot")
        answer = str(m.sqrt(int(ex)))
    elif text == 'sinΘ':
        print("cal sinTheta")
        answer = str(m.sin(m.radians(int(ex))))
    elif text == 'cosΘ':
        print("cal cosTheta")
        answer = str(m.cos(m.radians(int(ex))))
    elif text == 'tanΘ':
        print("cal tanTheta")
        answer = str(m.tan(m.radians(int(ex))))

    textField.delete(0, END)
    textField.insert(0, answer)

def sc_click():
    global normalcalc
    if normalcalc:
        buttonFrame.pack_forget()

        scFrame.pack(side=TOP)
        buttonFrame.pack(side=TOP)
        window.geometry('400x660')

        print("show scientific")
        normalcalc = False
    else:
        print("show normal")
        scFrame.pack_forget()
        window.geometry('400x520')
        normalcalc = True


#binding sc buttons
sqrtBtn.bind("<Button-1>", calculate_sc)
powBtn.bind("<Button-1>", calculate_sc)
factBtn.bind("<Button-1>", calculate_sc)
radBtn.bind("<Button-1>", calculate_sc)
degBtn.bind("<Button-1>", calculate_sc)
sinBtn.bind("<Button-1>", calculate_sc)
cosBtn.bind("<Button-1>", calculate_sc)
tanBtn.bind("<Button-1>", calculate_sc)

fontMenu = ('',10)
menubar = Menu(window)

mode = Menu(menubar, font=fontMenu, tearoff=0)
mode.add_checkbutton(label="Scientific Calculator", command=sc_click)

menubar.add_cascade(label="Mode", menu=mode)

window.config(menu=menubar)


window.mainloop()