class HouseHeating:
	def __init__(self, temp=20):
		self.temp = temp
		self.goal_temp = 27

	def __repr__(self):
		return "This is a heating system created with Python."

	def get_temps(self):
		return self.temp

	def set_temps(self, new_tmp):
		self.goal_temp = new_tmp
		return f"Temprature set to: {self.temp}"

	def goal_satisfy(self):
		if self.temp == self.goal_temp:
			message = f"The goal temprature` {self.goal_temp} is satisfied."
		elif self.temp < self.goal_temp:
			message = f"The temprature is lower than the goal temprature` {self.goal_temp} raise it by {self.goal_temp - self.temp}."
		else:
			message = f"The temprature is higher than the goal temprature` {self.goal_temp} lower it by {self.temp - self.goal_temp}."

		return message


def check_houses(houses):
	norm = 0
	for house in houses:
		if house.get_temps() == house.goal_temp:
			norm += 1

	return f"{norm} houses have normal temprature out of {len(houses_avail)}"


house1 = HouseHeating(15)
house2 = HouseHeating(27)
house3 = HouseHeating(10)
house4 = HouseHeating(27)

houses_avail = [house1, house2, house3, house4]

print(check_houses(houses_avail))