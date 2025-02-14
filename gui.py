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

        for F in (HomePage, Settings,ExerciseList,# Loop through the pages
        ChestGroup,BackGroup,LegsGroup):
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
         command=lambda: self.show_frame(Settings))
        self.settingsButton.pack(side="right",padx=10)

        self.addExerciseButton = tk.Button(
            self.bottomBar, text="+", font=("Arial", 20, "bold"), 
            bg="grey9", fg="white", width=3, height=1, 
            relief="ridge", borderwidth=5,# Border styling
            command=lambda: self.show_frame(ExerciseList))
        self.addExerciseButton.pack(pady=10)# pady raises it from the bottom a bit




    def show_frame(self, page):
        frame = self.frames[page]
        frame.tkraise()# Display the frame


    
    
class HomePage(tk.Frame):
    def __init__(self,parent,controller):
        super().__init__(parent,bg="grey12")
        label = tk.Label(self, text="Home", font=("Arial", 24), bg="grey12", fg="white")
        label.pack(side="top", pady=20,padx=150)

class Settings(tk.Frame):
    def __init__(self, parent,controller):
        super().__init__(parent, bg="grey12")  # Create a frame inside parent (container)

        # Page title
        label = tk.Label(self, text="Settings", font=("Arial", 24), bg="grey12", fg="white")
        label.pack(pady=20,padx=150)  # Add some space

        # Button to switch back to Home Page


class ExerciseList(tk.Frame):
    def __init__(self,parent,controller):
        super().__init__(parent,bg="grey12")



        label = tk.Label(self, text="Exercises", font=("Arial", 24), bg="grey12", fg="white")
        label.pack(side="top", pady=20,padx=150)

        # Buttons for the exercise groups
        self.chestGroup = tk.Button(self,text="Chest",
         bg="grey9", fg="white", font=("Arial", 12),
         command=lambda: controller.show_frame(ChestGroup))
        self.chestGroup.pack(pady=10)# pady raises it from the bottom a bit

        self.BackGroup = tk.Button(self,text="Back",
         bg="grey9", fg="white", font=("Arial", 12),
         command=lambda: controller.show_frame(BackGroup))
        self.BackGroup.pack(pady=10)# pady raises it from the bottom a bit

        self.LegsGroup = tk.Button(self,text="Legs",
         bg="grey9", fg="white", font=("Arial", 12),
         command=lambda: controller.show_frame(LegsGroup))
        self.LegsGroup.pack(pady=10)# pady raises it from the bottom a bit
        


"""
Frames for the exercise pages
"""

class ChestGroup(tk.Frame):
    def __init__(self,parent,controller):
        super().__init__(parent,bg="grey12")
        label = tk.Label(self, text="Chest Exercises",
        font=("Arial",24), bg="grey12", fg="white")
        label.pack(side="top",pady=20,padx=50)

        self.BackButton = tk.Button(self, text="Back",
         bg="grey9", fg="white", font=("Arial", 12),
         command=lambda: controller.show_frame(ExerciseList))
        self.BackButton.pack(side="top",pady=5)

        self.benchPressBb = tk.Button(self, text="Barbell Bench Press",
         bg="grey9", fg="white", font=("Arial", 14),
         command=lambda: controller.show_frame(HomePage))
        self.benchPressBb.pack(side="top",pady=10)
        
        self.benchPressDb = tk.Button(self, text="Dumbbell Bench Press",
         bg="grey9", fg="white", font=("Arial", 14),
         command=lambda: controller.show_frame(HomePage))
        self.benchPressDb.pack(side="top",pady=10)

        self.pushUps = tk.Button(self, text="Push-Ups",
         bg="grey9", fg="white", font=("Arial", 14),
         command=lambda: controller.show_frame(HomePage))
        self.pushUps.pack(side="top",pady=10)

        self.pecFly = tk.Button(self, text="Pec Fly",
         bg="grey9", fg="white", font=("Arial", 14),
         command=lambda: controller.show_frame(HomePage))
        self.pecFly.pack(side="top",pady=10)


class BackGroup(tk.Frame):
    def __init__(self,parent,controller):
        super().__init__(parent,bg="grey12")
        label = tk.Label(self, text="Back Exercises",font=("Arial",24), bg="grey12", fg="white")
        label.pack(side="top",pady=20,padx=50)

        self.BackButton = tk.Button(self, text="Back",
         bg="grey9", fg="white", font=("Arial", 12),
         command=lambda: controller.show_frame(ExerciseList))
        self.BackButton.pack(side="top",pady=5)

        self.deadlift = tk.Button(self, text="Deadlift",
         bg="grey9", fg="white", font=("Arial", 14),
         command=lambda: controller.show_frame(HomePage))
        self.deadlift.pack(side="top",pady=10)
        

        self.latPulldown = tk.Button(self, text="Lat Pulldown",
         bg="grey9", fg="white", font=("Arial", 14),
         command=lambda: controller.show_frame(HomePage))
        self.latPulldown.pack(side="top",pady=10)

        self.lowRow = tk.Button(self, text="Low Row",
         bg="grey9", fg="white", font=("Arial", 14),
         command=lambda: controller.show_frame(HomePage))
        self.lowRow.pack(side="top",pady=10)

        self.barbellRow = tk.Button(self, text="Barbell Row",
         bg="grey9", fg="white", font=("Arial", 14),
         command=lambda: controller.show_frame(HomePage))
        self.barbellRow.pack(side="top",pady=10)


class LegsGroup(tk.Frame):
    def __init__(self,parent,controller):
        super().__init__(parent,bg="grey12")
        label = tk.Label(self, text="Legs Exercises",font=("Arial",24), bg="grey12", fg="white")
        label.pack(side="top",pady=20,padx=50)

        self.BackButton = tk.Button(self, text="Back",
         bg="grey9", fg="white", font=("Arial", 12),
         command=lambda: controller.show_frame(ExerciseList))
        self.BackButton.pack(side="top",pady=5)

        self.barbellSquats = tk.Button(self, text="Barbell Squats",
         bg="grey9", fg="white", font=("Arial", 14),
         command=lambda: controller.show_frame(HomePage))
        self.barbellSquats.pack(side="top",pady=10)

        self.splitSquats = tk.Button(self, text="Split Squats",
         bg="grey9", fg="white", font=("Arial", 14),
         command=lambda: controller.show_frame(HomePage))
        self.splitSquats.pack(side="top",pady=10)

        self.legRaises = tk.Button(self, text="Leg Raises",
         bg="grey9", fg="white", font=("Arial", 14),
         command=lambda: controller.show_frame(HomePage))
        self.legRaises.pack(side="top",pady=10)

        self.hamstringCurls = tk.Button(self, text="Hamstring Curls",
         bg="grey9", fg="white", font=("Arial", 14),
         command=lambda: controller.show_frame(HomePage))
        self.hamstringCurls.pack(side="top",pady=10)
  

if __name__ == "__main__":
    app = App()
    app.mainloop()
