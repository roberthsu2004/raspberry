from tkinter import *
class App:
        def __init__(self,master):
            master.geometry("800x800");
            fm1 = Frame(master);
            Button(fm1, text="button1").pack(side=LEFT,expand=YES,fill=BOTH);
            Button(fm1, text="button2").pack(side=LEFT,expand=YES,fill=BOTH);
            Button(fm1, text="button3").pack(side=LEFT,expand=YES,fill=BOTH);
            fm1.pack(side=TOP,expand=YES,fill=BOTH);
            
            fm2 = Frame(master);
            Button(fm2, text="button4").pack(side=LEFT,expand=YES,fill=BOTH);
            Button(fm2, text="button5").pack(side=LEFT,expand=YES,fill=BOTH);
            Button(fm2, text="button6").pack(side=LEFT,expand=YES,fill=BOTH);
            fm2.pack(side=TOP,expand=YES,fill=BOTH);
            
            fm3 = Frame(master);
            Button(fm3, text="button7").pack(side=LEFT,expand=YES,fill=BOTH);
            Button(fm3, text="button8").pack(side=LEFT,expand=YES,fill=BOTH);
            Button(fm3, text="button9").pack(side=LEFT,expand=YES,fill=BOTH);
            fm3.pack(side=TOP,expand=YES,fill=BOTH);
            
root = Tk();
root.option_add("*font",("verdana",12,"bold"));
root.title("Pack - Example 7");
display = App(root)
root.mainloop();
