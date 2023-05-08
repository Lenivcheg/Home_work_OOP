class Student:

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lec(self, lecturer, course, grade):
        if (isinstance(lecturer, Lecturer) and course in self.finished_courses or
                self.courses_in_progress and course in lecturer.courses_attached):
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return print('Ошибка Студента')

    def __str__(self):
        info = f'Имя: {self.name}\nФамилия: {self.surname}\nСредний балл :{self.a_score()}\n' \
               f'Курсы в процессе обучения: {self.courses_in_progress}\nЗавершенные курсы :{self.finished_courses}'
        return info

    def a_score(self):
        for lesson, grade in self.grades.items():
            rating = sum(grade) / len(grade)
            return rating

    def __lt__(self, other):
        if not isinstance(other, Student):
            return f'\nНе является Студентом'
        return self.a_score() < other.a_score()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def a_score(self):
        for lesson, grade in self.grades.items():
            rating_l = sum(grade) / len(grade)
            return rating_l

    def __str__(self):
        info = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции:{self.a_score()}'
        return info

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return f'\nНе является Лектором'

        return self.a_score() < other.a_score()


class Reviewer(Mentor):
    @staticmethod
    def rate_hw(student, course, grade):
        if isinstance(student, Student) and course in student.finished_courses or student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return print('Ошибка Ривьера')

    def __str__(self):
        info = f'Имя: {self.name}\nФамилия: {self.surname}'
        return info


# Наполнение экземпляров классов для тестов.
lec_1 = Lecturer('Mikel', 'Nelson')
lec_1.courses_attached.append('Git')
lec_1.courses_attached.append('Python')
lec_1.courses_attached.append('SQL')

lec_2 = Lecturer('Nikol', 'Watson')
lec_2.courses_attached.append('Git')
lec_2.courses_attached.append('SQL')
lec_2.courses_attached.append('Framework')

stu_1 = Student('Sirena', 'Gnomish', 'female')
stu_1.finished_courses.append('Git')
stu_1.finished_courses.append('Framework')
stu_1.courses_in_progress.append('Python')
stu_1.courses_in_progress.append('SQL')

stu_2 = Student('Geogr', 'Smirnov', 'male')
stu_2.finished_courses.append('Python')
stu_2.finished_courses.append('SQL')
stu_2.courses_in_progress.append('Git')
stu_2.courses_in_progress.append('Framework')

rev_1 = Reviewer('Artur', 'Morgan')
rev_2 = Reviewer('Kristian', 'Boring')

#  Наполнение оценок по курсам студентами
stu_1.rate_lec(lec_1, 'Python', 8)
stu_1.rate_lec(lec_1, 'Git', 9)
stu_1.rate_lec(lec_1, 'SQL', 7)
stu_1.rate_lec(lec_2, 'SQL', 6)
stu_1.rate_lec(lec_2, 'Framework', 10)
stu_1.rate_lec(lec_2, 'Git', 6)

stu_2.rate_lec(lec_1, 'Python', 7)
stu_2.rate_lec(lec_1, 'Git', 8)
stu_2.rate_lec(lec_1, 'SQL', 9)
stu_2.rate_lec(lec_2, 'SQL', 10)
stu_2.rate_lec(lec_2, 'Framework', 2)
stu_2.rate_lec(lec_2, 'Git', 9)

#  Наполнения оценок ревьюерами студентам
rev_1.rate_hw(stu_1, 'Git', 4)
rev_1.rate_hw(stu_1, 'SQL', 7)
rev_1.rate_hw(stu_1, 'Framework', 5)
rev_1.rate_hw(stu_1, 'Python', 10)

rev_1.rate_hw(stu_2, 'Git', 10)
rev_1.rate_hw(stu_2, 'SQL', 5)
rev_1.rate_hw(stu_2, 'Framework', 9)
rev_1.rate_hw(stu_2, 'Python', 4)

rev_2.rate_hw(stu_1, 'Git', 9)
rev_2.rate_hw(stu_1, 'SQL', 6)
rev_2.rate_hw(stu_1, 'Framework', 8)
rev_1.rate_hw(stu_1, 'Python', 5)

rev_2.rate_hw(stu_2, 'Git', 9)
rev_2.rate_hw(stu_2, 'SQL', 6)
rev_2.rate_hw(stu_2, 'Framework', 8)
rev_2.rate_hw(stu_2, 'Python', 7)
student_list = [stu_2, stu_1]
lecturer_list = [lec_1, lec_2]


def average_score_s(s_list, course):
    res, num = 0, 0
    for student in s_list:
        if course in student.finished_courses or student.courses_in_progress:
            res += sum(student.grades[course])
            num += len(student.grades[course])
        return print(f'Средняя оценка студентов по {course} {res / num}')


def average_score_l(l_list, course):
    res, num = 0, 0
    for lecture in l_list:
        if course in lecture.courses_attached:
            res += sum(lecture.grades[course])
            num += len(lecture.grades[course])
    print(f'Средняя оценка студентов по {course} {res / num}')


average_score_s(student_list, 'SQL')
average_score_l(lecturer_list, 'Git')


print('\n')
print(stu_1, '\n')
print(stu_2, '\n')
print(lec_1, '\n')
print(lec_2, '\n')
print(stu_1 < stu_2, '\n')
print(lec_1 < lec_2, '\n')
