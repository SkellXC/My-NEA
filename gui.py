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







        self.frames = {}

        for F in (HomePage, Settings):# Loop through the pages
            frame = F(self.container, self) # Creates an instance of the frame
            self.frames[F] = frame # Then stores it in the dictionary
            frame.grid(row=0, column=0, sticky="nsew") # Stacks the frames back
        
        self.show_frame(HomePage)

        self.homeButton = tk.Button(self.topBar, text="Home",
         bg="grey9", fg="white", font=("Arial", 12),
         command=lambda: self.show_frame(HomePage))
        
        self.homeButton.pack(side="left", padx=10)

        self.settingsButton = tk.Button(self.topBar, text="Settings",
         bg="grey9", fg="white", font=("Arial", 12),
         command=lambda: self.show_frame(Settings)
         )
        
        self.settingsButton.pack(side="right",padx=10)

    def show_frame(self, page):
        frame = self.frames[page]
        frame.tkraise()# Display the frame


    
    
class HomePage(tk.Frame):
    def __init__(self,parent,controller):
        super().__init__(parent,bg="grey12")
        label = tk.Label(self, text="Home", font=("Arial", 24), bg="grey12", fg="white")
        label.pack(side="top", pady=20,padx=150)

class Settings(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="grey12")  # Create a frame inside parent (container)

        # Page title
        label = tk.Label(self, text="Settings", font=("Arial", 24), bg="grey12", fg="white")
        label.pack(pady=20,padx=150)  # Add some space

        # Button to switch back to Home Page


if __name__ == "__main__":
    app = App()
    app.mainloop()