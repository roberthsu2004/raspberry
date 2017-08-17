from tkinter import *
class App:
        def __init__(self,master):
            master.geometry("800x800");
            fm1 = Frame(master);
            fm1Border = Frame(fm1,borderwidth=2,relief=GROOVE);
            self.__garageLayout(fm1Border);
            fm1Border.pack(side=LEFT,expand=YES,fill=BOTH,padx=10,pady=10);
            fm1.pack(side=TOP,expand=YES,fill=BOTH);
        
            fm2 = Frame(master);
            fm2Border = Frame(fm2,borderwidth=2,relief=GROOVE);
            self.__livingRoomLayout(fm2Border);
            fm2Border.pack(side=LEFT,expand=YES,fill=BOTH,padx=10,pady=10);
            fm2.pack(side=TOP,expand=YES,fill=BOTH);
            
            fm3 = Frame(master);
            fm3Border = Frame(fm3,borderwidth=2,relief=GROOVE);
            self.__bathRoomLayout(fm3Border);
            fm3Border.pack(side=LEFT,expand=YES,fill=BOTH,padx=10,pady=10);
            fm3.pack(side=TOP,expand=YES,fill=BOTH);
        
        def __garageLayout(self,frame):
            fm1Title = Label(frame,text="停車庫").pack(side=TOP,pady=10,padx=10,anchor=W);
            #parking
            parkingFrame=Frame(frame,background="#345678");
            parkingBorder = Frame(parkingFrame,borderwidth=2,relief=GROOVE,background="#345678");
            parkingTitle = Label(parkingFrame,text="停車狀態",background="#345678",foreground="white").place(relx=0.02,rely=0.00,anchor=NW)
            self.parkingMessageString = StringVar();
            parkingMessage = Label(parkingBorder,textvariable=self.parkingMessageString,background="#345678",foreground="white").pack(expand=YES);
            self.parkingMessageString.set("presented");
            parkingBorder.pack(side=LEFT,expand=YES,fill=BOTH,padx=10,pady=10);
            parkingFrame.pack(side=LEFT,expand=YES,fill=BOTH);
            #gate
            gateFrame=Frame(frame,background="#876543");
            gateBorder = Frame(gateFrame,borderwidth=2,relief=GROOVE,background="#876543");
            gateTitle = Label(gateFrame,text="柵欄狀態",background="#876543",foreground="white").place(relx=0.02,rely=0.00,anchor=NW)
            self.gateTextString = StringVar();
            gateButton = Button(gateBorder,textvariable=self.gateTextString,command=self.changeGate).pack(expand=YES,fill=BOTH,padx=20,pady=20);
            self.gateTextString.set("Gate Open");
            gateBorder.pack(side=LEFT,expand=YES,fill=BOTH,padx=10,pady=10);
            gateFrame.pack(side=LEFT,expand=YES,fill=BOTH);

        def changeGate(self):
            if self.gateTextString.get() == "Gate Open":
                    self.gateTextString.set("Gate Close");
            else:
                    self.gateTextString.set("Gate Open");
            

        def __livingRoomLayout(self,frame):
            fm2Title = Label(frame,text="一樓客廳").pack(side=TOP,pady=10,padx=10,anchor=W);
            Button(frame, text="button4").pack(side=LEFT,expand=YES,fill=BOTH);
            Button(frame, text="button5").pack(side=LEFT,expand=YES,fill=BOTH);
            Button(frame, text="button6").pack(side=LEFT,expand=YES,fill=BOTH);

        def __bathRoomLayout(self,frame):
            fm3Title = Label(frame,text="二摟臥室").pack(side=TOP,pady=10,padx=10,anchor=W);
            Button(frame, text="button7").pack(side=LEFT,expand=YES,fill=BOTH);
            Button(frame, text="button8").pack(side=LEFT,expand=YES,fill=BOTH);
            Button(frame, text="button9").pack(side=LEFT,expand=YES,fill=BOTH);    
            
root = Tk();
root.option_add("*font",("verdana",18));
root.title("Home");
display = App(root)
root.mainloop();
