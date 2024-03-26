import tkinter
import tkinter.messagebox

class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.main_window.geometry("500x200")
        self.main_window.title("Frames and buttons")


        # creates two frames, one top and one bottom
        self.top_frame = tkinter.Frame(self.main_window)
        self.middle_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)


        self.label1 = tkinter.Label(self.top_frame, text = "John")
        self.label2 = tkinter.Label(self.top_frame, text = "James")
        self.label3 = tkinter.Label(self.top_frame, text = "Jack")

        self.label1.pack(side = "left")
        self.label2.pack(side = "left")
        self.label3.pack(side = "left")

        self.label4 = tkinter.Label(self.middle_frame, text = "Jill")
        self.label5 = tkinter.Label(self.middle_frame, text = "Jamie")
        self.label6 = tkinter.Label(self.middle_frame, text = "Jennifer")        

        self.label4.pack(side = "left")
        self.label5.pack(side = "left")
        self.label6.pack(side = "left")

        self.my_button = tkinter.Button(self.bottom_frame, text = "Click me!", command = self.do_something)
        self.quit_button = tkinter.Button(self.bottom_frame, text = "Quit", command = self.main_window.destroy)

        self.top_frame.pack()
        self.middle_frame.pack()
        self.bottom_frame.pack()

        self.my_button.pack(side = "right")
        self.quit_button.pack(side = "left")

        tkinter.mainloop() 

    def do_something(self):
        tkinter.messagebox.showinfo("Response", "Thanks for clicking the button!")

my_gui = MyGUI()

print("Moving on...") 