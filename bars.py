import json
import os

def load_data(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath, mode ='r', encoding = 'utf-8') as file_handler:
        return json.load(file_handler)


def get_biggest_bar(data):
    temp_big = None
    for bar in data:
    	if temp_big is None or temp_big["Cells"].get("SeatsCount")<bar["Cells"].get("SeatsCount"):
    		temp_big = bar
    return temp_big


def get_smallest_bar(data):
    temp_small = None
    for bar in data:
    	if temp_small is None or temp_small["Cells"].get("SeatsCount")>=bar["Cells"].get("SeatsCount"):
    		temp_small = bar
    return temp_small


def get_closest_bar(data, longitude, latitude):
    temp_closest = None
    temp_distance = None
    for bar in data:
    	if temp_closest is None or temp_distance>calculate_distance(bar["Cells"].get("geoData").get("coordinates"), [longitude, latitude]):
    		temp_closest = bar
    		temp_distance = calculate_distance(temp_closest["Cells"].get("geoData").get("coordinates"), [longitude, latitude])
    return temp_closest


def calculate_distance(point_one, point_two):
	return ((point_one[0]-point_two[0])**2+(point_one[1]-point_two[1])**2)**(1/2)

if __name__ == '__main__':
	data_location = input("ВВедите путь к файлу json: ")
	data = load_data(data_location)
	if data is None:
		print("Не удалось открыть файл")
		exit()
	while True:
		key = int(input("ВВедите: \n\t1-Для показа самого большого бара\n\t2-Для показа самого маленького бара\n\t3-Для показа ближайшего бара\n\t0-Выход\n"))
		if key == 1:
   			print(get_biggest_bar(data))
		elif key == 2:
   			print(get_smallest_bar(data))
		elif key==3:
   			print("Введите ваши координаты:")
   			my_location = [float(input()), float(input())]
   			print(get_closest_bar(data,my_location[0],my_location[1]))
		elif key==0:
   			exit()
