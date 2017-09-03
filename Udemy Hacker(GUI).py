from Tkinter import *
import Hacking_Udemy
import tkMessageBox

#Functions For Success Code
def Succesful_HAcking():
    tkMessageBox.showinfo("Thanks For Using", "Hacking Courses Succesfully Taken Press Ok To Continue ")
    Hacking_Udemy.hacking_courses()

def Succesful_Programming():
    tkMessageBox.showinfo("Thanks For Using", "Programming Courses Course Succesfully Taken Press Ok To Continue")
    Hacking_Udemy.Programming_courses()

def Succesful_Lifestyle():
    tkMessageBox.showinfo("Thanks For Using", "Lifestyle Courses Succesfully Taken Press Ok To Continue")
    Hacking_Udemy.Lifestyle_courses()

def Succesful_Marketing():
    tkMessageBox.showinfo("Thanks For Using", "Marketing Courses Succesfully Taken Press Ok To Continue")
    Hacking_Udemy.Marketing_courses()

def Succesful_Design():
    tkMessageBox.showinfo("Thanks For Using", "Design Courses Succesfully Taken Press Ok To Continue")
    Hacking_Udemy.Designing_Courses()

def Succesful_All():
    tkMessageBox.showinfo("Thanks For Using", "All Courses Succesfully Taken Press Ok To Continue")
    Hacking_Udemy.All_Courses()

#Creation Of MAin Window and Configuration

main = Tk()
main.configure(background='black',padx=30,pady=30)
main.maxwidth=1000, 1000
main.minwidth=1000, 1000
main.resizable(False, False)
main.wm_title("Udemy Hacker By Ferreter")

#COnfiguration for ALL COURSES Button

bottom_frame = Frame(main)
bottom_frame.pack(side=BOTTOM,padx=70)
bottom_frame.configure(bg='black',padx=70)

#Main Logo and BY Ferreter and Notice Creation and COnfiguration

Main_logo = Label(main,text="Udemy Hacker",fg="red",bg="black",font=("Fixedsys",44,"roman bold italic"))
Main_logo.pack()
Main_logo.configure()

BY_Below_mainLogo= Label(main,text="By Ferreter",fg="red",bg="black",font=("Fixedsys",28,"italic"))
BY_Below_mainLogo.pack()
BY_Below_mainLogo.configure(padx=400)


Notice_text = Label(main,text="Please Click on any one of the below buttons  to get the \n course you want.\"Note: Please Login on www.Udemy.com before \n clicking any button \" :",fg="red",bg="black",font=("Fixedsys",20))
Notice_text.pack(pady=(100,50))

#All The Buttons Creation and Configurations

Hacking_button = Button(main,command=Succesful_HAcking,bg="black",fg="red",text="Hacking Courses",font=("Fixedsy",16), borderwidth=3, relief="groove",activeforeground="red",activebackground='grey')
Hacking_button.pack(side=LEFT,padx=10,pady=10)

Programming_button = Button(main,command=Succesful_Programming,bg="black",fg="red",text="Programming Courses",font=("Fixedsys",16), borderwidth=3, relief="groove",activeforeground="red",activebackground='grey')
Programming_button.pack(side=LEFT,padx=10,pady=10)

Lifestyle_button = Button(main,bg="black",fg="red",command=Succesful_Lifestyle,text="Lifestyle Courses",font=("Fixedsys",16), borderwidth=3, relief="groove",activeforeground="red",activebackground='grey')
Lifestyle_button.pack(side=LEFT,padx=10,pady=10)

Marketing_button = Button(main,bg="black",fg="red",command=Succesful_Marketing,text="Marketing Courses",font=("Fixedsys",16), borderwidth=3, relief="groove",activeforeground="red",activebackground='grey')
Marketing_button.pack(side=LEFT,padx=10,pady=10)

Design_button = Button(main,bg="black",fg="red",command=Succesful_Design,text="Design Courses",font=("Fixedsys",16), borderwidth=3, relief="groove",activeforeground="red",activebackground='grey')
Design_button.pack(side=LEFT,padx=10,pady=10)

All_Courses_button = Button(bottom_frame,bg="black",fg="red",text="All Courses",command=Succesful_All,font=("Fixedsys",16), borderwidth=3, relief="groove",activeforeground="red",activebackground='grey')
All_Courses_button.pack(side=BOTTOM,padx=70)

#Main Loop so that it does not close

main.mainloop()
