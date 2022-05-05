import sys


class Student:
    def __init__(self, name, age, sex, course, answers):
        self._name = name
        self._age = age
        self._sex = sex
        self._course = course
        self._answers = answers

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @property
    def sex(self):
        return self._sex

    @property
    def course(self):
        return self._course

    @property
    def answers(self):
        return self._answers

    def get_info(self):
        print("Student's Information")
        self._name = input("Name: ")
        self._age = int(input("Age: "))
        self._sex = input("Sex: ")
        self._course = input("Course: ")

    def answer_survey(self):
        print("\nDirections: Please indicate how much you agree or disagree "
              "with each of these statements. Just put the number only.")
        print("5 - Strongly Agree\n4 - Agree\n3 - Neutral\n2 - Disagree\n1 - Strongly Disagree")
        print("Statements:")

        print("\nDuring this new normal, online class, in the midst of the pandemic," +
              "\nI've noticed any changes in my physique, particularly in terms of weight.")
        self._answers[0] = int(input("Answer: "))

        print("")
        self._answers[1] = int(input("Answer: "))

        print("")
        self._answers[2] = int(input("Answer: "))

        print("")
        self._answers[3] = int(input("Answer: "))

        print("")
        self._answers[4] = int(input("Answer: "))

        print("")
        self._answers[5] = int(input("Answer: "))

        print("")
        self._answers[6] = int(input("Answer: "))

        print("")
        self._answers[7] = int(input("Answer: "))

        print("")
        self._answers[8] = int(input("Answer: "))

        print("")
        self._answers[9] = int(input("Answer: "))


def current_stats():
    print("Current Stats here")


def exit_program():
    print("Thank you for using this program.")
    sys.exit()
