from tkinter import *

conduitType = ["Heavy duty rigid UPVC conduit", "Corflo conduit", 
"Medium duty corrugated", "Medium duty rigid UPVC conduit"]
CableType = ['-', '1.5', '2.5', '4' , '6' ,'10' ,'16', '25','35','50','70','95']
XLPE = ['-', '16','25','35','50','70','95','120']

class Application(Frame):

    def __init__(self, master):
        """ Initialise the Frame. """
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self): 

        self.conduitLbl = Label (self, text = "Type of Conduit", height=2, width=20)#Label
        self.conduitLbl.grid(row=0, column = 0)

        self.conduit = StringVar(master) ### OPTION MENU FOR CONIOT TYPE
        self.conduit.set("Heavy duty rigid UPVC conduit") # default value
        self.conduitOptions = OptionMenu(master, self.conduit, *conduitType)
        self.conduitOptions.config(width=28)
        self.conduitOptions.grid(row=0, column=1)
        
        self.PVCLabel = Label (master, text = "Cable Type", height=2, width=20)#Label
        self.PVCLabel.grid(row=1, column = 0)
        
        self.PVC_flat = Label (master, text = "XLPE Cable Type", height=2, width=20)#Label
        self.PVC_flat.grid(row=2, column = 0)

        self.cable = StringVar(master)
        self.cable.set("-") # default value
        self.PVCom = OptionMenu(master, self.cable, *CableType, )
        self.PVCom.config(width=15)
        self.PVCom.grid(row=1, column=1)

        self.cablePVC = StringVar(master)
        self.cablePVC.set("-") # default value
        self.PVCom = OptionMenu(master, self.cablePVC, *XLPE, )
        self.PVCom.config(width=15)
        self.PVCom.grid(row=2, column=1)

        self.circuitLbl = Label (master, text = "Number of Circuits:", height=1, width=20) #Label
        self.circuitLbl.grid(row=3, column = 0)

        self.getCircuit = IntVar()  
        self.getCircuit = Entry (master) ######## ENTRY BOX

        self.getCircuit.grid(row=3, column=1)        
            
        self.btn = Button(master, text="Calculate", bg="light grey", command=self.onButtonClick)
        self.btn.grid(row = 4,column=1)           

        self.conduitTypeResult = Label (master, text = "Conduit Type-> ", height=1, width=40) #Label
        self.conduitTypeResult.grid(row=0, column =2) 

        self.PVCResult = Label (master, text = "Cable Type-> ", height=2, width=25) #Label
        self.PVCResult.grid(row=1, column =2)    

        self.XLPE = Label (master, text = "", height=2, width=25) #Label
        self.XLPE.grid(row=2, column =2)  

        self.circuitNo = Label (master, text = "Number of Circuits-> ", height=2, width=25) #Label
        self.circuitNo.grid(row=3, column =2)   

        self.conduitResult = Label (master, text = "-", height=2, width=40, font='Helvetica 9 bold') #Label
        self.conduitResult.grid(row=4, column =2)    

        self.close = Button(master, text="Close", bg="light grey", command=master.destroy)
        self.close.grid(row = 5,column=0)

        self.disclaimerText = Label (master, text = """DISCLAIMER\n Please refer to the Table (can be accessed by clicking Open Table button)
         to confirm the results before practically applying the Number Of Conduits. Each output has not been tested thus 
         caution should be taken when using this program.\n
         REFERENCE: AS/NZ 3000:2018 Electrical Installations (known as the Australian/New Zeealand Wiring Rules"""
        ,font='Helvetica 9 bold') #Label
        self.disclaimerText.grid(row=6, rowspan=2, column=0, columnspan=3, sticky=W)     

        def openImage():
            control = Toplevel()
            canvas = Canvas(control, width=1309, height=761)
            canvas.pack(expand = YES, fill = BOTH)
            png1 = PhotoImage(file='C:\\Users\\Aditya.Verma\\Documents\\GitHub\\Table-c12-max-4-core---earth-cable-in-conduit\\Capture.PNG')
            canvas.create_image(0, 0, image = png1, anchor = NW)
            canvas.png1 = png1

        self.canvas = Canvas(master, width=99, height=30)
        self.canvas.grid(row=5, column=2)
        self.logo = PhotoImage(file='C:\\Users\\Aditya.Verma\\Documents\\GitHub\\Table-c10---max-single-core-sheathed-cables\\Lucid Logo.PNG')
        self.canvas.create_image(0, 0, image = self.logo, anchor = NW)
        self.canvas.logo = self.logo   

        self.openImage = Button(master, text="Open Table", bg="light grey", command=openImage)#image open button
        self.openImage.grid(row=5, column = 1)
        
        def reset():
             self.PVCResult.configure(text="" )
             self.conduitTypeResult.configure(text="-" )
             self.PVCResult.configure(text="-" )
             self.conduit.set("Heavy duty rigid UPVC conduit")
             self.cable.set("-")

        self.tableview = Button(master, text="Reset", bg="light grey", command=reset)
        self.tableview.grid(row = 4,column=0) 

    def onButtonClick(self):
        
        #get values
        def getConduitType(self):
            self.x = self.conduit.get()
            return self.x
        def getCable(self):
            self.x = self.cable.get()
            return self.x 
        def XLPE(self):
            self.x = self.cablePVC.get()
            return self.x              
        def getCircuitState(self):
            self.x = self.getCircuit.get()          
            return int(self.x) 

        if not self.getCircuit.get():
            self.conduitResult.configure(text="No. of Circuits has not been selected ", bg='orange' )      
              
        self.conduitTypeResult.configure(text="Conduit Type:  " + self.conduit.get(), font='Helvetica 9 bold')      
        
        if (getCable(self)=="-"):
            self.PVCResult.configure(text="" + self.cable.get(),font='Helvetica 9 bold' )
        else:
            self.PVCResult.configure(text="Cable Type:  " + self.cable.get(),font='Helvetica 9 bold' )

        if (XLPE(self)=="-"):
            self.XLPE.configure(text="" + self.cablePVC.get(),font='Helvetica 9 bold' )
        else:
            self.XLPE.configure(text="Cable Type:  " + self.cablePVC.get(),font='Helvetica 9 bold' ) 
                
        self.circuitNo.configure(text="Number of Circuits:  "+ self.getCircuit.get(), font='Helvetica 9 bold')

        def circuitNo(self):

            if (getConduitType(self)=="Heavy duty rigid UPVC conduit"):
                    
                if((getCable(self)=="1.5" or getCable(self)=="2.5") and getCircuitState(self)<= int("0")):
                    return "20"
                if((getCable(self)=="4" or getCable(self)=="6") and getCircuitState(self)<= int("0")):
                    return "20 or 25"
                if((getCable(self)=="1.5" or getCable(self)=="2.5") and getCircuitState(self)<= int("1")):
                    return "25 or 32"
                if((getCable(self)=="4" or getCable(self)=="6") and getCircuitState(self)<= int("1")):
                    return "32 or 40"
                if((getCable(self)=="1.5") and getCircuitState(self)<= int("3")):
                    return "40"
                if(getCable(self)=="2.5" and getCircuitState(self)<= int("2")):
                    return "40"
                
                if((getCable(self)=="1.5") and getCircuitState(self)<= int("5")):
                    return "50"
                if(getCable(self)=="2.5" and getCircuitState(self)<= int("4")):
                    return "50"
                if(getCable(self)=="4" and getCircuitState(self)<= int("3")):
                    return "50"
                if(getCable(self)=="6" and getCircuitState(self)<= int("2")):
                    return "50"

                if((getCable(self)=="1.5") and getCircuitState(self)<= int("9")):
                    return "63"
                if(getCable(self)=="2.5" and getCircuitState(self)<= int("6")):
                    return "63"
                if(getCable(self)=="4" and getCircuitState(self)<= int("5")):
                    return "63"
                if(getCable(self)=="6" and getCircuitState(self)<= int("4")):
                    return "63"
                
                if((getCable(self)=="1.5") and getCircuitState(self)<= int("16")):
                    return "80 (NZ)"
                if(getCable(self)=="2.5" and getCircuitState(self)<= int("12")):
                    return "80 (NZ)"
                if(getCable(self)=="4" and getCircuitState(self)<= int("9")):
                    return "80 (NZ)"
                if(getCable(self)=="6" and getCircuitState(self)<= int("8")):
                    return "80 (NZ)"
                
                if((getCable(self)=="1.5") and getCircuitState(self)<= int("18")):
                    return "80 (AUS)"
                if(getCable(self)=="2.5" and getCircuitState(self)<= int("14")):
                    return "80 (AUS)"
                if(getCable(self)=="4" and getCircuitState(self)<= int("10")):
                    return "80 (AUS)"
                if(getCable(self)=="6" and getCircuitState(self)<= int("9")):
                    return "80 (AUS)"
                
                if((getCable(self)=="1.5") and getCircuitState(self)<= int("29")):
                    return "100 (NZ)"
                if(getCable(self)=="2.5" and getCircuitState(self)<= int("21")):
                    return "100 (NZ)"
                if(getCable(self)=="4" and getCircuitState(self)<= int("16")):
                    return "100 (NZ)"
                if(getCable(self)=="6" and getCircuitState(self)<= int("14")):
                    return "100 (NZ)"
                
                if((getCable(self)=="1.5") and getCircuitState(self)<= int("31")):
                    return "100 (AUS)"
                if(getCable(self)=="2.5" and getCircuitState(self)<= int("23")):
                    return "100 (AUS)"
                if(getCable(self)=="4" and getCircuitState(self)<= int("18")):
                    return "100 (AUS)"
                if(getCable(self)=="6" and getCircuitState(self)<= int("15")):
                    return "100 (AUS)"
                
                if((getCable(self)=="1.5") and getCircuitState(self)<= int("47")):
                    return "125"
                if(getCable(self)=="2.5" and getCircuitState(self)<= int("35")):
                    return "125"
                if(getCable(self)=="4" and getCircuitState(self)<= int("27")):
                    return "125"
                if(getCable(self)=="6" and getCircuitState(self)<= int("23")):
                    return "125"
                
                if((getCable(self)=="1.5") and getCircuitState(self)<= int("61")):
                    return "150"
                if(getCable(self)=="2.5" and getCircuitState(self)<= int("46")):
                    return "150"
                if(getCable(self)=="4" and getCircuitState(self)<= int("35")):
                    return "150"
                if(getCable(self)=="6" and getCircuitState(self)<= int("31")):
                    return "150"
                
                if((getCable(self)=="10" or getCable(self)=="16" or getCable(self)=="25" or getCable(self)=="35"
                or getCable(self)=="50"  or getCable(self)=="70" or getCable(self)=="95") and getCircuitState(self)<= int("0")):
                    return "20, 25 or 32"
                
                if((getCable(self)=="25" or getCable(self)=="35"
                or getCable(self)=="50"  or getCable(self)=="70" or getCable(self)=="95") and getCircuitState(self)<= int("0")):
                    return "40"
                
                if((getCable(self)=="50"  or getCable(self)=="70" or getCable(self)=="95") and getCircuitState(self)<= int("0")):
                    return "50"
                
                if((getCable(self)=="10" or getCable(self)=="16") and getCircuitState(self)<= int("1")):
                    return "40"
                
                if((getCable(self)=="10" or getCable(self)=="16" or getCable(self)=="25" or getCable(self)=="35"
                or getCable(self)=="50")  and getCircuitState(self)<= int("1")):
                    return "50"
                
                if((getCable(self)=="16" or getCable(self)=="25" or getCable(self)=="35"
                or getCable(self)=="95") and getCircuitState(self)<= int("0")):
                    return "63"
                
                if(getCable(self)=="10" and getCircuitState(self)<= int("2")):
                    return "63"
                
                if(getCable(self)=="10" and getCircuitState(self)<= int("5")):
                    return "80 (NZ)"
                if(getCable(self)=="16" and getCircuitState(self)<= int("4")):
                    return "80 (NZ)"
                if(getCable(self)=="25" and getCircuitState(self)<= int("3")):
                    return "80 (NZ)"
                if(getCable(self)=="35" and getCircuitState(self)<= int("2")):
                    return "80 (NZ)"
                if(getCable(self)=="50" and getCircuitState(self)<= int("1")):
                    return "80 (NZ)"
                if(getCable(self)=="70" and getCircuitState(self)<= int("1")):
                    return "80 (NZ)"
                if(getCable(self)=="95" and getCircuitState(self)<= int("1")):
                    return "80 (NZ)"
                
                if(getCable(self)=="10" and getCircuitState(self)<= int("6")):
                    return "80 (AUS)"
                if(getCable(self)=="16" and getCircuitState(self)<= int("4")):
                    return "80 (AUS)"
                if(getCable(self)=="25" and getCircuitState(self)<= int("3")):
                    return "80 (AUS)"
                if(getCable(self)=="35" and getCircuitState(self)<= int("2")):
                    return "80 (AUS)"
                if(getCable(self)=="50" and getCircuitState(self)<= int("1")):
                    return "80 (AUS)"
                if(getCable(self)=="70" and getCircuitState(self)<= int("1")):
                    return "80 (AUS)"
                if(getCable(self)=="95" and getCircuitState(self)<= int("1")):
                    return "80 (AUS)"
                
                if(getCable(self)=="10" and getCircuitState(self)<= int("9")):
                    return "100 (NZ)"
                if(getCable(self)=="16" and getCircuitState(self)<= int("7")):
                    return "100 (NZ)"
                if(getCable(self)=="25" and getCircuitState(self)<= int("5")):
                    return "100 (NZ)"
                if(getCable(self)=="35" and getCircuitState(self)<= int("4")):
                    return "100 (NZ)"
                if(getCable(self)=="50" and getCircuitState(self)<= int("3")):
                    return "100 (NZ)"
                if(getCable(self)=="70" and getCircuitState(self)<= int("2")):
                    return "100 (NZ)"
                if(getCable(self)=="95" and getCircuitState(self)<= int("1")):
                    return "100 (NZ)"
                
                if(getCable(self)=="10" and getCircuitState(self)<= int("10")):
                    return "100 (AUS)"
                if(getCable(self)=="16" and getCircuitState(self)<= int("8")):
                    return "100 (AUS)"
                if(getCable(self)=="25" and getCircuitState(self)<= int("5")):
                    return "100 (AUS)"
                if(getCable(self)=="35" and getCircuitState(self)<= int("4")):
                    return "100 (AUS)"
                if(getCable(self)=="50" and getCircuitState(self)<= int("3")):
                    return "100 (AUS)"
                if(getCable(self)=="70" and getCircuitState(self)<= int("2")):
                    return "100 (AUS)"
                if(getCable(self)=="95" and getCircuitState(self)<= int("1")):
                    return "100 (AUS)"
                
                if(getCable(self)=="10" and getCircuitState(self)<= int("15")):
                    return "125"
                if(getCable(self)=="16" and getCircuitState(self)<= int("12")):
                    return "125"
                if(getCable(self)=="25" and getCircuitState(self)<= int("8")):
                    return "125"
                if(getCable(self)=="35" and getCircuitState(self)<= int("7")):
                    return "125"
                if(getCable(self)=="50" and getCircuitState(self)<= int("5")):
                    return "125"
                if(getCable(self)=="70" and getCircuitState(self)<= int("4")):
                    return "125"
                if(getCable(self)=="95" and getCircuitState(self)<= int("3")):
                    return "125"
                
                if(getCable(self)=="10" and getCircuitState(self)<= int("20")):
                    return "150"
                if(getCable(self)=="16" and getCircuitState(self)<= int("15")):
                    return "150"
                if(getCable(self)=="25" and getCircuitState(self)<= int("11")):
                    return "150"
                if(getCable(self)=="35" and getCircuitState(self)<= int("9")):
                    return "150"
                if(getCable(self)=="50" and getCircuitState(self)<= int("6")):
                    return "150"
                if(getCable(self)=="70" and getCircuitState(self)<= int("5")):
                    return "150"
                if(getCable(self)=="95" and getCircuitState(self)<= int("4")):
                    return "150"
                
                
                
                if((XLPE(self)=="16" or XLPE(self)=="25" or XLPE(self)=="35" or XLPE(self)=="50"
                or XLPE(self)=="70" or XLPE(self)=="95" or XLPE(self)=="120") and getCircuitState(self)<= int("0")):
                    return "20, 25 or 32"

                if((XLPE(self)=="25" or XLPE(self)=="35" or XLPE(self)=="50"
                or XLPE(self)=="70" or XLPE(self)=="95" or XLPE(self)=="120") and getCircuitState(self)<= int("0")):
                    return "40"

                if(XLPE(self)=="16" and getCircuitState(self)<= int("1")):
                    return "40"
                
                if((XLPE(self)=="50" or XLPE(self)=="70" or XLPE(self)=="95" or XLPE(self)=="120") and getCircuitState(self)<= int("0")):
                    return "50"
                
                if((XLPE(self)=="16" or XLPE(self)=="25" or XLPE(self)=="35") and getCircuitState(self)<= int("1")):
                    return "50"

                if(XLPE(self)=="16" and getCircuitState(self)<= int("3")):
                    return "63"
                if(XLPE(self)=="25" and getCircuitState(self)<= int("1")):
                    return "63"
                if(XLPE(self)=="35" and getCircuitState(self)<= int("1")):
                    return "63"
                if(XLPE(self)=="50" and getCircuitState(self)<= int("1")):
                    return "63"
                if(XLPE(self)=="70" and getCircuitState(self)<= int("1")):
                    return "63"
                if(XLPE(self)=="95" and getCircuitState(self)<= int("0")):
                    return "63"
                if(XLPE(self)=="120" and getCircuitState(self)<= int("0")):
                    return "63"
                
                if(XLPE(self)=="16" and getCircuitState(self)<= int("5")):
                    return "80 (NZ)"
                if(XLPE(self)=="25" and getCircuitState(self)<= int("3")):
                    return "80 (NZ)"
                if(XLPE(self)=="35" and getCircuitState(self)<= int("2")):
                    return "80 (NZ)"
                if(XLPE(self)=="50" and getCircuitState(self)<= int("1")):
                    return "80 (NZ)"
                if(XLPE(self)=="70" and getCircuitState(self)<= int("1")):
                    return "80 (NZ)"
                if(XLPE(self)=="95" and getCircuitState(self)<= int("1")):
                    return "80 (NZ)"
                if(XLPE(self)=="120" and getCircuitState(self)<= int("1")):
                    return "80 (NZ)"
                
                if(XLPE(self)=="16" and getCircuitState(self)<= int("6")):
                    return "80 (AUS)"
                if(XLPE(self)=="25" and getCircuitState(self)<= int("3")):
                    return "80 (AUS)"
                if(XLPE(self)=="35" and getCircuitState(self)<= int("2")):
                    return "80 (AUS)"
                if(XLPE(self)=="50" and getCircuitState(self)<= int("1")):
                    return "80 (AUS)"
                if(XLPE(self)=="70" and getCircuitState(self)<= int("1")):
                    return "80 (AUS)"
                if(XLPE(self)=="95" and getCircuitState(self)<= int("1")):
                    return "80 (AUS)"
                if(XLPE(self)=="120" and getCircuitState(self)<= int("1")):
                    return "80 (AUS)"

                if(XLPE(self)=="16" and getCircuitState(self)<= int("9")):
                    return "100 (NZ)"
                if(XLPE(self)=="25" and getCircuitState(self)<= int("6")):
                    return "100 (NZ)"
                if(XLPE(self)=="35" and getCircuitState(self)<= int("4")):
                    return "100 (NZ)"
                if(XLPE(self)=="50" and getCircuitState(self)<= int("3")):
                    return "100 (NZ)"
                if(XLPE(self)=="70" and getCircuitState(self)<= int("2")):
                    return "100 (NZ)"
                if(XLPE(self)=="95" and getCircuitState(self)<= int("1")):
                    return "100 (NZ)"
                if(XLPE(self)=="120" and getCircuitState(self)<= int("1")):
                    return "100 (NZ)"
                
                if(XLPE(self)=="16" and getCircuitState(self)<= int("10")):
                    return "100 (AUS)"
                if(XLPE(self)=="25" and getCircuitState(self)<= int("6")):
                    return "100 (AUS)"
                if(XLPE(self)=="35" and getCircuitState(self)<= int("5")):
                    return "100 (AUS)"
                if(XLPE(self)=="50" and getCircuitState(self)<= int("3")):
                    return "100 (AUS)"
                if(XLPE(self)=="70" and getCircuitState(self)<= int("2")):
                    return "100 (AUS)"
                if(XLPE(self)=="95" and getCircuitState(self)<= int("1")):
                    return "100 (AUS)"
                if(XLPE(self)=="120" and getCircuitState(self)<= int("1")):
                    return "100 (AUS)"
                
                if(XLPE(self)=="16" and getCircuitState(self)<= int("15")):
                    return "125"
                if(XLPE(self)=="25" and getCircuitState(self)<= int("9")):
                    return "125"
                if(XLPE(self)=="35" and getCircuitState(self)<= int("7")):
                    return "125"
                if(XLPE(self)=="50" and getCircuitState(self)<= int("6")):
                    return "125"
                if(XLPE(self)=="70" and getCircuitState(self)<= int("4")):
                    return "125"
                if(XLPE(self)=="95" and getCircuitState(self)<= int("3")):
                    return "125"
                if(XLPE(self)=="120" and getCircuitState(self)<= int("2")):
                    return "125"
                
                if(XLPE(self)=="16" and getCircuitState(self)<= int("20")):
                    return "150"
                if(XLPE(self)=="25" and getCircuitState(self)<= int("12")):
                    return "150"
                if(XLPE(self)=="35" and getCircuitState(self)<= int("10")):
                    return "150"
                if(XLPE(self)=="50" and getCircuitState(self)<= int("7")):
                    return "150"
                if(XLPE(self)=="70" and getCircuitState(self)<= int("5")):
                    return "150"
                if(XLPE(self)=="95" and getCircuitState(self)<= int("4")):
                    return "150"
                if(XLPE(self)=="120" and getCircuitState(self)<= int("3")):
                    return "150"
            
            if (getConduitType(self)=="Corflo conduit"):
                
                if((getCable(self)=="1.5") and getCircuitState(self)<= int("29")):
                    return "100 (NZ)"
                if(getCable(self)=="2.5" and getCircuitState(self)<= int("21")):
                    return "100 (NZ)"
                if(getCable(self)=="4" and getCircuitState(self)<= int("16")):
                    return "100 (NZ)"
                if(getCable(self)=="6" and getCircuitState(self)<= int("14")):
                    return "100 (NZ)"
                
                if((getCable(self)=="1.5") and getCircuitState(self)<= int("30")):
                    return "100 (AUS)"
                if(getCable(self)=="2.5" and getCircuitState(self)<= int("22")):
                    return "100 (AUS)"
                if(getCable(self)=="4" and getCircuitState(self)<= int("17")):
                    return "100 (AUS)"
                if(getCable(self)=="6" and getCircuitState(self)<= int("15")):
                    return "100 (AUS)"
                
                if((getCable(self)=="1.5") and getCircuitState(self)<= int("45")):
                    return "125"
                if(getCable(self)=="2.5" and getCircuitState(self)<= int("33")):
                    return "125"
                if(getCable(self)=="4" and getCircuitState(self)<= int("26")):
                    return "125"
                if(getCable(self)=="6" and getCircuitState(self)<= int("22")):
                    return "125"
                
                if((getCable(self)=="1.5") and getCircuitState(self)<= int("59")):
                    return "150."
                if(getCable(self)=="2.5" and getCircuitState(self)<= int("44")):
                    return "150."
                if(getCable(self)=="4" and getCircuitState(self)<= int("34")):
                    return "150."
                if(getCable(self)=="6" and getCircuitState(self)<= int("29")):
                    return "150"
                
                if(getCable(self)=="10" and getCircuitState(self)<= int("9")):
                    return "100 (NZ)"
                if(getCable(self)=="16" and getCircuitState(self)<= int("7")):
                    return "100 (NZ) or 100 (AUS)"
                if(getCable(self)=="25" and getCircuitState(self)<= int("5")):
                    return "100 (NZ) or 100 (AUS)"
                if(getCable(self)=="35" and getCircuitState(self)<= int("4")):
                    return "100 (NZ) or 100 (AUS)"
                if(getCable(self)=="50" and getCircuitState(self)<= int("3")):
                    return "100 (NZ) or 100 (AUS)"
                if(getCable(self)=="70" and getCircuitState(self)<= int("2")):
                    return "100 (NZ) or 100 (AUS)"
                if(getCable(self)=="95" and getCircuitState(self)<= int("1")):
                    return "100 (NZ) or 100 (AUS)" 
                
                if(getCable(self)=="10" and getCircuitState(self)<= int("10")):
                    return "100 (AUS)"

                if(getCable(self)=="10" and getCircuitState(self)<= int("14")):
                    return "125"
                if(getCable(self)=="16" and getCircuitState(self)<= int("11")):
                    return "125"
                if(getCable(self)=="25" and getCircuitState(self)<= int("8")):
                    return "125"
                if(getCable(self)=="35" and getCircuitState(self)<= int("6")):
                    return "125"
                if(getCable(self)=="50" and getCircuitState(self)<= int("5")):
                    return "125"
                if(getCable(self)=="70" and getCircuitState(self)<= int("3")):
                    return "125"
                if(getCable(self)=="95" and getCircuitState(self)<= int("2")):
                    return "125"             

                if(getCable(self)=="10" and getCircuitState(self)<= int("19")):
                    return "150"
                if(getCable(self)=="16" and getCircuitState(self)<= int("15")):
                    return "150"
                if(getCable(self)=="25" and getCircuitState(self)<= int("1")):
                    return "150"
                if(getCable(self)=="35" and getCircuitState(self)<= int("9")):
                    return "150"
                if(getCable(self)=="50" and getCircuitState(self)<= int("6")):
                    return "150"
                if(getCable(self)=="70" and getCircuitState(self)<= int("5")):
                    return "150"
                if(getCable(self)=="95" and getCircuitState(self)<= int("3")):
                    return "150"      

                if(XLPE(self)=="16" and getCircuitState(self)<= int("9")):
                    return "100 (NZ)"
                if(XLPE(self)=="25" and getCircuitState(self)<= int("6")):
                    return "100 (NZ)"
                if(XLPE(self)=="35" and getCircuitState(self)<= int("4")):
                    return "100 (NZ)"
                if(XLPE(self)=="50" and getCircuitState(self)<= int("6")):
                    return "100 (NZ)"
                if(XLPE(self)=="70" and getCircuitState(self)<= int("5")):
                    return "100 (NZ)"
                if(XLPE(self)=="95" and getCircuitState(self)<= int("1")):
                    return "100 (NZ)"
                if(XLPE(self)=="120" and getCircuitState(self)<= int("1")):
                    return "100 (NZ)"
                
                if(XLPE(self)=="16" and getCircuitState(self)<= int("10")):
                    return "100 (AUS)"
                if(XLPE(self)=="25" and getCircuitState(self)<= int("6")):
                    return "100 (AUS)"
                if(XLPE(self)=="35" and getCircuitState(self)<= int("5")):
                    return "100 (AUS)"
                if(XLPE(self)=="50" and getCircuitState(self)<= int("3")):
                    return "100 (AUS)"
                if(XLPE(self)=="70" and getCircuitState(self)<= int("2")):
                    return "100 (AUS)"
                if(XLPE(self)=="95" and getCircuitState(self)<= int("1")):
                    return "100 (AUS)"
                if(XLPE(self)=="120" and getCircuitState(self)<= int("1")):
                    return "100 (AUS)"
                
                if(XLPE(self)=="16" and getCircuitState(self)<= int("15")):
                    return "125"
                if(XLPE(self)=="25" and getCircuitState(self)<= int("9")):
                    return "125"
                if(XLPE(self)=="35" and getCircuitState(self)<= int("7")):
                    return "125"
                if(XLPE(self)=="50" and getCircuitState(self)<= int("5")):
                    return "125"
                if(XLPE(self)=="70" and getCircuitState(self)<= int("4")):
                    return "125"
                if(XLPE(self)=="95" and getCircuitState(self)<= int("3")):
                    return "125"
                if(XLPE(self)=="120" and getCircuitState(self)<= int("2")):
                    return "125"
                
                if(XLPE(self)=="16" and getCircuitState(self)<= int("19")):
                    return "150"
                if(XLPE(self)=="25" and getCircuitState(self)<= int("12")):
                    return "150"
                if(XLPE(self)=="35" and getCircuitState(self)<= int("9")):
                    return "150"
                if(XLPE(self)=="50" and getCircuitState(self)<= int("7")):
                    return "150"
                if(XLPE(self)=="70" and getCircuitState(self)<= int("5")):
                    return "150"
                if(XLPE(self)=="95" and getCircuitState(self)<= int("4")):
                    return "150"
                if(XLPE(self)=="120" and getCircuitState(self)<= int("3")):
                    return "150"
                

            if (getConduitType(self)=="Medium duty corrugated"):
                
                if((getCable(self)=="1.5" or getCable(self)=="2.5" or getCable(self)=="4" or getCable(self)=="6") and getCircuitState(self)<= int("0")):
                    return "20"  
                
                if((getCable(self)=="1.5") and getCircuitState(self)<= int("1")):
                    return "25"  

                if((getCable(self)=="2.5" or getCable(self)=="4" or getCable(self)=="6") and getCircuitState(self)<= int("0")):
                    return "25"   

                if((getCable(self)=="1.5" or getCable(self)=="2.5" or getCable(self)=="4" or getCable(self)=="6") and getCircuitState(self)<= int("1")):
                    return "32" 

                if((getCable(self)=="2.5" or getCable(self)=="4" or getCable(self)=="6") and getCircuitState(self)<= int("1")):
                    return "40"        
                
                if((getCable(self)=="1.5") and getCircuitState(self)<= int("2")):
                    return "20"  
                
                if(getCable(self)=='10' and getCircuitState(self) <= int("7")):
                    return "80 (NZ)"

            if (getConduitType(self)=="Medium duty rigid UPVC conduit"):
                if((getCable(self)=="1.5" or getCable(self)=="2.5" or getCable(self)=="4" or getCable(self)=="6") and getCircuitState(self)<= int("0")):
                    return "16"     
                
                if((getCable(self)=="2.5" or getCable(self)=="4" or getCable(self)=="6") and getCircuitState(self)<= int("0")):
                    return "20" 
                
                if((getCable(self)=="1.5" or getCable(self)=="2.5" or getCable(self)=="4" or getCable(self)=="6") and getCircuitState(self)<= int("1")):
                    return "32" 
                
                if((getCable(self)=="1.5" or getCable(self)=="2.5" or getCable(self)=="4") and getCircuitState(self)<= int("1")):
                    return "25" 
                
                if((getCable(self)=="4" or getCable(self)=="6") and getCircuitState(self)<= int("1")):
                    return "40" 
                
                if((getCable(self)=="1.5") and getCircuitState(self)<= int("1")):
                    return "20" 
                
                if(getCable(self)=="6" and getCircuitState(self)<= int("0")):
                    return "25" 
                
                if((getCable(self)=="1.5") and getCircuitState(self)<= int("3")):
                    return "40" 
                if(getCable(self)=="2.5" and getCircuitState(self)<= int("2")):
                    return "40" 

                if((getCable(self)=="1.5") and getCircuitState(self)<= int("5")):
                    return "50"
                if(getCable(self)=="2.5" and getCircuitState(self)<= int("4")):
                    return "50"
                if(getCable(self)=="4" and getCircuitState(self)<= int("3")):
                    return "50"
                if(getCable(self)=="6" and getCircuitState(self)<= int("2")):
                    return "50"

                if((getCable(self)=='1.5' or getCable(self)=="2.5" or getCable(self)=='4' or getCable(self)=='4') and getCircuitState(self) <= int("0")):
                    return "20"
                
                if((getCable(self)=='10' or getCable(self)=='16' or getCable(self)=='25' or getCable(self)=='4') and getCircuitState(self) <= int("0")):
                    return "16, 20, 25 or 32"

                if(getCable(self)=="25" and getCircuitState(self)<= int("0")):
                    return "40"
                
                if((getCable(self)=="16" or getCable(self)=='10') and getCircuitState(self)<= int("1")):
                    return "40"
                
                if((getCable(self)=="16" or getCable(self)=='10' or getCable(self)=='25') and getCircuitState(self)<= int("1")):
                    return "50"
                                    
            else:
                return "Invalid input, please check again"
        
        self.conduitResult.configure(text="Conduit Size:\n" + circuitNo(self), bg='green2')
        if (circuitNo(self)=="Invalid input, please check again"):
            self.conduitResult.configure(bg='red')

                   
master = Tk()
master.title("Number of Conduits. Table C12")
master.geometry("700x325")
app = Application(master)

master.mainloop()
