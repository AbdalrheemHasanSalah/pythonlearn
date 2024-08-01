from tkinter import *
#from PIL import Image

#canvas 
class A(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.geometry("1024x720+400+150")
        self.canvas=Canvas(self,bg="blue",highlightthickness=0)
        self.canvas.place(x=0,y=0,width=1024,height=720)
        self.canvas.create_rectangle(10,10,100,100,fill="orange",width=4)
        self.canvas.create_rectangle(10,140,150,140)
        self.canvas.create_rectangle(150,10,150,140)
        self.canvas.create_line(10,10,100,100)
        self.canvas.create_oval(10,10,100,100)
        self.canvas.create_oval(20,200,500,500)


a=A()
a.mainloop()

#import image
root = Tk()
root.title('PythonGuides')
photo=PhotoImage(file=r'D:\png.png')
Label(root,image=photo).pack()
root.geometry("500x500")

root.mainloop()

#text and entry and label and button 
root2=Tk()
root2.geometry("800x500")
root2.title('python')

def btn_print():
    print("hello world")
def btn2_print():
    label["text"]=txt1.get("1.0","end")
    label["bg"]="black"
fram=Frame(root2,bg="red")
txt1=Text(fram,width="50",height="4",bg="black",fg="white",font="40")
ent1=Entry(root2,bg="black",fg="white")
btn1=Button(fram,command=btn_print,text="print hello",width="10",height="1",font="5",bg="red",fg="black")
btn2=Button(fram,command=btn2_print,text="print on label",width="20",height="1",font="5",bg="red",fg="black")
label=Label(fram,text="label",width="15",height="5",bg="green",fg="red")
fram.pack()
txt1.pack()
ent1.pack()
btn1.pack()
btn2.pack()
label.pack()


root2.mainloop()
#frame 
root3=Tk()
root3.geometry("800x500")

frame=Frame(root3)
Btn1=Button(frame,text="button1")

frame2=Frame(root3)
Btn2=Button(frame2,text="button2")

frame3=Frame(root3)
btn3=Button(frame3,text="button3")

frame4=Frame(root3)
btn4=Button(frame4,text="button4")



Btn1.pack()
Btn2.pack()
btn3.pack()
btn4.pack()


# Btn1.place(anchor=NW,width="50",height="100",bordermode=OUTSIDE)
# Btn2.place(anchor=NW,width="100",height="150",bordermode=OUTSIDE)
# btn3.place(anchor=NW,width="55",height="100",bordermode=OUTSIDE)
# btn4.place(anchor=NW,width="200",height="250",bordermode=OUTSIDE)

# frame.pack(side=TOP)
# frame2.pack(side=LEFT)
# frame3.pack(side=RIGHT)
# frame4.pack(side=BOTTOM)



#Grids

frame.grid(column=1,row=1)
frame2.grid(column=2,row=1)
frame3.grid(column=1,row=2)
frame4.grid(column=2,row=2)


root3.mainloop()






#label frame  __________________________
#example this is label frame________________________________________
LP=Tk()
lbfr=LabelFrame(LP,text="this is label frame")
lbfr.pack(expand="yes",fill="both")
LP.mainloop()


#check button
def hello():
    print("hello world")
check=Tk()
checkbtn=Checkbutton(check,text="Auto Save",font="14",command=hello,onvalue=1,offvalue=0)

rdbtn=Radiobutton(check,text="1",value=1)
rdbtn2=Radiobutton(check,text="2",value=2)
rdbtn3=Radiobutton(check,text="3",value=3)
rdbtn4=Radiobutton(check,text="4",value=4)

checkbtn.pack()

rdbtn.pack()
rdbtn2.pack()
rdbtn3.pack()
rdbtn4.pack()



check.mainloop()


# #list box and panewindow
lp_tk=Tk()
lp=Listbox(lp_tk)



# panewindow
pane1=PanedWindow(background="blue",orient=VERTICAL)
pane1.pack(fill=BOTH,expand=1)
pane2=PanedWindow(background="red",orient=VERTICAL)
pane2.pack(fill=BOTH,expand=1)
pane3=PanedWindow(background="black")
lap=Label(pane3,text="pane",background="black",fg="red",font=50)
pane3.add(lap)
pane3.pack(fill=BOTH,expand=1)





# #list box

lp.insert(1,"oop1")
lp.insert(2,"oop2")
lp.insert(3,"oop3")
lp.insert(4,"oop4")
lp.insert(5,"oop5")

#lp.pack()


def checklp():
    strcheck=lp.get(ACTIVE)
    if strcheck=="oop1":
        print("1")

    elif strcheck=="oop2":
        print("2")
    elif strcheck=="oop3":
        print("3")
    elif strcheck=="oop4":
        print("4")
    elif strcheck=="oop5":
         print("5")

button1=Button(lp_tk,text="check",command=checklp)
pane1.add(button1)

button1.pack()

lp.mainloop()





#top level

top=Toplevel()

btn=Button(top,text="click")
btn.pack()




#menu bar
root=Tk()
root.title("menubar")
root.geometry("500x500")
def donothing():
    filewin=Toplevel(root)
    Button=Button(filewin,text="do nothing")
    Button.pack()
str=" "
def copy():
    global str 
    str=text.get("1.0","end")
def paste():
    label["text"]=str    
def undo():
    label["text"]=" "

menubar = Menu(root)
filemenu=Menu(menubar,tearoff=0)
filemenu.add_command(label="menu")
filemenu.add_command(label="open",command=donothing)
filemenu.add_command(label="save",command=donothing)
filemenu.add_command(label="close",command=root.quit)
filemenu.add_separator()
filemenu.add_command(label="exit",command=root.quit)
menubar.add_cascade(label="file",menu=filemenu)
edit=Menu(menubar,tearoff=0)
edit.add_cascade(label="undo",command=undo)
edit.add_separator()
edit.add_command(label="cut",)
edit.add_command(label="copy",command=copy)
edit.add_command(label="paste",command=paste)
menubar.add_cascade(label="edit",menu=edit)


text=Text(root,width=40,height=20,font=15)
label=Label(root,width=20,height=40,anchor=CENTER,background="black",foreground="white")


text.pack()
label.pack()
root.config(menu=menubar)

root.mainloop()
