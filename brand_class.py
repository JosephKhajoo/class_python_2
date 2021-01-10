class Country:
	def __init__(self, name, capital):
		self.name = name
		self.capital = capital

	def present(self):
		return f"{self.name}'s capital is {self.capital}"


class Brand:
	def __init__(self, name, start_hour):
		self.name = name
		self.start_hour = start_hour

	def present(self):
		return f"{self.name} opens at {self.start_hour}"


class Season:
	def __init__(self, name, avg_tmp):
		self.name = name
		self.avg_tmp = avg_tmp

	def present(self):
		return f"Its {self.name} and the average temperature is {self.avg_tmp}"


class Product(Country, Brand, Season):
	def __init__(self, name, type_, price, quantity):
		self.name = name
		self.type_ = type_
		self.price = price
		self.quantity = quantity

	def present(self):
		return f"This is a {self.name}, it costs {self.price} and theres {self.quantity} left."

	def discount(self, prescent):
		self.price = self.price * prescent / 100
		return self.price

	def increase_quantity(self, amount):
		self.quantity += amount
		return self.quantity