import json
import os
import math

def load_json(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath, 'r', encoding = 'utf-8') as file_handler:
        return json.load(file_handler)
      	
def return_largest(data):
    return max(data, key=lambda i: i["Cells"].get("SeatsCount")).get("Cells").get("Name")
    
def return_smallest(data):
    return min(data, key=lambda i: i["Cells"].get("SeatsCount")).get("Cells").get("Name")

def return_closest(data):
    return min(data, key=lambda i: calculate_vector(get_bar_coordinate(i), my_longitude, my_latitude)) \
    .get("Cells").get("Name")

def calculate_vector(bar_coordinate, my_longitude, my_latitude):
	delta_x=float(bar_coordinate[0])-float(my_longitude)
	delta_y=float(bar_coordinate[1])-float(my_latitude)
	return math.hypot(delta_x, delta_y)	

def get_bar_coordinate(data):
	return data["Cells"]["geoData"]["coordinates"]

if __name__=='__main__':
	adress=input("Write the adress to \"bars.json\" file: ")
	opened_json=load_json(adress)
	print ("\n")
	print ("The largest bas is: %s" % return_largest(opened_json))
	print ("The smallest bar is: %s" % return_smallest(opened_json))
	print ("\n")
	my_longitude=input("Give me your Longitude: ")
	my_latitude=input("Give me your Latitude: ")
	print ("\n")
	print("The nearest bar to you is: %s" % return_closest(opened_json))
