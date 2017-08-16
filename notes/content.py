from tkinter import *
class App:
        def __init__(self,master):
            #master.geometry("300x200");
            fm = Frame(master);
            Button(fm, text="Top").pack(side=TOP,expand=YES,fill=BOTH);
            Button(fm, text="Center").pack(side=TOP,expand=YES,fill=BOTH);
            Button(fm, text="Bottom").pack(side=TOP,expand=YES,fill=BOTH);
            fm.pack(side=LEFT);
            fm2 = Frame(master);
            Button(fm2, text="Left").pack(side=LEFT);
            Button(fm2, text="This is Center").pack(side=LEFT);
            Button(fm2, text="Right").pack(side=LEFT);
            fm2.pack(side=LEFT);
            
root = Tk();
root.option_add("*font",("verdana",12,"bold"));
root.title("Pack - Example 4");
display = App(root)
root.mainloop();
