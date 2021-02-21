#Modules
from tkinter import*
from tkinter import ttk


#----------------------------------------
class MyQuiz():
    def __init__(self,root):
        self.Start = Frame(root)
        self.Start.grid()
        self.Title = Label(self.Start, text="English Quiz", font = 30)
        self.Title.grid(columnspan = 2)

        self.StartQuiz = ttk.Button(self.Start, text = "Start Quiz", command = NextPage)
        self.StartQuiz.grid(column = 1)


        

class StartQuiz():
    def __init__(self,root):
        self.StartQuiz = Frame(root)
        Quiz.Start.grid_forget()
        self.StartQuiz.grid()
        #Radiobutton
        self.v = StringVar(root, "1")
        values = {"Level 1" : "1", "Level 2" : "2", "Level 3" : "3"}
        

        self.ChooseLevel = Label(self.StartQuiz, text = "Choose Level", bg = "black", fg = "white", font = 30)
        self.ChooseLevel.grid(columnspan = 3)
        for (text, value) in values.items():
            Radiobutton(self.StartQuiz, text = text, variable = self.v,  value = value, indicator = 0,background = "light blue").grid()
        
        self.NextBut = ttk.Button(self.StartQuiz, text = "Next", command = lambda: NextPages(self.v))
        self.NextBut.grid(row = 3)


def NextPage():
  global LevelChoosing
  LevelChoosing = StartQuiz(root)
  
#Difficulty 1 -----------------------------------------------------------------------------------------
class Level1:
    def __init__(self, root):
        LevelChoosing.StartQuiz.grid_forget()
        self.Level1 = Frame(root)
        self.Level1.grid()

        self.Title = Label(self.Level1, text = "Level 2")
        self.Title.grid(columnspan = 2, row = 0,)
        self.Question = Label(self.Level1)
        self.Question.grid(column = 1, row = 2)
        self.QEntry = Entry(self.Level1)
        self.QEntry.grid(row = 3, column = 2) 
        

        def NextQuestion():
                pass
        
        self.Next_But = ttk.Button(self.Level1, text = "Next", command = NextQuestion)
        self.Next_But.grid(row = 4, column = 0)

        Q_Entry = self.QEntry.get()
        
        Q_List = ["How many weeks are there in a year?","If John had 50 candies and he ate 40, what does he have?",
                  "Can you count how many days on your finger is in a leap year?","If Brook Book booked bookings twice",
                  "how many books booking did book book?","What does OOP stand for?"]
        Q_Answer = ["53", "Diabetes", "No, because you only have 10 fingers", "Twice", "Object Oriented Programming"]

        def Submit_Ans():
            if Q_Entry == "":
                self.Question.config(text = "Correct!")
                self.Next_But.grid()
                pass
            else:
                self.Question.config(text = "Bad!")
                self.Next_But.grid()
                pass
        self.Submit_But = ttk.Button(self.Level1, text= "Submit", command =  Submit_Ans)
        self.Submit_But.grid(row = 4, column = 1)
lvl1 = None

def NextPages(value_chosen):
  if value_chosen.get() == "1":
    lvl1 = Level1(root)
  else:
    pass

#runs when the name of the program is recognized as True
if __name__ == "__main__":
    root = Tk()
    root.title("English Quiz")
    Quiz = MyQuiz(root)
    root.geometry("250x200+420+160")
  
