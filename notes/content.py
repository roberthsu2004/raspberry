from tkinter import *
class App:
        def __init__(self,master):
            master.geometry("800x800");
            fm1 = Frame(master);
            fm1Border = Frame(fm1,borderwidth=2,relief=GROOVE);
            fm1Title = Label(fm1Border,text="停車庫").pack(side=TOP,pady=10,padx=10,anchor=W);
            Button(fm1Border, text="button1").pack(side=LEFT,expand=YES,fill=BOTH);
            Button(fm1Border, text="button2").pack(side=LEFT,expand=YES,fill=BOTH);
            Button(fm1Border, text="button3").pack(side=LEFT,expand=YES,fill=BOTH);
            fm1Border.pack(side=LEFT,expand=YES,fill=BOTH,padx=10,pady=10);
            fm1.pack(side=TOP,expand=YES,fill=BOTH);
            
            fm2 = Frame(master);
            fm2Border = Frame(fm2,borderwidth=2,relief=GROOVE);
            fm2Title = Label(fm2Border,text="一樓客廳").pack(side=TOP,pady=10,padx=10,anchor=W);
            Button(fm2Border, text="button4").pack(side=LEFT,expand=YES,fill=BOTH);
            Button(fm2Border, text="button5").pack(side=LEFT,expand=YES,fill=BOTH);
            Button(fm2Border, text="button6").pack(side=LEFT,expand=YES,fill=BOTH);
            fm2Border.pack(side=LEFT,expand=YES,fill=BOTH,padx=10,pady=10);
            fm2.pack(side=TOP,expand=YES,fill=BOTH);
            
            fm3 = Frame(master);
            fm3Border = Frame(fm3,borderwidth=2,relief=GROOVE);
            fm3Title = Label(fm3Border,text="二摟臥室").pack(side=TOP,pady=10,padx=10,anchor=W);
            Button(fm3Border, text="button7").pack(side=LEFT,expand=YES,fill=BOTH);
            Button(fm3Border, text="button8").pack(side=LEFT,expand=YES,fill=BOTH);
            Button(fm3Border, text="button9").pack(side=LEFT,expand=YES,fill=BOTH);
            fm3Border.pack(side=LEFT,expand=YES,fill=BOTH,padx=10,pady=10);
            fm3.pack(side=TOP,expand=YES,fill=BOTH);
            
root = Tk();
root.option_add("*font",("verdana",18));
root.title("Home");
display = App(root)
root.mainloop();
