import json
import yaml


def json_to_text(json_file, text_file):

	with open(json_file, "r") as file_to_conv:
		data = json.load(file_to_conv)

	with open(text_file, "w") as file_to_fill:
		json.dump(data, file_to_fill, indent=2)

	return "Done.\n"


def yaml_to_text(yaml_file, text_file):

	with open(yaml_file, "r") as file_to_conv:
		data = yaml.load(file_to_conv)

	with open(text_file, "w") as file_to_fill:
		yaml.dump(data, file_to_fill, indent=2)

	return "Done.\n"


def yaml_to_json(yaml_file, json_file)
	try:
		with open(yaml_file, "r") as file_to_conv:
			data = yaml.load(file_to_conv)

		with open(json_file, "w") as file_to_fill:
			json.dump(data, file_to_fill, indent=2)

		return "Done.\n"
	except FileNotFoundError:
		print("File {} not found.".format(yaml_file))


def json_to_yaml(json_file, yaml_file):
	try:
		with open(json_file, "r") as file_convert:
			data = json.load(file_convert)

		with open(yaml_file, "w") as file_fill:
			yaml.dump(data, file_fill, sort_keys=False)

		return "Done.\n"
	except FileNotFoundError:
		print("File {} not found".format(json_file))


# json_to_yaml_parser("sample.json", "sample_yaml.yml")
# json_to_text("sample.json", "test.txt")
# yaml_to_json("sample_yaml.yml", "sample.json")
# yaml_to_text("sample_yaml.yml", "test.txt")