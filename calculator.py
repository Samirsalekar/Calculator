# # from tkinter import *
# # root = Tk()
# # root.geometry("400x300")
# #
# # root.minsize(250,150)
# # root.maxsize(300,500)
# # cal = Label(text="CALCULATOR")
# # cal.pack()
# #
# #
# # root.mainloop()
# #
# #
# # from tkinter import *
# # from PIL import Image,ImageTk
# # root = Tk()
# # root.geometry("500x300")
# # root.minsize(100,50)
# # root.maxsize(1000,1200)
# # root.title("Tkinter project")
# # cal = Label(text="Calculator")
# # cal.pack()
# # def animal():
# #     print("This is a lion")
# # def bird():
# #     print("lion and birds are different")
# # def reptile():
# #     print("lion and reptile are very smart")
# #
# # image = Image.open("download.jpg")
# # photo = ImageTk.PhotoImage(image)
# # Lion = Label(image=photo)
# # Lion.pack(side=TOP,anchor="nw")
# # title_label = Label(text='''The lion (Panthera leo) is a large cat of the genus Panthera, native to Africa and India. It has a muscular, broad-chested body; a short, rounded head; round ears;\n and a hairy tuft at the end of its tail. It is sexually dimorphic; adult male lions are larger than females and have a prominent mane.''')
# # title_label.pack(anchor="sw",side=TOP,fill=Y)
# # frame=Frame(root,borderwidth=7,bg="red",relief=SUNKEN)
# # frame.pack(anchor="nw",side=LEFT,)
# # frame1=Frame(root,borderwidth=10,bg="green",relief=SUNKEN)
# # frame1.pack(anchor="nw",side=LEFT)
# # frame2=Frame(root,borderwidth=10,bg="yellow",relief=SUNKEN)
# # frame2.pack(anchor="nw",side=LEFT)
# # b1=Button(frame1,text="click here",fg="grey",command=animal)
# # b1.pack(padx=25,side=RIGHT)
# # b2=Button(frame,text="click me",fg="red",command=bird)
# # b2.pack(padx=25,side=RIGHT)
# # b3=Button(frame2,text="click me",fg="white",command=reptile)
# # b3.pack(padx=25,side=RIGHT)
# # image2=Image.open("download (2).jpg")
# # photo2=ImageTk.PhotoImage(image)
# # Lion2=Label(image=photo)
# # Lion2.pack()
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# # root.mainloop()
# # from tkinter import *
# # root = Tk()
# # root.geometry("500x400")
# # root.minsize(200,300)
# # root.maxsize(800,900)
# # root.title("form project")
# #
# # def getval():
# #     pass
# # User = Label(root,text="Username")
# # Password = Label(root,text="Password")
# # User.grid()
# # Password.grid()
# # Uservalue = StringVar
# # Passvalue = StringVar
# # Userentry = Entry(root,textvariable=Uservalue)
# # Passentry = Entry(root,textvariable=Passvalue)
# # Userentry.grid(row=0,column = 1)
# # Passentry.grid(row=1,column=1)
# # Button(text="SUBMIT",command=getval).grid()
# #
# #
# #
# #
# #
# #
# #
# #
# # root.mainloop()
# # from tkinter import *
# # def click(event):
# #     global fieldvalue
# #     text=event.widget.cget("text")
# #     print(text)
# #     if text == "=":
# #         if fieldvalue.get().isdigit():
# #             value = int(fieldvalue.get())
# #         else:
# #             value = eval(screen.get())
# #
# #         fieldvalue.set(value)
# #         screen.update()
# #
# #     elif text == "c":
# #         fieldvalue.set("")
# #         screen.update()
# #
# #     else:
# #         fieldvalue.set(fieldvalue.get()+text)
# #         screen.update()
# #
# #
# #
# #
# # root = Tk()
# # root.geometry("400x600")
# # root.minsize(500,700)
# # root.maxsize(500,700)
# # root.title("Samir Calculator")
# # root.wm_iconbitmap("th.jpg")
# # fieldvalue = StringVar()
# # fieldvalue.set("")
# # screen = Entry(root, textvar=fieldvalue, font="Arial 25 bold")
# # screen.pack(fill=X,ipadx=8,pady=10,padx=10)
# # frame = Frame(root,bg="black")
# # button = Button(frame,text="9",font="lucida 25 bold",bg="yellow",padx=5,pady=5)
# # button.pack(side=LEFT,padx=18,pady=12)
# # button.bind("<Button-1>",click)
# # button = Button(frame,text="8",font="lucida 25 bold",bg="yellow",padx=5,pady=5)
# # button.pack(side=LEFT,padx=18,pady=12)
# # button.bind("<Button-1>",click)
# # button = Button(frame,text="7",font="lucida 25 bold",bg="yellow",padx=5,pady=5)
# # button.pack(side=LEFT,padx=18,pady=12)
# # button.bind("<Button-1>",click)
# #
# #
# # frame.pack()
# #
# #
# # frame = Frame(root,bg="black")
# # button = Button(frame,text="6",font="lucida 25 bold",bg="yellow",padx=5,pady=5)
# # button.pack(side=LEFT,padx=18,pady=12)
# # button.bind("<Button-1>",click)
# # button = Button(frame,text="5",font="lucida 25 bold",bg="yellow",padx=5,pady=5)
# # button.pack(side=LEFT,padx=18,pady=12)
# # button.bind("<Button-1>",click)
# # button = Button(frame,text="4",font="lucida 25 bold",bg="yellow",padx=5,pady=5)
# # button.pack(side=LEFT,padx=18,pady=12)
# # button.bind("<Button-1>",click)
# #
# #
# #
# #
# #
# # frame.pack()
# #
# # frame = Frame(root,bg="black")
# # button = Button(frame,text="3",font="lucida 25 bold",bg="yellow",padx=5,pady=5)
# # button.pack(side=LEFT,padx=18,pady=12)
# # button.bind("<Button-1>",click)
# # button = Button(frame,text="2",font="lucida 25 bold",bg="yellow",padx=5,pady=5)
# # button.pack(side=LEFT,padx=18,pady=12)
# # button.bind("<Button-1>",click)
# # button = Button(frame,text="1",font="lucida 25 bold",bg="yellow",padx=5,pady=5)
# # button.pack(side=LEFT,padx=18,pady=12)
# # button.bind("<Button-1>",click)
# #
# #
# #
# #
# #
# # frame.pack()
# # frame = Frame(root,bg="black")
# # button = Button(frame,text="-",font="lucida 25 bold",bg="yellow",padx=6,pady=5)
# # button.pack(side=LEFT,padx=18,pady=12)
# # button.bind("<Button-1>",click)
# # button = Button(frame,text="0",font="lucida 25 bold",bg="yellow",padx=6,pady=5)
# # button.pack(side=LEFT,padx=18,pady=12)
# # button.bind("<Button-1>",click)
# # button = Button(frame,text="+",font="lucida 25 bold",bg="yellow",padx=6,pady=5)
# # button.pack(side=LEFT,padx=18,pady=12)
# # button.bind("<Button-1>",click)
# #
# #
# #
# #
# #
# # frame.pack()
# # frame = Frame(root,bg="black")
# # button = Button(frame,text="/",font="lucida 25 bold",bg="yellow",padx=7,pady=5)
# # button.pack(side=LEFT,padx=18,pady=12)
# # button.bind("<Button-1>",click)
# # button = Button(frame,text="=",font="lucida 25 bold",bg="yellow",padx=7,pady=5)
# # button.pack(side=LEFT,padx=18,pady=12)
# # button.bind("<Button-1>",click)
# # button = Button(frame,text="*",font="lucida 25 bold",bg="yellow",padx=7,pady=5)
# # button.pack(side=LEFT,padx=18,pady=12)
# # button.bind("<Button-1>",click)
# #
# #
# #
# #
# #
# # frame.pack()
# # frame = Frame(root,bg="black")
# # button = Button(frame,text="c",font="lucida 25 bold",bg="yellow",padx=5,pady=5)
# # button.pack(side=LEFT,padx=18,pady=12)
# # button.bind("<Button-1>",click)
# # button = Button(frame,text="%",font="lucida 25 bold",bg="yellow",padx=5,pady=5)
# # button.pack(side=LEFT,padx=18,pady=12)
# # button.bind("<Button-1>",click)
# # button = Button(frame,text=".",font="lucida 25 bold",bg="yellow",padx=5,pady=5)
# # button.pack(side=LEFT,padx=18,pady=12)
# # button.bind("<Button-1>",click)
# #
# #
# #
# #
# #
# # frame.pack()
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# # root.mainloop()
#
from tkinter import *
from PIL import Image,ImageTk
root=Tk()
def getvalue():
    print("Succesfully")

root.geometry("444x333")
root.title("TRAVELS COMPANY")

label = Label(root,text="SAMIR TOURS AND TRAVELS",font="comicsansms 13 bold")
label.grid(row=0,column = 20)
image = Image.open("images.jpg")
photo = ImageTk.PhotoImage(image)
bus = Label(image = photo)
bus.grid(row= 1,column=30)
name = Label(root,text = "FULL NAME")
PhoneNumber = Label(root,text = "Phone Number")
Gender = Label(root,text = "Gender")
Email = Label(root,text = "Email ID")
Address = Label(root,text = "Address")
Emergency = Label(root,text = "Emergency Contact")
Paymentmode = Label(root,text = "Payment mode")
name.grid(row=2,column=1)
PhoneNumber.grid(row=3,column=1)
Gender.grid(row=4,column=1)
Email.grid(row=5,column=1)
Address.grid(row=6,column=1)
Emergency.grid(row=7,column=1)
Paymentmode.grid(row=8,column=1)

namevalue = StringVar()
PhoneNumbervalue = StringVar()
Gendervalue = StringVar()
Emailvalue = StringVar()
Addressvalue = StringVar()
Emergencyvalue = StringVar()
Paymentmodevalue = StringVar()
Foodserviecevalue = IntVar()

nameentry = Entry(root,textvariable=namevalue)
PhoneNumberentry = Entry(root,textvariable=PhoneNumbervalue)
Genderentry = Entry(root,textvariable=Gendervalue)
Emailentry = Entry(root,textvariable=Emailvalue)
Addressentry = Entry(root,textvariable=Addressvalue)
Emergencyentry = Entry(root,textvariable=Emergencyvalue)
Paymentmodeentry = Entry(root,textvariable=Paymentmodevalue)

nameentry.grid(row=2,column=2)
PhoneNumberentry.grid(row=3,column=2)
Genderentry.grid(row=4,column=2)
Emailentry.grid(row=5,column=2)
Addressentry.grid(row=6,column=2)
Emergencyentry.grid(row=7,column=2)
Paymentmodeentry.grid(row=8,column=2)

foodservice = Checkbutton(text="want free meals?",variable=Foodserviecevalue)
foodservice.grid(row=9,column= 2)
button = Button(text="Submit",command=getvalue)
button.grid(row=10,column=2)








root.mainloop()