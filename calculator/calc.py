from tkinter import *

class main:
    # all used class variables
    root = None
    display = None
    inpt = None
    default_inpt = ''

    def __init__(self):
        self.root = Tk()
        # window size config
        self.root.geometry("335x400")
        self.root.maxsize(335, 400)
        self.root.minsize(335, 400)
        # window style config
        self.root.title('Python calc')
        self.root.iconbitmap('calc.ico')
        self.root.configure(bg='#dbdbdb')

        self.inpt = StringVar()
        self.main_activity()


    # functions

    def click_button(self, num):
        if num == '^':
            self.default_inpt += '**'
            self.inpt.set(self.default_inpt)
        else:
            self.default_inpt += str(num)
            self.inpt.set(self.default_inpt)

    def equalbutton(self, event):
        res = eval(self.default_inpt)
        self.inpt.set(res)
        self.default_inpt = str(res)

    def clear_display(self, event):
        self.default_inpt = ''
        self.inpt.set('')

    def backspc(self, event):
        self.default_inpt = self.default_inpt[:-1]
        self.inpt.set(self.default_inpt)


    def main_activity(self):

        # creating widgets
        self.display = Entry(self.root, textvariable= self.inpt, font=('Digital-7',26), width=18, state='disabled', bd=4, disabledbackground='#d9fffd')
        Button0 = Button(self.root, text='0', padx=14, pady=14, command= lambda: self.click_button(0), font=('Digital-7',16))
        Button1 = Button(self.root, text='1', command= lambda: self.click_button(1), font=('Digital-7',16), padx=17, pady=14)
        Button2 = Button(self.root, text='2', command= lambda: self.click_button(2), font=('Digital-7',16), padx=14, pady=14)
        Button3 = Button(self.root, text='3', command= lambda: self.click_button(3), font=('Digital-7',16), padx=14, pady=14)
        Button4 = Button(self.root, text='4', command= lambda: self.click_button(4), font=('Digital-7',16), padx=14, pady=14)
        Button5 = Button(self.root, text='5', command= lambda: self.click_button(5), font=('Digital-7',16), padx=14, pady=14)
        Button6 = Button(self.root, text='6', command= lambda: self.click_button(6), font=('Digital-7',16), padx=14, pady=14)
        Button7 = Button(self.root, text='7', command= lambda: self.click_button(7), font=('Digital-7',16), padx=14, pady=14)
        Button8 = Button(self.root, text='8', command= lambda: self.click_button(8), font=('Digital-7',16), padx=14, pady=14)
        Button9 = Button(self.root, text='9', command= lambda: self.click_button(9), font=('Digital-7',16), padx=14, pady=14)
        Button_plus = Button(self.root, text='+', command= lambda: self.click_button('+'), font=('Digital-7',16), padx=14, pady=14)
        Button_minus = Button(self.root, text='-', command= lambda: self.click_button('-'), font=('Digital-7',16), padx=14, pady=14)
        Button_multiply = Button(self.root, text='*', command= lambda: self.click_button('*'), font=('Digital-7',16), padx=14, pady=14)
        Button_div = Button(self.root, text='/', command= lambda: self.click_button('/'), font=('Digital-7',16), padx=13, pady=14)
        Button_power = Button(self.root, text='^', command= lambda: self.click_button('^'), font=('Digital-7',16), padx=17, pady=14)
        Button_equal = Button(self.root, text='=', font=('Digital-7',16), padx=18, pady=14)
        Button_clear = Button(self.root, text='CE', font=('Digital-7',16), padx=14, pady=14)
        Button_backspace = Button(self.root, text='←', font=('Digital-7',16), padx=12, pady=14)


        # packing widgets
        self.display.pack()

        # Binding buttons
        Button_equal.bind("<Button-1>", self.equalbutton)
        Button_clear.bind("<Button-1>", self.clear_display)
        Button_backspace.bind("<Button-1>", self.backspc)

        Button1.place(x=10, y=100)
        Button2.place(x=10,y=170)
        Button3.place(x=10,y=240)
        Button4.place(x=75,y=100)
        Button5.place(x=75,y=170)
        Button6.place(x=75,y=240)
        Button7.place(x=140,y=100)
        Button8.place(x=140,y=170)
        Button9.place(x=140,y=240)
        Button0.place(x=75,y=310)
        Button_plus.place(x=205,y=100)
        Button_minus.place(x=205,y=170)
        Button_multiply.place(x=205,y=240)
        Button_div.place(x=205,y=310)
        Button_power.place(x=270,y=310)
        Button_clear.place(x=270,y=100)
        Button_equal.place(x=270,y=240)
        Button_backspace.place(x=270,y=170)


calc = main()

mainloop()