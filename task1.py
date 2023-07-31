from collections import deque


class NameDescriptor:
    def __init__(self):
        self.__name = None

    def __get__(self, instance, owner):
        return self.__name

    def __set__(self, instance, value):
        if not all(word.isalpha() for word in value.split()):
            raise ValueError("ФИО должны содержать только буквы.")
        if not all(word.istitle() for word in value.split()):
            raise ValueError("Фамилия, имя и отчество должны начинаться с заглавной буквы.")
        self.__name = value


class Student:
    name = NameDescriptor()

    def __init__(self, name):
        self.name = name
        self._subjects = {}
        with open('subjects.csv', 'r', encoding='utf-8') as file:
            self._valid_subjects = [line.strip() for line in file]

    @property
    def average_grade(self):
        total_grades = [grade for grades in self._subjects.values() for grade in grades['grades']]
        return sum(total_grades) / len(total_grades) if total_grades else 0

    def add_subject(self, subject):
        if subject not in self._valid_subjects:
            raise ValueError(f"Subject '{subject}' is not valid.")
        self._subjects[subject] = {'grades': deque(), 'tests': deque()}

    def add_grade(self, subject, grade):
        if subject not in self._subjects:
            raise ValueError(f"Subject '{subject}' does not exist.")
        if grade < 2 or grade > 5:
            raise ValueError("Grade should be between 2 and 5.")
        self._subjects[subject]['grades'].append(grade)

    def add_test_result(self, subject, result):
        if subject not in self._subjects:
            raise ValueError(f"Subject '{subject}' does not exist.")
        if result < 0 or result > 100:
            raise ValueError("Test result should be between 0 and 100.")
        self._subjects[subject]['tests'].append(result)

    def average_test_score(self, subject):
        if subject not in self._subjects:
            raise ValueError(f"Subject '{subject}' does not exist.")
        tests = self._subjects[subject]['tests']
        return sum(tests) / len(tests) if tests else 0


if __name__ == "__main__":
    student = Student("Сидоренко Альбина Викторовна")
    student.add_subject("Информатика")
    student.add_grade("Информатика", 5)
    student.add_grade("Информатика", 5)
    student.add_test_result("Информатика", 70)
    student.add_test_result("Информатика", 90)
    student.add_subject("Математика")
    student.add_grade("Математика", 4)
    student.add_grade("Математика", 5)
    student.add_test_result("Математика", 60)
    student.add_test_result("Математика", 40)

    print("Средний балл по оценкам:", student.average_grade)
    print("Средний балл по тестам по предмету 'Информатика':", student.average_test_score("Информатика"))
    print("Средний балл по тестам по предмету 'Математика':", student.average_test_score("Математика"))