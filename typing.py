
# window.mainloop()
####################varvis 4
from tkinter import *
from time import strftime
from PIL import ImageTk, Image
import time
from playsound import playsound
import os
import random
from timeit import default_timer as timer

import random
root = Tk()
root.title("typing")
root.geometry("1000x650+40+30")

x=0

def game():
    windows = Toplevel(root)
    windows.geometry("1250x500") 
    global x
    if x == 0:
        # root.destroy()
        x = x + 1

    def check_result():
        end = timer()
        check=end - start
        if entry.get() == words[word]:
 
            print(end - start)
            x4 = Label(windows, text="BINGO! RIGHT Input",bg="orange" ,font="times 20")
            x4.place(x=250, y=230)
            x4 = Label(windows, text="you have taken time=="+str(check), font="times 20")
            x4.place(x=250, y=300)
            
        else:
            print("Wrong Input")
            x4 = Label(windows, text="Wrong Input",bg="orange" ,font="times 20")
            x4.place(x=250, y=230)
            x4 = Label(windows, text="you have taken time=="+str(check), font="times 20")
            x4.place(x=250, y=300)
    # print(check_result.c)
    word = ['programming', 'coding', 'algorithm',
    "A positive attitude can really make dreams come true.",
                "Never bend your head. Always hold it high. Look the world Vertical in the eye.",
                "Rules are meant to be Broken.",
                "If people are trying to bring you “Down”, It only means that you are “Above them”.",
                "No one is busy in this world. Its all about priorities!",
                "I have a sign of my door. The sign says, Attitude is everything, so pick a good one.!",
                "Before you criticize ME, make sure u are Excellent.",
                "If you left me without any Reason, Do not come back with any Justification.",
                "In order to succeed your desire for success should be greater than your fear of failure.",

                "I am always right, Once I thought that I am wrong, But i was wrong.",
                "Respect for those who deserve it, not for those who demand it.",
                "My Life, My Choices, My Mistakes, My Lessons, Not your business…",
                "Before you want the world to believe in you,make sure you have started believing in yourself.",

                "My attitude will always be based on how you treat me..",
                "If you’re searching for that one person who will change your life, take a look in the mirror.",

                "Its not the Mountains we conquer, but ourselves.",
                "Failure is the opportunity to begin again more intelligently.","The greatest advantage of speaking the truth is that you don’t have to remember what you said.",

                "You say I dream too big I say you think too small.",
                "I myself am entirely made of blame, stitched together with good intentions…",
                "The purpose of our life is to be happy",
                "Don’t count the days, Make the days count.",
                "My Attitude is a result of your actions! So if you don’t like my Attitude blame yourself.",
                "Two things define you: Your Patience when you have nothing, and your Attitude when you have Everything.",
                "Only difference between Good day and a Bad day is your Attitude..",
                "Alter your Attitude and you can alter your Life.",
                "Always remember that you are Unique just like everyone else.",
                "Boys use the word Friendship to start love… and Girls use this word Friendship to end love. Same word but a different Attitude….",
                "Your Attitude can hurt me… But mine can even kill you.",
                "Hurt me with the Truth, but never comfort me with a Lie.",

             'systems', 'python', 'software']
    words = random.randint(0, (len(words) - 1))
   
    start = timer()
    x31 = Label(windows , text="TYPE BELOW WORDS", font="times 20 bold")
    x31.place(x=500, y=10)
    x2 = Label(windows , text=words[word],font="comicsansms 20 ")    
    x2.place(x=150, y=60)
    x3 = Label(windows , text="Start Typing", font="times 20 bold")
    x3.place(x=10, y=100)
    entry = Entry(windows ,font="comicsansms 17 ",width=77,fg="orange")
    entry.place(x=180, y=105)
    b2 = Button(windows ,font="comicsansms 20 bold", text="Done",command=check_result, width=12, bg='grey')
    b2.place(x=150, y=150)
    b3 = Button(windows ,font="comicsansms 20 bold", text="Try Again",command=gameover, width=12, bg='grey')
    b3.place(x=350, y=150)

    # print(check_result.c)
    windows.mainloop()





canvas = Canvas(root, width=500, height=500)
canvas.pack()
img = ImageTk.PhotoImage(Image.open("C:\\Users\\rishabh tiwari\\PycharmProjects\\firstpro\\os\\a.jpg"))
canvas.pack(side='top', fill='both', expand='yes')
canvas.create_image(0, 0, anchor=NW, image=img)
###frame
framegreen = Frame(root, bg="#000023")

framegreen.place(x=0, y=600, height=100, width=250)
###label
title = Label(framegreen, text="press for setting and about to", font=("Impact", 15, "italic"), bg="white", fg="red").place(x=5, y=1)
#
f2 = Frame(root)
f2.place(x=200, y=400, height=60, width=380)

b1 = Button(f2, font=("adobe arbic", 20, "italic"), text="press to get typing option", bg="Aqua", command=game)
b1.place(x=200, y=410, height=10, width=300)
b1.pack()
# frame and button of QUIT
f3 = Frame(root)
f3.place(x=690, y=400, height=60, width=80)
b2 = Button(f3, font=("Impact", 20, "italic"), text="EXIT", bg="Aqua", command=lambda: root.destroy())
b2.place(x=650, y=460)
b2.pack()

work = Label(root, text="TYPING MASTER BY RISHABH ", font=("Impact", 25, "italic"), bg="white",
             fg="Aqua").place(x=400, y=70)



root.mainloop()
             