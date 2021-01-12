class Taxi:
	def __init__(self, taxi_name, car_type):
		self.taxi_name = taxi_name
		self.car_type = car_type
		self.taxi_price = 10000

	def discount(self, prescent):
		self.taxi_price -= (self.taxi_price * prescent / 100)
		return self.taxi_price

	def presentation(self):
		return f"name: {self.name}\ntype of car: {self.car_type}\nprice for trip {self.taxi_price}"


class Hotel(Taxi):
	def __init__(self, hotel_name, place, mid_room, lux_room, *args):
		if args:
			Taxi.__init__(self, *args)

		self.hotel_name = hotel_name
		self.place = place
		self.mid_room = mid_room
		self.mr_price = 10000
		self.lux_room = lux_room
		self.lr_price = 20000


	def presentation(self):
		return f"name: {self.name}\nplace: {self.place}\nrooms: mid_room lux_room\nprice: {self.mr_price}(mid) and {self.lr_price}(lux)"

	def booking(self, room_number):
		for room, stat in self.mid_room.items():
			if room == room_number:
				self.mid_room[room_number] = "free"

	def list_all_rooms(self):
		for room, stat in self.mid_room.items():
			print(f"{room} - {stat}")

	def check_room(self, room_number):
		for room, stat in self.mid_room.items():
			if room == room_number:
				if stat == "free":
					return "Its free."
				else:
					return "Its busy."

	def discount(self, prescent):
		self.mr_price -= (self.mr_price * prescent / 100)
		return self.mr_price


class Tour(Hotel, Taxi):
	def __init__(self, tour_name, *args):
		Hotel.__init__(self, *args)
		self.tour_name = tour_name
		self.mid_price = self.mr_price + self.taxi_price
		self.lux_price = self.lr_price + self.taxi_price

	def presentation(self):
		present = f"""
Hello we offer {self.tour_name} tour we have two options mid: {self.mid_price} and lux: {self.lux_price},
which includes transport with {self.taxi_name} company which provides {self.car_type} cars and the price for it is {self.taxi_price},
we will stay at {self.hotel_name} which offers two types of rooms: middle {self.mr_price}, and lux: {self.lr_price}
"""
		return present

rooms = {
	"room1":"free", 
	"room2":"busy", 
	"room3":"busy",
	"room4":"free"
}

lux_rooms = {
	"room1":"free", 
	"room2":"busy",
}

# a = Hotel("My Hotel", "Garni Gexard", rooms, lux_rooms)

# print(a.presentation())

# print(a.check_room("room2"))
# print(a.booking("room2"))
# print(a.check_room("room2"))

# print(a.discount(15))

# a.list_all_rooms()

# tour = Tour("My Tour", "My Hotel", "Garni", rooms, lux_rooms, "Taski", "merc")

# print(tour.presentation())