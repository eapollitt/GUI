import tkinter


class myGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        

        self.label1 = tkinter.Label(self.main_window, text='Hello World!')
        self.label2 = tkinter.Label(self.main_window, text='This is my GUI program')
    
    #packit controls what part of the screen these elements will show on 
     #default is top


        self.label1.pack()
        self.label2.pack()

        tkinter.mainloop() #sustains the window on a loop until the user closes it out
        #the rest of the code does not get executed until you're finished with that window

my_gui = myGUI()

print("I am done")

#text box shows up on top left of computer screen, and when you close it out, I am done prints in the terminal
