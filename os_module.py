import os

# cwd = os.getcwd()

# os.mkdir("n_1")

# print(os.listdir())

# os.chdir("n_1")
# os.mkdir("n_2")

# print(os.listdir())

# os.rmdir("n_2")

# os.chdir("..")
# os.rmdir("n_1")

# print(os.listdir())

# os.rename(old, new)

a = open("name.txt", "w")
b = open("name2.txt", "w")
c = open("name3.txt", "w")

for i in os.listdir("."):
	if os.path.isdir(i):
		print("DIR {}".format(i))
	else:
		print("--- {}".format(i))

path = os.path.join(os.getcwd(), "new_one", "jeko2")