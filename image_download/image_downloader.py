import requests
import os


class ImageDownload:
	def __init__(self, image_file):
		self.image_file = image_file
		self.image_list = []
		
		if not os.path.exists("imgs"):
			os.mkdir("imgs")

	def fill_image_list(self):
		with open(self.image_file, "r") as file:
			for i in file:
				self.image_list.append(i.strip())
		return self.image_list


	def download(self):
		self.fill_image_list()
		for link in self.image_list:
			if "?" in link:
				filename = link.split("?")[0].split("/")[-1]
			else:
				filename = link.split("/")[-1]
			
			data = requests.get(link)

			if data.reason.lower() != "ok":
				print(f"[!] Failed to download {filename} due to a '{data.reason}' error")
				continue

			with open(os.path.join("imgs", filename), "wb") as write_file:
				print(f"[*] Downloading `{filename}`")
				write_file.write(data.content)

		print("\n[+] Done.")


img1 = ImageDownload("images.txt")
img1.download()