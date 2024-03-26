import tkinter

class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk() #the "main_window" can be any text but the tkinter.Ty() has to be that

        self.main_window.geometry("500x200")
        self.main_window.title("Label Demo")

        self.label1 = tkinter.Label(self.main_window, text = "Hello World!") #creates a label widget
        self.label2 = tkinter.Label(self.main_window, text = "This is my GUI program")

        self.label1.pack()#must use the "pack()" meathod (tells GUI what element to use on screen)
        self.label2.pack()#makes wigdet visiable when called

        #self.label1.pack(side = "left") # - will move text left
        #self.label2.pack(side = "right") # - will move text right

        ##!!!WHAT IS THE DEFAULT LOCATION OF THE PACK MEATHOD - TOP!!!

        tkinter.mainloop() #only when the main window is closed either through submitting it or closing it out, then the code will continue


    #create an instance of the line GUI class
        
my_gui = MyGUI() #create the instance

print("Moving on...") 