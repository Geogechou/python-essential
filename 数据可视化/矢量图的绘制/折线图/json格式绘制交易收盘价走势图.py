"""
用Pygal绘制svg矢量图
同时读取一个json文件
"""
import json
import pygal
import math
# 将数据加载到列表中
filename='btc_close_2017.json'
with open(filename) as f:
	btc_data=json.load(f)
#创建五个列表
dates,months,weeks,weekdays,closes=[],[],[],[],[]
for btc_dict in btc_data:
	dates.append(btc_dict['date'])
	#month,weeks,weekdays只是加进去，最后没有用到
	months.append(int(btc_dict['month']))
	weeks.append(int(btc_dict['week']))
	weekdays.append(btc_dict['weekday'])
	closes.append(int(float(btc_dict['close'])))

#对数变换
close_log=[math.log10(v) for v in closes]
#show_minor_x_labels，让横坐标轴不用显示最小刻度,防止数据密集堆在一起
line_chart=pygal.Line(x_label_rotation=20,show_minor_x_labels=False)
line_chart.title='close-price'
line_chart.x_labels=dates
N=20# x轴坐标每隔20天显示一次
line_chart.x_labels_major=dates[::N]
#把要显示的数据add就好了
line_chart.add('close-price',close_log)
#line_chart.render_to_png('close_price.png')
line_chart.render_to_file('close_price.svg')
