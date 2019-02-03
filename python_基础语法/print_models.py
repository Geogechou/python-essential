def make_car(brand_name,kind_name,color,**other_info):
	car_info={}
	car_info["brand_name"]=brand_name
	car_info["kind_name"]=kind_name
	car_info["color"]=color
	for k,v in other_info.items():
		car_info[k]=v
	return car_info	
