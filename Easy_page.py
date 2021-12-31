from tkinter import *
import random
import math
import tkinter.font as font

def back_page():
    app.destroy()
    import first_page

#create the window
app = Tk(className=" Easy")
app.geometry("750x590")


#background color:
app.configure(bg="white")
app_font = font.Font(size = 12)
#for the title: 
title = Label(app, text="EASY TEXT", anchor=CENTER, font=("Arial Rounded MT Bold",20), bg="pink", fg='black', relief="solid")
title.place(x=284, y=20)


large_font = ('Verdana',12)
text_enter = Entry(app, width='65' ,bg="white", fg="black",font=app_font)
text_enter.place(x=100, y=280)



text_sent = Label(app, height='5', width='60', fg='black', bg='pink', wraplength=500, anchor=CENTER,justify=CENTER ,font=large_font,relief="solid")
text_sent.place(x='90', y='100')

def random_sent():
    """To make a random sentence"""
    s=open("random_sentences_e.txt", "r").read()
    #to just read the file
    sentences=s.split("\n")
    random_sentc=random.choice(sentences)
    #to show it in the text_sent box
    text_sent.config(text=random_sentc)

random_sent()

def reset_delete():
    """To reset the program when you click on Reset button"""
    text_enter.delete(0,'end')
    global timer
    global count_fault
    global check
    global  doTick
    s=open("random_sentences_e.txt", "r").read()
    text_enter.config(bg="white")

    #to just read the file
    sentences=s.split("\n")
    random_sentc=random.choice(sentences)
    #to show it in the text_sent box
    text_sent.config(text=random_sentc)
    label_count.config(text="Number of words: ",bg="light blue",fg="black")
    label_result.config(text="Result: ",bg="light blue",fg="black")
    count_fault=0
    timeLabel.config(text="00:00:00",bg="white",fg="black",relief=None)
    doTick=False
    timer=[0,0,0,0]
    check=False
    faults.config(text="The number of faults: 0")
    count_fault=0


#button for reset
reset = Button(app, text="RESET", bg="light blue", fg="black", font=("Arial Rounded MT Bold",12), relief=RAISED, command=reset_delete,width=10)
reset.place(x=570, y=510)

label_result=Label(app,text="Result : ",font="Arial 11", bg="light blue" ,width="15",relief=SOLID)
label_result.place(x=100, y=335)
label_count=Label(app,text="Number of words: ", font="Arial 11",bg="light blue",width="15",relief=SOLID)
label_count.place(x=550, y=335)
label_main=Label(app,text="WPM: ", font="Arial 11",bg="light blue",width="15",relief=SOLID)
label_main.place(x=320, y=335)


#now we want calculate the time the numbers of letters

def calculate_word():
    """Calculate the time of your typing and show the result"""
    sent=text_enter.get()   #to get the text that you entered
    count_word=len(sent.split())
    return count_word


calculate_word()



def wpm():
    global timer
    timer[3]+=1.6 

    timer[0]=math.floor(timer[3]/100/60)
    timer[1]=math.floor((timer[3]/100) - (timer[0]*60))
    timer[2]=math.floor(timer[3]-(timer[1]*100)-(timer[0]*6000))

    sent=text_enter.get()   #to get the text that you entered
    count_word=len(sent.split())  #number of words
    sum=5*count_word
    if(timer[1]>0 and timer[1]<=59):
        result=sum//timer[1]
        return result
    elif(timer[0]==1 and timer[1]>0 and timer[1]<=59):
        result=sum//(timer[1]+60)
        return result
    elif(timer[0]==2 and timer[1]>0 and timer[1]<=59):
        result=sum//(timer[1]+120)
        return result

def show_result():
    """To show the result in the labels"""
    global timer
    timer[3]+=1.6 

    timer[0]=math.floor(timer[3]/100/60)
    timer[1]=math.floor((timer[3]/100) - (timer[0]*60))
    timer[2]=math.floor(timer[3]-(timer[1]*100)-(timer[0]*6000))
    if(timer[0]==0 and (timer[1])<=30):
        label_result.config(bg="#00FF00",fg="black")
        label_count.config(bg="#00FF00",fg="black")
        label_main.config(bg="#00FF00",fg="black")
        return "Execlent"

    elif((timer[1]>30  and timer[1]<=59) or (timer[0]==1 and timer[1]<=20 and timer[1]>=0) ):
        label_result.config(bg="yellow",fg="black")
        label_count.config(bg="yellow",fg="black")
        label_main.config(bg="yellow",fg="black")
        return "Average!"

    elif(timer[0]==1 and timer[1]>20 and timer[1]<=59):
        label_result.config(bg="chocolate",fg="black")
        label_count.config(bg="chocolate",fg="black")
        label_main.config(bg="chocolate",fg="black")
        return "Too Slow"
    elif(timer[0]>=2 and timer[1]>=0):
        label_result.config(bg="red",fg="white")
        label_count.config(bg="red",fg="white")
        label_main.config(bg="red",fg="white")
        return "Awful!!!"



def check_text(e):
    """Check the coreect letters when you are typing"""
    global count_fault
    origin=text_sent.cget("text")
    sent=text_enter.get()
    match_text=origin[0:len(sent)]       

    if(sent==origin):#if you typed correctly
        text_enter.config(fg="black")
        text_enter.config(bg="#00FF00")
        label_result.config(text="Result: "+show_result())
        label_count.config(text="Number of words: "+str(calculate_word()))
        label_main.config(text="WPM: "+str(wpm()))
        #label_main.config(text="Main result: "+str(main_result()))

    elif(sent==match_text):
        text_enter.config(fg="black")
        text_enter.config(bg="yellow")
    
    elif(sent!=match_text):#if one of your letters were wrong!
        text_enter.config(fg="white")
        text_enter.config(bg="red")
        count_errors()



#use events--->when the key goes up.
app.bind('<KeyRelease>',check_text)


count_fault=0

def count_errors():
    """Counting the times that you typed wrong"""
    global count_fault
    origin=text_sent.cget("text")
    sent=text_enter.get()
    match_text=origin[0:len(sent)]
    if(sent!=match_text):
        count_fault+=1
        faults.config(text="The number of faults  is : "+str(count_fault))
    


faults=Label(app,font=app_font,text="The number of faults: 0" ,bg="light blue" , width="25",relief="sunken")
faults.place(x=245, y=390)


doTick = True
check=False

timeLabel = Label(app,text="00:00:00" ,fg='black',font=('Helvetica',20) , bg="white")
timeLabel.pack(pady=230,padx=60)
timer=[0,0,0,0]


def tick2():
    """The main function for the timer"""
    global timer
    if not doTick:
        return

    timer[3]+=1.6 

    timer[0]=math.floor(timer[3]/100/60)
    timer[1]=math.floor((timer[3]/100) - (timer[0]*60))
    timer[2]=math.floor(timer[3]-(timer[1]*100)-(timer[0]*6000))
    timeLabel.config(text=str(have_zero(timer[0]))+":"+str(have_zero(timer[1]))+":"+str(have_zero(timer[2])))

    app.after(10,tick2)



def stop():
    """To stop the timer"""
    global doTick
    doTick = False
    timeLabel.config(bg="#00FF00",relief=SUNKEN,fg="black")

def start():
    """To start the timer"""
    global doTick
    doTick = True
    timeLabel.config(relief=SUNKEN)
    tick2()

def have_zero(timer):
    """add zero to the numbers"""
    if (timer<=9):
        timer="0"+str(timer)
    return timer
    

def main_timer(e):
    global check
    sent=len(text_enter.get())
    sent_text=text_enter.get()
    origin=len(text_sent.cget("text"))
    original_text=text_sent.cget("text")
    if(sent==0 and check==False):
        check=True
        start()
    elif(sent_text==original_text):
        stop()



back = Button(app, text="Back", bg="pink", fg="black", font=("Arial Rounded MT Bold",12), relief=RAISED , command=back_page,width=10)
back.place(x=22, y=510)

"""Start_btn = Button(app, text="Start", bg="pink", fg="black", font=("Arial Rounded MT Bold",13), relief=RAISED , command=main_timer,width=11)
Start_btn.place(x=300, y=510)"""

app.bind("<KeyPress>",main_timer)
app.mainloop()
