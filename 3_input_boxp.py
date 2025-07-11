import tkinter
import tkinter.messagebox

class KiloConverter:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.main_window.geometry("500x200")
        self.main_window.title("Frames and buttons")


        # creates two frames, one top and one bottom
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)


        self.prompt_label = tkinter.Label(self.top_frame, text = "Enter a distance in kilometers")

        self.kilo_entry = tkinter.Entry(self.top_frame, width = 10)

        self.prompt_label.pack(side = "left")
        self.kilo_entry.pack(side = "left")

        self.calc_button = tkinter.Button(self.bottom_frame, text = "Convert", command = self.convert)
        self.quit_button = tkinter.Button(self.bottom_frame, text = "Quit", command = self.main_window.destroy)

        self.calc_button.pack(side = "left")
        self.quit_button.pack(side = "left")

        self.top_frame.pack()
        self.bottom_frame.pack()


        tkinter.mainloop() 

    def convert(self):
        kilo = float(self.kilo_entry.get())

        miles = round(kilo * 0.6214, 2)

        tkinter.messagebox.showinfo("Result", str(kilo) + " kilometers is equal to " + str(miles) + " miles.")


kconv = KiloConverter()

print("Moving on...") 