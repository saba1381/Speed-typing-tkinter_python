from tkinter import *

app = Tk(className=" Speed Type Test")
app.geometry("700x400")


def easy():
    app.destroy()
    import Easy_page
def meduim():
    app.destroy()
    import meduim_page

def hard():
    app.destroy()
    import Hard_page

app.configure(bg="white")
title = Label(app, text="Welcome to Speed Typing Test", anchor=CENTER, font=("Arial Rounded MT Bold",20), bg="#F08080", fg='black', relief="solid")
title.place(x=158, y=20)

options=["Easy" , "Meduim" , "Hard"]


checked=StringVar()
checked.set("Easy")


lst=OptionMenu(app,checked,*options)
lst.pack(padx=145,pady=120)
lst.config(bg="pink",width=6)


def show():
    global checked
    if(checked.get()=="Easy"):
        easy()
    elif(checked.get()=="Meduim"):
        meduim()
    elif(checked.get()=="Hard"):
        hard()

start = Button(app, text="Click me", bg="green", fg="black", font="Arial 15", relief=RAISED,width=20,command=show)
start.place(x=245, y=200)


exit = Button(app, text="Exit", bg="red", fg="black", font="Arial 15", relief=RAISED,width=20,command=quit)
exit.place(x=245, y=300)
app.mainloop()