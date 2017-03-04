from tkinter import *

class App:    
    def __init__(self,master):
        self.master = master;
        mainFrame = Frame(self.master);
        servoFrame = Frame(mainFrame);
        borderFrame = Frame(servoFrame,borderwidth=2,relief=GROOVE,pady=30,padx=10);        
        Label(servoFrame,text="Servo").place(relx=0.03,anchor=NW);
        self.button0 = Button(borderFrame,text="0",width=5);
        self.button0.pack(side=LEFT,pady=5);
        self.button45 = Button(borderFrame,text="45",width=5);
        self.button45.pack(side=LEFT,pady=5);
        self.button90 = Button(borderFrame,text="90",width=5);
        self.button90.pack(side=LEFT,pady=5);
        self.button135 = Button(borderFrame,text="135",width=5);
        self.button135.pack(side=LEFT,pady=5);
        self.button180 = Button(borderFrame,text="180",width=5);
        self.button180.pack(side=LEFT,pady=5);
        borderFrame.pack(side=TOP,padx=10,pady=10);    
        servoFrame.pack(side=TOP);
        
        distanceFrame = Frame(mainFrame);
        distanceFrame.pack(side=TOP);
        mainFrame.pack();
        

if __name__ == "__main__":
    root = Tk();
    root.title("servo And HC-HR04");
    root.option_add("*font",("Helvetica",18, "bold"));
    root.option_add("*background","gold");
    root.option_add("*selectForeground","black");
    app = App(root);
    root.mainloop();
    
    
    
