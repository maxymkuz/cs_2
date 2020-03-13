import time
import sys
import os


class Subject:
    """ A class for each subject"""

    def __init__(self):
        """
        Initializes the grade and skills and deadlines
        of a single subject
        """
        self.grade = 0
        self.skill = 0
        self.deadlines = None

    def get_grade(self):
        return self.grade

    def get_skill(self):
        return self.skill

    def add_skill(self):
        if self.skill >= 5:
            self.skill += 1
        else:
            self.skill += 2

    def set_grade(self, grade):
        self.grade = round(grade, 2)

    def check_answer(self, day, ipt_answer):
        """ Checks if user answered question successfully
        and adds points according to student's skill level
        """
        max_grade = self.deadlines[day][0]
        skill_grade = max_grade * (self.skill + 2) / 10
        if ipt_answer == self.deadlines[day][-1]:
            total_score = skill_grade * 0.6 + max_grade * 0.4
            self.grade += round(total_score, 2)
            print(f"Your answer is correct. Your score is {total_score} out of {max_grade}")
        else:
            self.grade += round(skill_grade * 0.6, 2)
            print(f"Your answer is NOT correct, correct answer is "
                  f"{self.deadlines[day][-1]}. "
                  f"Your score is {skill_grade * 0.6} out of {max_grade}\n")
        time.sleep(0.5)
        input("Press enter to continue: ")


class Programming(Subject):
    """ Class that represents an programming subject
    """
    def __init__(self):
        """ Initializes an instance of this subject
        """
        super().__init__()
        self.name = "PROGRAMMING"
        # Those are important dates
        self.deadlines = {4: (10, "test on lecture",
                              "[Andriy Romaniuk]: Яке значення буде отримано \
 в результаті обчислення виразу 4 != 4.0?", "False"),
                          6: (20, "test",
                              "[Andriy Romaniuk]: Що буде отримано в результаті "
                              "виконання pow(2, 2, 2)?", "0"),
                          9: (30, "middle",
                              """   [Andriy Romaniuk]:
x = [12.1, 34.0]
print(len(' '.join(list(map(str, x)))""", "9"),
                          12: (30, "Final exam",
                               """[Andriy Romaniuk]: 
Class A:
    def __init__(self, x=3):
        self._x = x

Class B(A):
    def __init__(self):
        super().__init__(5)
    
    def display(self):
        print(self._x)

def main():
    obj = B()
    obj.display()

main()""", "9")}


class Calculus(Subject):
    """ Class that represents an Calculus subject
    """

    def __init__(self):
        """ Initializes an instance of this subject
        """

        super().__init__()
        self.name = "CALCULUS"
        # Those are important dates for student
        self.deadlines = {5: (30, "Usual test on Logical thinking",
                              """[Stepan Feduniak]:
    У мами — двоє синів. У кожного з них є сестра. Скільки дітей у мами?

Відповідь написати одним числом""", "3"),
                          10: (30, "Usual test on Logical thinking", """
[Stepan Feduniak]:
    П’ять музик у дудки дули,
    вони дули п’ять годин.
    Поміркуйте, як там було,
    скільки в дудку дув один?

Відповідь написати в годинах одним числом""", "5"),
                          15: (40, "Final exam",
                               """[Stepan Feduniak]:
    5 гномиків вишикувалися для гри. Білосніжка викликала третього гномика.
    Скільки гномиків залишилось у шерензі?

Відповідь написати одним числом
""", "4")}


class Student:
    """ Represents a player with his skills and grades"""

    def __init__(self, programming, calculus):
        """
        :param programming: Subject
        :param calculus: Subject
        """
        self.health = 100
        self.subjects = [programming, calculus]

    def describe_subjects(self, day):
        """
        Is used to return all information needed in a string
        about subjects and user statistics in a given way
        :param day: int
        :return: string
        """
        res = []
        for subject in self.subjects:
            deadlines = [f"    {i - day} day(s) left for the "
                         f"{subject.deadlines[i][1]}. Maximum grade: "
                         f"{subject.deadlines[i][0]} points"
                         for i in subject.deadlines if i > day and i - day < 7]
            deadlines.insert(0, "\n" + "~" * 45 +
                             f"\n{len(res)}. {subject.name}. Current grade: {subject.grade}\n" \
                             f"Current skill: {subject.skill} out of 10\n  Deadlines:")
            res.append("\n".join(deadlines))
        return "\n".join(res)

    def all_subjects(self):
        """
        Returns a list of subjects
        :return: list
        """
        return [subject.name for subject in self.subjects]

    def all_subjects_with_index(self):
        """
        Returns a list of subjects and it's indexes
        :return: list
        """
        return [f"{i}.{self.subjects[i].name}" for i in range(len(self.subjects))]

    def is_test(self, day):
        """
        Checks if there is a test on given day
        and returns subject if yes, else False
        :param day:
        :return: Subject
        """
        for subject in self.subjects:
            if day in subject.deadlines:
                return subject
        return False


def start_game():
    """ None -> None
    Function to start a game session
    """
    # Clears the terminal of prior code for a properly formatted title screen.
    os.system('clear')
    # Prints the title.
    print('#' * 52)
    print('# Welcome to the text-based student simulator game #')
    print("#              Author: Maxym Kuzyshyn              #")
    print('#' * 52)
    print("                   .: Play :.                  ")
    # print("                   .: Help :.                  ")
    print("                   .: Quit :.                  ")
    usr_ipt = input("> ")
    if usr_ipt.lower() == "play":
        os.system('clear')
        print("""
###############################################################################
# You are playing for a usual student in an University.                       #
#                                                                             #
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
#                                                                             #
#     Your semester is starting soon. Your task is to survive this semester.  #
# In order to survive you have to have 60+ points from ALL subjects you have. #
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
#                                                                             #
#     Your performance on test depends on your skill level on that subject,   #
# which you can gain through everyday work on it. Also your grade depends     #
# on your own knowledge and luck! So good luck!!!                             #
#                                                                             #""")
        ipt = input("Enter any key to start: ")
        return True
    elif usr_ipt.lower() == "quit":
        sys.exit()


def finish_game(student):
    """(Student) -> None
    Output function for the results of the game
    """
    os.system('clear')
    lost_subjects = []
    print(f"You have finished the semester\n~~~~~~~~~~~~~~~~~~~~~~~~~~\nYour final score:")
    for subject in student.subjects:
        if subject.grade < 60:
            lost_subjects.append((subject.name, subject.grade))
        print(f"{subject.name}. Skill level: {subject.skill}. Final grade: {subject.grade}")
    if lost_subjects:
        print("\nYou have LOST!!!!! You haven't managed to survive this semester. Now you die!\n")
        for i in lost_subjects:
            print(f"You have failed the {i[0]} with the grade {i[1]} out of 60")
    else:
        print("\nCONGRATULATIONS you have WON the game.\nYou have managed "
              "to survive this semester in the University!")
