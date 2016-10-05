import json
import os
import math

#opens the json table
def load_json_data(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath, 'r', encoding = 'utf-8') as file_handler:
        return json.load(file_handler)
      
#returns the "Cells" subdictionary
def cells_dict(data):
	into_list=[]
	for bar in data:
		into_list.append(bar["Cells"])
	return into_list
	
#returns dictionary: {"name_of_bar_1": number_of_seats, ...}
def bar_protocol(register):
	bars={}
	for bar in register:
		name = bar["Name"]
		seats=bar["SeatsCount"]
		bars[name]=seats
	return bars
	
#returns dictionary: {"name_of_bar_1": coordinates, ...}
def all_bars_position(tabl):
	bars_pos={}
	for bar in tabl:
		name = bar["Name"]
		bar_pos=one_bar_position(bar)
		bars_pos[name]=bar_pos
	return bars_pos
	
#function that performs computing for the previous function	
def one_bar_position(new_dict):
	geodata=new_dict["geoData"]
	coord=geodata["coordinates"]
	return coord
	
#returns dictionary: {"name_of_bar_1": vector, ...}
def vector_to_me(coord, my_x, my_y):
	for bar in coord:
		coo=coord[bar]
		bar_x= coo[0]
		bar_y=coo[1]
		coord[bar]=hypotenuse(bar_x, bar_y, my_x, my_y)
	return coord	
	
#function that performs computing for the previous function			
def hypotenuse(x_bar, y_bar, x_my, y_my):
	delta_x=x_bar-x_my
	delta_y=y_bar-y_my
	return math.hypot(delta_x, delta_y)
	
#returns the name of the largest bar
def maximal(string):
    a=max(string, key=lambda i: string[i])
	return a
	
#returns the name of the smallest bar	
def minimal(string):
	b=min(string, key=lambda i: string[i])
	return b

#returns the name of nearest bar	
def nearest_bar(hyp_table):
	c=min(hyp_table, key=lambda i: hyp_table[i])
	return c

if __name__ == '__main__':
	adress=input("Write the adress to \"bars.json\" file: ")   
	table=load_json_data(str(adress))
	print ("\n")
	res=bar_protocol(cells_dict(table))
	print ("The largest bas is: %s" % maximal(res))
	print ("The smallest bar is: %s" % minimal(res))
	print ("\n")
	my_x=input("Give me your Longitude: ")
	my_y=input("Give me your Latitude: ")
	print ("\n")
	bars_pos=all_bars_position(res1)
	vectors=vector_to_me(bars_pos, float(my_x), float(my_y))
	print("The nearest bar to you is: %s" % nearest_bar(vectors))
