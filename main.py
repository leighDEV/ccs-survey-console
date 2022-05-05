import menu as m

while True:
    print("==Menu==")
    print("[A]nswer Survey\n[S]how Current Statistics\n[E]xit")

    choice = input("Enter choice: ")
    if choice == 'A':
        s = m.Student(m.Student.name, m.Student.age, m.Student.sex, m.Student.course, m.Student.answers)
        m.Student.get_info(s)
        m.Student.answer_survey(s)
    elif choice == 'S':
        m.current_stats()
    elif choice == 'E':
        m.exit_program()
        break
    else:
        print("Wrong input.")
    print()
