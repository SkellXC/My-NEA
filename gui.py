import tkinter as tk

class App(tk.Tk):
    # Inherit from Tkinter so it behaves like a normal Tkinter window
    def __init__(self):
        super().__init__()# calls the constructor for the Tkinter (parent) class
        self.title("Workout Tracker")
        self.geometry("400x620")# UI size


        self.container = tk.Frame(self)# creates a container to holder widgets
        self.container.pack(fill=tk.BOTH, expand=True)
        # Acts like a wrapper for the different pages

        self.frames = {}                      

    def show_frame(self, page):
        frame = self.frames[page]
        frame.tkraise()
        # This function rasies the selected frame to the
        # front of the window.




if __name__ == "__main__":
    app = App()
    app.mainloop()