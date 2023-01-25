from tkinter import *
class MyWindow:

    def __init__(self, win):
        self.label1=Label(win, text= "Value for a:", fg="aqua")
        self.label2 = Label(win, text='Value for b:', fg="red")
        self.label3 = Label(win, text='Value for c:', fg="lime")
        self.label4 = Label(win, text='Answer:', fg="lightblue")
        self.label1.place(x=80, y=40)
        self.label2.place(x=80, y=90)
        self.label3.place(x=80, y=140)
        self.label4.place(x=225, y=250)
        self.text1 = Entry()
        self.text2 = Entry()
        self.text3 = Entry()
        self.text4 = Entry()
        self.text1.place(x=160, y=40)
        self.text2.place(x=160, y=90)
        self.text3.place(x=160, y=140)
        self.text4.place(x=50, y=275, height=50, width=400)
        self.button1 = Button(win, text='Calculate Quadratic')
        self.b1 = Button(win, text='Calculate Quadratic', command=self.quad)
        self.b1.place(x=180, y=195)

    def quad(quadcal):
        import cmath

        a = float(quadcal.text1.get())
        b = float(quadcal.text2.get())
        c = float(quadcal.text3.get())
        discriminant = cmath.sqrt((b ** 2) - (4 * a * c))

        answer_one = (-b + discriminant) / (2 * a)

        answer_two = (-b - discriminant) / (2 * a)

        result = answer_one, answer_two
        quadcal.text4.delete(0, 'end')
        quadcal.text4.insert(END, str(result))


window=Tk()
mywin=MyWindow(window)
window.title('Quadratic Calculator')
window.geometry("500x500")
window.mainloop()