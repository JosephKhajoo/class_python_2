import os


def dir_cwd():
	print("\n" + os.getcwd() + "\n")
	for i in os.listdir():
		print(i)

os.mkdir("Dir1")

dir_cwd()

os.chdir("Dir1")
os.mkdir("Dir2")
os.mkdir("Dir3")

dir_cwd()

os.chdir("Dir3")
os.mkdir("Dir4")
os.chdir("..")
os.chdir("..")
dir_cwd()

user_input = input("Wanna Delete all folders?[y/n]: ")

if user_input.lower() == "y":
	print("\nRemoving all directories...")
	
	os.chdir("Dir1")
	os.rmdir("Dir2")
	
	os.chdir("Dir3")
	os.rmdir("Dir4")
	
	os.chdir("..")
	os.rmdir("Dir3")

	os.chdir("..")
	os.rmdir("Dir1")

	dir_cwd()
	print("\nRemoved.")