from tkinter import *

def prime_factor():
    num=int(entry.get())
    if num>0:
        factor=2
        primeFacts = "{} = ".format(num)
        while num > factor:
            if num % factor == 0:
                primeFacts+= str(factor) + "*"
                num = num//factor
            else:
                factor += 1
        primeFacts += str(factor)
        resultlabel.configure(text=primeFacts)
    else:
        resultlabel.configure(text="Invalid Number")

window= Tk()
window.title("Prime Factorization")
window.geometry("600x350")
window.configure(bg="light blue", padx=10, pady=10)

frame1=Frame(window, bg="hot pink",width="400", height="130", padx=10, pady=10)
frame2=Frame(window, bg="hot pink",width="400", height="130", padx=10, pady=10)
frame3=Frame(window, bg="hot pink",width="400", height="130", padx=10, pady=10)
frame1.pack()
frame2.pack()
frame3.pack()

inputlabel=Label(frame1, bg="pink", fg="black", text="Enter your number: ", padx=10, pady=10, font=("Courier", 20))
inputlabel.pack(side=LEFT)

entry=Entry(frame1,bg="pink", fg="black", bd=10, font=("Courier", 20))
entry.pack(side=RIGHT)

button=Button(frame2, text="Click Here", font=("Courier", 30), bg="pink",fg="hot pink", command=prime_factor)
button.pack()

resultlabel=Label(frame3, bg="pink", text = "____", font=("Courier", 20))
resultlabel.pack()

window.mainloop()