import tkinter as tk
import sqlite3
from datetime import datetime

# Database
connection = sqlite3.connect("workout.db")# Create and connect to the database
cursor = connection.cursor()# Connects the database

# Create the rows in the database
# id is the primary key
myTable = """CREATE TABLE IF NOT EXISTS exercises(
    id INTEGER PRIMARY KEY,
    exerciseName TEXT NOT NULL,
    weight INTEGER NOT NULL,
    repetitions INTEGER NOT NULL,
    date TEXT NOT NULL)"""
cursor.execute(myTable)

# Placeholder data
cursor.execute("INSERT INTO exercises (exerciseName, weight, repetitions, date)"
"    VALUES ('Bench Press', 100, 10, '2025-03-08')")







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



        
        self.showFrame(HomePage)

        self.homeButton = tk.Button(self.topBar, text="Home",
         bg="grey9", fg="white", font=("Arial", 12),
         command=lambda: self.showFrame(HomePage))
        self.homeButton.pack(side="left", padx=10)


        self.settingsButton = tk.Button(self.topBar, text="Settings",
         bg="grey9", fg="white", font=("Arial", 12),
         command=lambda: self.showFrame(Settings))
        self.settingsButton.pack(side="right",padx=10)

        self.addExerciseButton = tk.Button(
            self.bottomBar, text="+", font=("Arial", 20, "bold"), 
            bg="grey9", fg="white", width=3, height=1, 
            relief="ridge", borderwidth=5,# Border styling
            command=lambda: self.showFrame(ExerciseList))
        self.addExerciseButton.pack(pady=10)# pady raises it from the bottom a bit




    def showFrame(self, page):
        # If page is a string (exercise name)
        if isinstance(page, str) and page in self.exercises:
            # Check if we've already created this exercise page
            if page not in self.frames:
                # Create the frame
                exerciseFrame = ExercisePage(self.container, self, 
                                             name=page, 
                                             group=self.exercises[page])# Create an instance of the page
                self.frames[page] = exerciseFrame
                exerciseFrame.grid(row=0, column=0, sticky="nsew")
            
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
         command=lambda: controller.showFrame(ChestGroup))
        self.chestGroup.pack(pady=10)# pady raises it from the bottom a bit

        self.BackGroup = tk.Button(self,text="Back",
         bg="grey9", fg="white", font=("Arial", 12),
         command=lambda: controller.showFrame(BackGroup))
        self.BackGroup.pack(pady=10)# pady raises it from the bottom a bit

        self.LegsGroup = tk.Button(self,text="Legs",
         bg="grey9", fg="white", font=("Arial", 12),
         command=lambda: controller.showFrame(LegsGroup))
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
         command=lambda: controller.showFrame(ExerciseList))
        self.BackButton.pack(side="top",pady=5)

        self.benchPressBb = tk.Button(self, text="Barbell Bench Press",
         bg="grey9", fg="white", font=("Arial", 14),
         command=lambda: controller.showFrame("Barbell Bench Press"))
        self.benchPressBb.pack(side="top",pady=10,padx=30)
        
        self.benchPressDb = tk.Button(self, text="Dumbbell Bench Press",
         bg="grey9", fg="white", font=("Arial", 14),
         command=lambda: controller.showFrame("Dumbbell Bench Press"))
        self.benchPressDb.pack(side="top",pady=10)

        self.pushUps = tk.Button(self, text="Push-Ups",
         bg="grey9", fg="white", font=("Arial", 14),
         command=lambda: controller.showFrame("Push-Ups"))
        self.pushUps.pack(side="top",pady=10)

        self.pecFly = tk.Button(self, text="Pec Fly",
         bg="grey9", fg="white", font=("Arial", 14),
         command=lambda: controller.showFrame("Pec Fly"))
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
         command=lambda: controller.showFrame(ExerciseList))
        self.BackButton.pack(side="top",pady=5)

        self.deadlift = tk.Button(self, text="Deadlift",
         bg="grey9", fg="white", font=("Arial", 14),
         command=lambda: controller.showFrame("Deadlift"))
        self.deadlift.pack(side="top",pady=10)
        

        self.latPulldown = tk.Button(self, text="Lat Pulldown",
         bg="grey9", fg="white", font=("Arial", 14),
         command=lambda: controller.showFrame("Lat Pulldown"))
        self.latPulldown.pack(side="top",pady=10)

        self.lowRow = tk.Button(self, text="Low Row",
         bg="grey9", fg="white", font=("Arial", 14),
         command=lambda: controller.showFrame("Low Row"))
        self.lowRow.pack(side="top",pady=10)

        self.barbellRow = tk.Button(self, text="Barbell Row",
         bg="grey9", fg="white", font=("Arial", 14),
         command=lambda: controller.showFrame("Barbell Row"))
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
         command=lambda: controller.showFrame(ExerciseList))
        self.BackButton.pack(side="top",pady=5)

        self.barbellSquats = tk.Button(self, text="Barbell Squats",
         bg="grey9", fg="white", font=("Arial", 14),
         command=lambda: controller.showFrame("Barbell Squats"))
        self.barbellSquats.pack(side="top",pady=10)

        self.splitSquats = tk.Button(self, text="Split Squats",
         bg="grey9", fg="white", font=("Arial", 14),
         command=lambda: controller.showFrame("Split Squats"))
        self.splitSquats.pack(side="top",pady=10)

        self.legRaises = tk.Button(self, text="Leg Raises",
         bg="grey9", fg="white", font=("Arial", 14),
         command=lambda: controller.showFrame("Leg Raises"))
        self.legRaises.pack(side="top",pady=10)

        self.hamstringCurls = tk.Button(self, text="Hamstring Curls",
         bg="grey9", fg="white", font=("Arial", 14),
         command=lambda: controller.showFrame("Hamstring Curls"))
        self.hamstringCurls.pack(side="top",pady=10)


"""
1.	Create a dictionary to store each of the exercises.
2.	Loop through the dictionary and create instances of exercise page for each exercise
3.	Store each of these in self.frames 
4.	Map the pages over
5.	Open them with showFrame
"""

class ExercisePage(tk.Frame):
    def __init__(self,parent,controller,name="", group=""):
        super().__init__(parent,bg="grey12")
        self.name = name
        self.group = group# Can be used to organize data according to the muscle group

        exercisePageLabel = tk.Label(self, text=self.name, font=("Arial", 24), bg="grey12", fg="white")
        exercisePageLabel.pack(side="top", pady=20,padx=0)# Places a label with the exercise name at the top

        """
        Weights & Repetitions Textbox, increment button and decrement button.
        I have made smaller frames to put these in to help organize.
        """

        # Textbox
        weightInputFrame = tk.Frame(self, bg="grey12", width=120, height=80)
        weightInputFrame.pack(side="top", pady=10)
        weightInputFrame.pack_propagate(False)  # Prevents the frame from resizing to fit its children
        
        self.weightInput = tk.Text(weightInputFrame, font=("Arial", 32))# Create the text widget inside the fixed frame
        self.weightInput.tag_configure("center", justify="center") 
        self.weightInput.insert("1.0", "0","center")# Set 0 as the default value
        self.weightInput.pack(fill="both", expand=True)
        self.weightInput.bind("<KeyPress>", self.validate_integer_input)
        
        # Buttons
        weightFrame = tk.Frame(self, bg="grey12")
        weightFrame.pack(side="top", pady=10)# Create a frame for the weight increment/decrement button
        self.weightValue = tk.IntVar(value=0)# Default value

        weightDecrement = tk.Button(weightFrame, text="-", font=("Arial", 20), command=self.decrementWeight)
        weightDecrement.pack(side="left")
        weightIncrement = tk.Button(weightFrame, text="+", font=("Arial", 20),command=self.incrementWeight)
        weightIncrement.pack(side="left")  

        """
        Same funciton as above, just for the repetitions button
        """

        # Textbox for reps
        repsInputFrame = tk.Frame(self, bg="grey12", width=120, height=80)# Create the textbox frame for reps
        repsInputFrame.pack(side="top", pady=10)
        repsInputFrame.pack_propagate(False)  

        self.repsInput = tk.Text(repsInputFrame, font=("Arial", 32))
        self.repsInput.tag_configure("center", justify="center") 
        self.repsInput.insert("1.0", "0","center")# Set 0 as the default value
        self.repsInput.pack(fill="both", expand=True)
        self.repsInput.bind("<KeyPress>", self.validate_integer_input)

        # Buttons for reps
        repsFrame = tk.Frame(self, bg="grey12")
        repsFrame.pack(side="top", pady=10)# Create a frame for the reps increment/decrement button
        self.repsValue = tk.IntVar(value=0)# Default value
        

        repsDecrement = tk.Button(repsFrame, text="-", font=("Arial", 20), command=self.decrementReps)
        repsDecrement.pack(side="left")
        repsIncrement = tk.Button(repsFrame, text="+", font=("Arial", 20),command=self.incrementReps)
        repsIncrement.pack(side="left")       

        # Save the set. Need to connect it to the database
        saveButton = tk.Button(self, text="Save", font=("Arial", 20),command=self.saveSet)
        saveButton.pack(side="top", pady=15)

    def incrementWeight(self):
        self.updateTextbox(self.weightInput, 5)

    def decrementWeight(self):
        self.updateTextbox(self.weightInput, -5)

    def incrementReps(self):
        self.updateTextbox(self.repsInput, 1)

    def decrementReps(self):
        self.updateTextbox(self.repsInput, -1)

    def updateTextbox(self, textbox, change):
        try:
            currentValue = int(textbox.get("1.0", "end").strip())
        except ValueError:
            currentValue = 0  # Default to 0 if invalid input
        
        newValue = max(0, currentValue + change)  # Prevents negative values
        textbox.delete("1.0", "end")# Delete first line at the beginning of the text box
        textbox.insert("1.0", str(newValue), "center")# Insert at the first line (hence 1.0)

    def saveSet(self):
        weight = self.weightInput.get("1.0", "end").strip()
        reps = self.repsInput.get("1.0", "end").strip()
        date = datetime.now().strftime("%Y-%m-%d")

        cursor.execute("INSERT INTO exercises (exerciseName, weight, repetitions, date) Values (?, ?, ?, ?)",
        (self.name, weight, reps, date))

        connection.commit()# Commit the changes to the database (else they are stored in memory)
        """cursor.execute("SELECT * FROM exercises")
        results = cursor.fetchall()
        print(results)"""

    def validate_integer_input(self, event):
        if event.char.isdigit() or event.keysym in ("BackSpace", "Delete", "Left", "Right"):
            # keysym allows these keys to be used as well as integers
            return
        else:
            return "break"# Cancels the keypress

if __name__ == "__main__":# Convention that indicates that this file is meant to be run
    app = App()
    app.mainloop()
