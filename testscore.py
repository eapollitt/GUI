import tkinter
import tkinter.messagebox

#five frames 
#frames woudl be top and elements would be left 


class myGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        
        self.main_window.geometry('500x200')
        self.main_window.title("Label Demo")
        


        self.topframe = tkinter.Frame(self.main_window)
        self.topmiddleframe = tkinter.Frame(self.main_window)
        self.middleframe = tkinter.Frame(self.main_window)
        self.bottommiddleframe = tkinter.Frame(self.main_window)
        self.bottomframe = tkinter.Frame(self.main_window)


        self.entry1 = tkinter.StringVar()#created a string variable
        self.entry2 = tkinter.StringVar()
        self.entry3 = tkinter.StringVar()

        self.promptlabel1 = tkinter.Label(self.topframe, text='Enter the score for test 1:')
        self.entry1 = tkinter.Entry(self.topframe, width=10)
        self.promptlabel2 = tkinter.Label(self.topmiddleframe, text='Enter the score for test 2:')
        self.entry2 = tkinter.Entry(self.topmiddleframe, width=10)
        self.promptlabel3 = tkinter.Label(self.middleframe, text='Enter the score for test 2:')
        self.entry3 = tkinter.Entry(self.middleframe, width=10)
        self.promptlabel4 = tkinter.Label(self.bottommiddleframe, text = "Average:")


        self.promptlabel1.pack(side='left')
        self.entry1.pack(side='right')
        self.promptlabel2.pack(side='left')
        self.entry2.pack(side='right')
        self.promptlabel3.pack(side='left')
        self.entry3.pack(side='right')
        self.promptlabel4.pack(side='left')
       

        self.result= tkinter.StringVar() 
        #self.average = tkinter.Label(self.bottommiddleframe,text=f"str(result)")
        #self.desc_label = tkinter.Label(self.bottommiddleframe,text=str(f"{result}"))


        #self.entry1 = tkinter.StringVar()#created a string variable
        #self.entry2 = tkinter.StringVar()
        #self.entry3 = tkinter.StringVar()

        #self.desc_label = tkinter.Label(self.bottommiddleframe,text="Average:")
        #self.avgerage = tkinter.Entry(self.bottommiddleframe,textvariable=self.avg_var.get())

        #self.desc_label.pack(side='left')
        #self.avgerage.pack(side='right')


        self.avg_button = tkinter.Button(self.bottomframe, text='Average',command=self.convert)
        self.quitbutton = tkinter.Button(self.bottomframe, text="Quit", command=self.main_window.destroy)

        self.avg_button.pack(side='left')
        self.quitbutton.pack(side='right')
     
        self.topframe.pack()
        self.topmiddleframe.pack()
        self.middleframe.pack()
        self.bottommiddleframe.pack()
        self.bottomframe.pack()

        
    #packit controls what part of the screen these elements will show on 
     #default is top
    
        tkinter.mainloop()


        #self.mybutton = tkinter.Button(self.main_window, text='Convert',command=self.convert)
        #self.quitbutton = tkinter.Button(self.main_window, text="Quit", command=self.main_window.destroy)
          #sustains the window on a loop until the user closes it out
        #the rest of the code does not get executed until you're finished with that window

    def convert(self):
        self.test1 = float(self.entry1.get())
        self.test2 = float(self.entry2.get())
        self.test3 = float(self.entry3.get()) 
        self.total = (self.test1 + self.test2 + self.test3)/3
        self.result = tkinter.Label(self.bottommiddleframe,text=str(self.total))
        self.result.pack(side='right')
        #get is a built in function ; accessor method
        #average = (total/3)
        #self.result = tkinter.Label(self.bottommiddleframe,text=f"str(result)")
        

        #avg_var = round((test1 + test2 + test3)/3 ,2)

        #self.avgerage = tkinter.Label(self.bottommiddleframe,textvariable=str(self.result.get()))
        #self.avgerage.pack(side='right')

        #tkinter.messagebox.showinfo("Average:" +str(avg_variable))

    #def do_something(self):
        #message = "You have selected:\n"
        
        #if self.cb1_var.get() ==1:
            #message += "option 1\n"
        #if self.cb2_var.get() ==1:
            #message += "option 2\n"
        #if self.cb3_var.get() ==1:
            #message += "option 3\n"
        
        #tkinter.messagebox.showinfo("Response",message)
    
        #top bottom left and right or options and top is the default if you dont specify
        
         #sustains the window on a loop until the user closes it out
        #the rest of the code does not get executed until you're finished with that window

my_gui = myGUI()

print("I am done")

#text box shows up on top left of computer screen, and when you close it out, I am done prints in the terminal
