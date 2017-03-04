from tkinter import *
from gpiozero import AngularServo

class App:
    
    def __init__(self,master):
        #for gpio servo initial
        self.servo = AngularServo(18,min_angle=0,max_angle=90);
        #for tk
        self.master = master;
        mainFrame = Frame(self.master);
        servoFrame = Frame(mainFrame);
        borderFrame = Frame(servoFrame,borderwidth=2,relief=GROOVE,pady=30,padx=10);        
        Label(servoFrame,text="Servo").place(relx=0.03,anchor=NW);
        self.button0 = Button(borderFrame,text="0",width=5,command=lambda:self.changeDegree(0));
        self.button0.pack(side=LEFT,pady=5);
        self.button0.focus();
        self.button25 = Button(borderFrame,text="25",width=5,command=lambda:self.changeDegree(25));
        self.button25.pack(side=LEFT,pady=5);
        self.button50 = Button(borderFrame,text="50",width=5,command=lambda:self.changeDegree(50));
        self.button50.pack(side=LEFT,pady=5);
        self.button75 = Button(borderFrame,text="75",width=5,command=lambda:self.changeDegree(75));
        self.button75.pack(side=LEFT,pady=5);
        self.button90 = Button(borderFrame,text="90",width=5,command=lambda:self.changeDegree(90));
        self.button90.pack(side=LEFT,pady=5);
        borderFrame.pack(side=TOP,padx=10,pady=10);    
        servoFrame.pack(side=TOP);
        #getting widget that trigged an event(search);
        distanceFrame = Frame(mainFrame);
        distanceFrame.pack(side=TOP);
        mainFrame.pack();
    
    def changeDegree(self,number):
        self.servo.angle=number;
        

if __name__ == "__main__":
    root = Tk();
    root.title("servo And HC-HR04");
    root.option_add("*font",("Helvetica",18, "bold"));
    root.option_add("*background","gold");
    root.option_add("*activeBackground","#333");
    root.option_add("*activeForeground","white");
    root.option_add("*highlightBackground","red");
    root.option_add("*HighlightColor","black");
    app = App(root);
    root.mainloop();
    
    
    
