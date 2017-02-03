from gpiozero import RGBLED
from tkinter import *

class App:
    def __init__(self,master):
        mainFrame = Frame(master,width=700,height=400);
        
        leftFrame = Frame(mainFrame,bg="#bbbbbb",width=200,height=400);
        
        self.resultCanvas = Canvas(leftFrame,width=200,height=200,bg="#bbbbbb");       
        self.resultCanvas.create_rectangle(10,10,180,180,fill="blue");
        self.resultCanvas.pack();
        
        leftFrame.pack(side=LEFT,fill=Y);
        
        rightFrame=Frame(mainFrame,bg="#bbbbbb",width=500);
        self.createRightArea(rightFrame);
        
        rightFrame.pack(side=LEFT,fill=Y);
        
        mainFrame.pack(fill=BOTH,expand=YES);

    def createRightArea(self,master):
        redLabel = Label(master,text="Red",fg="red",justify=LEFT,compound=LEFT).pack(fill=X,pady=10);
        self.redScale = Scale(master,from_=0,to=100,orient=HORIZONTAL,length=500,bg="red",foreground="white").pack(fill=X,pady=10);
        greenLabel = Label(master,text="Green",fg="green",justify=LEFT,compound=LEFT).pack(fill=X,pady=10);
        self.greenScale = Scale(master,from_=0,to=100,orient=HORIZONTAL,length=500,bg="green",foreground="white").pack(fill=X,pady=10);
        blueLabel = Label(master,text="Blue",fg="blue",justify=LEFT,compound=LEFT).pack(fill=X,pady=10);
        self.blueScale = Scale(master,from_=0,to=100,orient=HORIZONTAL,length=500,bg="blue",foreground="white").pack(fill=X,pady=10);
        

root = Tk();
root.geometry("700x400");
root.title("RGB_LED");
root.option_add("*Font",("Helvetica",18,"bold"));
root.option_add("*background","#bbbbbb");
display = App(root);
root.mainloop();
