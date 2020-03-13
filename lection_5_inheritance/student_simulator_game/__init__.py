from . student_simulator_classes import *
import sys
import time

student = Student(Programming(), Calculus())

start_game()
day, days_in_semester = 0, 16


while day < days_in_semester:
    os.system('clear')
    print(f"DAY {day}")
    for character in student.describe_subjects(day):
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.005)

    # Checking if a student has a test on this day
    test_subject = student.is_test(day)
    if test_subject:
        print(f"\n~~~~~~~~~~~~~~~~~~~~~~~~~~\n"
              f"Today is the test from {test_subject.name}. "
              f"You have to answer the following question:\n")
        print(test_subject.deadlines[day][-2])
        ipt_answer = input("> ")
        test_subject.check_answer(day, ipt_answer)

    else:  # If not then s/he can study today
        print(f"\n\nThere are {len(student.all_subjects())} to study:"
              f" {', '.join(student.all_subjects_with_index())}."
              f" Enter index from 0 to {len(student.all_subjects()) - 1}")
        ipt_subject = input("> ")
        if ipt_subject in student.all_subjects():
            for subject in student.subjects:
                if subject.name == ipt_subject:
                    print(f"Studying {ipt_subject}...")
                    time.sleep(3)
                    previous_skill = student.subjects[int(ipt_subject)]
                    subject.add_skill()
                    print(f"You've studied {ipt_subject} today. "
                          f"Your skill has grown from {previous_skill} to {subject.skill}")
                    break
        elif ipt_subject in [str(i) for i in range(len(student.subjects))]:
            previous_skill = student.subjects[int(ipt_subject)].skill

            student.subjects[int(ipt_subject)].add_skill()
            print(f"You've studied {student.subjects[int(ipt_subject)].name} today. "
                  f"Your skill has grown from {previous_skill} to {student.subjects[int(ipt_subject)].skill}")  # TODO make timer like 3 sec to study it
        elif ipt_subject.lower() == "quit":
            sys.exit()
        else:
            print("You entered an unappropriate value")
            time.sleep(3)
            continue

    time.sleep(2.5)
    day += 1


finish_game(student)
