students_list = ["Güven Eren", "Yasin Aktürk", "Batuhan Dümen", "Abdullah Halıcı", "Sedat Serbezler"]
grades_list = []

homework_list = [100, 57, 54, 45, 80]
midterm_list = [100, 87, 46, 10, 5]
final_list = [95, 21, 78, 20, 10]


def student_average_calculation():
    evaluate = 0
    successful_student = "Successful student"
    for i in range(5):
        summ = homework_list[i] + midterm_list[i] + final_list[i]
        result = summ / 3
        print("Result of the ", i + 1, "student", int(result))

        if result > evaluate:
            evaluate = result
            successful_student = students_list[i]
    print("First:", int(evaluate), "With GPA ", successful_student, "Congratulations :)", end="\n")
    grades_list = list(zip(final_list, homework_list, midterm_list))
    list1 = dict(zip(students_list, grades_list))

    print("Students names and scores", list1)


student_average_calculation()
