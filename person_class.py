class Person:
	def __init__(self, name, age, height, gender):
		self.name = name
		self.age = age
		self.height = height
		self.gender = gender

	def greet(self):
		return f"Hi my name is {self.name} and I am {self.age} years old."

	def optimal_weight(self):
		mid = (self.height - 100)
		if self.gender == "female":
			weight = mid - (mid * 10 / 100)
		else:
			weight = mid - (mid * 15 / 100)

		return weight


class Student(Person):
	def __init__(self, name, age, height, gender, grade, fav_subject):
		Person.__init__(self, name, age, height, gender)
		self.grade = grade
		self.fav_subject = fav_subject

	def read_book(self, book):
		try:
			with open(book, "r") as f:
				result = f.read()
				return result
		except Exception:
			pass

	def present(self):
		return f"Hi my name is {self.name}, im at {self.grade} grade and my favourite subject is {self.fav_subject}"


a_book = ""

student1 = Student("Davit", 15, 167, "male", 9, "Math")

print(student1.present())
print(student1.greet())
print(student1.read_book(a_book))
print(student1.optimal_weight())