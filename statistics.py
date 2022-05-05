import re
import os.path


def read():
    age_path = "C:\OneDrive\Documents\.School\Code\PycharmProjects\ccs-survey-console\extfiles\\age.txt"
    if os.path.exists(age_path):
        f_age = open(age_path, "r")
        eighteen = re.findall("age", age_path)
        print(eighteen)

read()