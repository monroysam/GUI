import tkinter
import tkinter.messagebox

class GIU:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.main_window.geometry("500x200")
        self.main_window.title("Frames and buttons")


        # creates two frames, one top and one bottom
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        self.radio_var = tkinter.IntVar()

        #set the intVar variable to 1
        self.radio_var.set(1)

        self.rb1 = tkinter.Radiobutton(self.top_frame, text = "option 1", variable = self.radio_var, value = 1)
        self.rb2 = tkinter.Radiobutton(self.top_frame, text = "option 2", variable = self.radio_var, value = 2)
        self.rb3 = tkinter.Radiobutton(self.top_frame, text = "option 3", variable = self.radio_var, value = 3)

        self.rb1.pack()
        self.rb2.pack()
        self.rb3.pack()

        self.ok_button = tkinter.Button(self.bottom_frame, text = "OK", command = self.show_choice)
        self.quit_button = tkinter.Button(self.bottom_frame, text = "Quit", command = self.main_window.destroy)

        self.ok_button.pack(side = "left")
        self.quit_button.pack(side = "left")


        self.top_frame.pack()
        self.bottom_frame.pack()


        tkinter.mainloop() 

    def show_choice(self):
        tkinter.messagebox.showinfo("Selection", "You hvae selected option " + str(self.radio_var.get()))

kconv = GIU()

print("Moving on...") 