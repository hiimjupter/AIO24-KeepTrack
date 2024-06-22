from abc import ABC, abstractmethod


class Ward():
    def __init__(self, name: str):
        self.name = name
        self.__people = []

    def add_person(self, person):
        self.__people.append(person)

    def count_doctor(self):
        count = 0
        for person in self.__people:
            # method 1:
            if isinstance(person, Doctor):
                count += 1
            # method 2:
            # if hasattr(person, "specialist"):
            # count += 1
        return f'Number of Doctors in {self.name} is: {count}'

    def sort_age(self):
        self.__people.sort(key=lambda x: x.yob, reverse=True)
        return f'List of __people based on age: {", ".join(f"{person.name} ({person.yob})" for person in self.__people)}'

    def compute_average(self):
        teacher_yob = [
            person.yob for person in self.__people if hasattr(person, 'subject')]
        return f'Average year of birth (teachers): {round(sum(teacher_yob) / len(teacher_yob))}'

    def describe(self):
        description = f'Ward: {self.name}\n'
        for person in self.__people:
            description += person.describe() + '\n'
        return description.strip()


class People(ABC):
    def __init__(self, name: str, yob: int):
        self.name = name
        self.yob = yob

    @abstractmethod
    def describe(self):
        pass


class Student(People):
    def __init__(self, name: str, yob: int, grade: str):
        super().__init__(name, yob)
        self.grade = grade

    def describe(self):
        return f'Student - Name: {self.name} - YoB: {self.yob} - Grade: {self.grade}'


class Teacher(People):
    def __init__(self, name: str, yob: int, subject: str):
        super().__init__(name, yob)
        self.subject = subject

    def describe(self):
        return f'Teacher - Name: {self.name} - YoB: {self.yob} - Subject: {self.subject}'


class Doctor(People):
    def __init__(self, name, yob, specialist):
        super().__init__(name, yob)
        self.specialist = specialist

    def describe(self):
        return f'Doctor - Name: {self.name} - YoB: {self.yob} - Specialist: {self.specialist}'


# Test case
student1 = Student("Student A", 2010, "7")
# print(student1.describe())

teacher1 = Teacher("Teacher A", 1969, "Math")
teacher2 = Teacher("Teacher B", 1995, "History")
# print(teacher1.describe())

doctor1 = Doctor("Docter A", 1945, "Endocrinologists")
doctor2 = Doctor("Doctor B", 1975, "Cardiologists")
# print(doctor1.describe())

ward1 = Ward("Ward 1")
ward1.add_person(student1)
ward1.add_person(teacher1)
ward1.add_person(teacher2)
ward1.add_person(doctor1)
ward1.add_person(doctor2)
print(ward1.describe())

print(ward1.count_doctor())

print(ward1.sort_age())

print(ward1.compute_average())
