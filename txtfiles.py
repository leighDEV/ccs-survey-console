import os.path


class TextFiles:
    def __init__(self, name, age, sex, course, answers):
        self._name = name
        self._age = age
        self._sex = sex
        self._course = course
        self._answers = answers

    def switch_ans(self, a):
        match a:
            case 1:
                return "Strongly Disagree"
            case 2:
                return "Disagree"
            case 3:
                return "Neutral"
            case 4:
                return "Agree"
            case 5:
                return "Strongly Agree"
            case _:
                return "Wrong input"

    def write(self, a):
        info_path = "C:\OneDrive\Documents\.School\Code\PycharmProjects\ccs-survey-console\extfiles\info.txt"
        if os.path.exists(info_path):
            f_info = open(info_path, "a")

            i = 0
            f_info.write(f"Student #{i + 1}")
            f_info.write(f"Name  : {self._name}")
            f_info.write(f"Age   : {self._age}")
            f_info.write(f"Sex   : {self._sex}")
            f_info.write(f"Course: {self._course}")

            f_info.write("Answers:")
            for a in self._answers:
                self.switch_ans(a)
        else:
            print("Info path does not exists.")

        results_path = "C:\OneDrive\Documents\.School\Code\PycharmProjects\ccs-survey-console\extfiles\results.txt"
        if os.path.exists(results_path):
            f_results = open(results_path, "a")
            f_results.write(a)

        age_path = "C:\OneDrive\Documents\.School\Code\PycharmProjects\ccs-survey-console\extfiles\age.txt"
        if os.path.exists(age_path):
            f_age = open(age_path, "a")
            f_age.write(self._age)

        sex_path = "C:\OneDrive\Documents\.School\Code\PycharmProjects\ccs-survey-console\extfiles\sex.txt"
        if os.path.exists(sex_path):
            f_sex = open(sex_path, "a")
            f_sex.write(self._sex)

        course_path = "C:\OneDrive\Documents\.School\Code\PycharmProjects\ccs-survey-console\extfiles\course.txt"
        if os.path.exists(course_path):
            f_course = open(course_path, "a")
            f_course.write(self._course)

        stats_path = "C:\OneDrive\Documents\.School\Code\PycharmProjects\ccs-survey-console\extfiles\stats.txt"
        if os.path.exists(stats_path):
            stats_path = open(stats_path, "w")
