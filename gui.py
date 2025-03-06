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
        ChestGroup,BackGroup,LegsGroup,
        ExercisePage):
            frame = F(self.container, self) # Creates an instance of the frame
            self.frames[F] = frame # Then stores it in the dictionary
            frame.grid(row=0, column=0, sticky="nsew") # Stacks the frames back

        self.exercises = {

            "Barbell Bench Press": "Chest",
            "Dumbbell Bench Press": "Chest",
            "Push-Ups": "Chest",
            "Pec Fly": "Chest",
            "Deadlift": "Back",
            "Lat Pulldown": "Back",
            "Low Row": "Back",
            "Barbell Row": "Back",
            "Barbell Squats": "Legs",
            "Split Squats": "Legs",
            "Leg Raises": "Legs",
            "Hamstring Curls": "Legs"
        }



        
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
        # If page is a string (exercise name)
        if isinstance(page, str) and page in self.exercises:
            # Check if we've already created this exercise page
            if page not in self.frames:
                # Create the frame
                exercise_frame = ExercisePage(self.container, self, 
                                             name=page, 
                                             group=self.exercises[page])# Create an instance of the page
                self.frames[page] = exercise_frame
                exercise_frame.grid(row=0, column=0, sticky="nsew")
            
            frame = self.frames[page]
        else:
            # Original behavior for class-based pages
            frame = self.frames[page]
            
        frame.tkraise()

    
    
class HomePage(tk.Frame):
    def __init__(self,parent,controller):
        super().__init__(parent,bg="grey12")
        homeLabel = tk.Label(self, text="Home", font=("Arial", 24), bg="grey12", fg="white")
        homeLabel.pack(side="top", pady=20,padx=150)

class Settings(tk.Frame):
    def __init__(self, parent,controller):
        super().__init__(parent, bg="grey12")  # Create a frame inside parent (container)

        # Page title
        settingsLabel = tk.Label(self, text="Settings", font=("Arial", 24), bg="grey12", fg="white")
        settingsLabel.pack(pady=20,padx=150)  # Add some space

        # Button to switch back to Home Page


class ExerciseList(tk.Frame):
    def __init__(self,parent,controller):
        super().__init__(parent,bg="grey12")

        exercisesLabel = tk.Label(self, text="Exercises", font=("Arial", 24), bg="grey12", fg="white")
        exercisesLabel.pack(side="top", pady=20,padx=150)

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
    # Class holds all the buttons for
    # Chest exercises.
    def __init__(self,parent,controller):
        super().__init__(parent,bg="grey12")
        chestLabel = tk.Label(self, text="Chest Exercises",
        font=("Arial",24), bg="grey12", fg="white")
        chestLabel.pack(side="top",pady=20,padx=50)

        self.BackButton = tk.Button(self, text="Back",
         bg="grey9", fg="white", font=("Arial", 12),
         command=lambda: controller.show_frame(ExerciseList))
        self.BackButton.pack(side="top",pady=5)

        self.benchPressBb = tk.Button(self, text="Barbell Bench Press",
         bg="grey9", fg="white", font=("Arial", 14),
         command=lambda: controller.show_frame("Barbell Bench Press"))
        self.benchPressBb.pack(side="top",pady=10,padx=30)
        
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
            # Class holds all the buttons for
            # Back exercises.
        super().__init__(parent,bg="grey12")
        backLabel = tk.Label(self, text="Back Exercises",font=("Arial",24), bg="grey12", fg="white")
        backLabel.pack(side="top",pady=20,padx=50)

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
            # Class holds all the buttons for
            # Leg exercises.
        super().__init__(parent,bg="grey12")
        legsLabel = tk.Label(self, text="Legs Exercises",font=("Arial",24), bg="grey12", fg="white")
        legsLabel.pack(side="top",pady=20,padx=50)

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


"""
1.	Create a dictionary to store each of the exercises.
2.	Loop through the dictionary and create instances of exercise page for each exercise
3.	Store each of these in self.frames 
4.	Map the pages over
5.	Open them with show_frame
"""

class ExercisePage(tk.Frame):
    def __init__(self,parent,controller,name="", group=""):
        super().__init__(parent,bg="grey12")
        self.name = name
        self.group = group# Can be used to organize data according to the muscle group

        exercisePageLabel = tk.Label(self, text=self.name, font=("Arial", 24), bg="grey12", fg="white")
        exercisePageLabel.pack(side="top", pady=20,padx=0)# Places a label with the exercise name at the top

        weightInputFrame = tk.Frame(self, bg="grey12", width=120, height=80)
        weightInputFrame.pack(side="top", pady=10)
        weightInputFrame.pack_propagate(False)  # Prevents the frame from resizing to fit its children
        
        self.weightInput = tk.Text(weightInputFrame, font=("Arial", 32))# Create the text widget inside the fixed frame
        self.weightInput.tag_configure("center", justify="center") 
        self.weightInput.insert("1.0", "0","center")# Set 0 as the default value
        self.weightInput.pack(fill="both", expand=True)
        

        repsInputFrame = tk.Frame(self, bg="grey12", width=120, height=80)# Create the textbox frame for reps
        repsInputFrame.pack(side="top", pady=10)
        repsInputFrame.pack_propagate(False)  

        self.repsInput = tk.Text(repsInputFrame, font=("Arial", 32))
        self.repsInput.tag_configure("center", justify="center") 
        self.repsInput.insert("1.0", "0","center")# Set 0 as the default value
        self.repsInput.pack(fill="both", expand=True)




if __name__ == "__main__":# Convention that indicates that this file is meant to be run
    app = App()
    app.mainloop()
