import tkinter as tk

class App(tk.Tk):
    # Inherit from Tkinter so it behaves like a normal Tkinter window
    def __init__(self):
        super().__init__()# calls the constructor for the Tkinter (parent) class
        self.title("Workout Tracker")
        self.geometry("400x620")# UI size

        # self.configure(bg="grey12") use if background isn't matching

        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)# Allow for horizontal streching

        

        self.topBar = tk.Frame(self,height=50, bg="grey9")# creates a top bar
        self.topBar.grid(row=0, column = 0, sticky="nsew")# Sticks it to the top but lets it stretch to the width

        self.bottomBar = tk.Frame(self,height=75, bg="grey9")# Copy of above for bottom
        self.bottomBar.grid(row=2,column=0, sticky="nsew")

        self.container = tk.Frame(self, bg="grey12")# creates a container to holder widgets
        self.container.grid(row=1,column=0, sticky="nsew")

        # buttons should be after container

        self.homeButton = tk.Button(self.topBar, text="Home",
         bg="grey9", fg="white", font=("Arial", 12))
        self.homeButton.pack(side="left", padx=10)


        
        self.addExerciseButton = tk.Button(
            self.bottomBar, text="+", font=("Arial", 20, "bold"), 
            bg="grey9", fg="white", width=3, height=1, 
            relief="ridge", borderwidth=5)# Border styling
        self.addExerciseButton.pack(pady=10)# pady raises it from the bottom a bit

        self.settingsButton = tk.Button(self.topBar, text="Settings",
         bg="grey9", fg="white", font=("Arial", 12))
        self.settingsButton.pack(side="right",padx=10)


        self.frames = {}                      

    def show_frame(self, page):
        frame = self.frames[page]
        frame.tkraise()
        # This function rasies the selected frame to the
        # front of the window.

    



if __name__ == "__main__":
    app = App()
    app.mainloop()