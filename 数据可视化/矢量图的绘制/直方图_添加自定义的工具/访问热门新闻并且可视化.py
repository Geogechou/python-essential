"""
api访问热门的新闻，并可视化
"""
import requests
from operator import itemgetter
import pygal
# 执行API调用并存储响应，该API需要翻墙
url='https://hacker-news.firebaseio.com/v0/topstories.json'
r=requests.get(url)
print("status code: ",r.status_code)

# 处理有关每篇文章的信息
submission_ids=r.json()
submission_dicts=[]
titles,comments=[],[]
for submission_id in submission_ids[:20]:
	#对于每篇文章，都执行一个API调用
	url=('https://hacker-news.firebaseio.com/v0/item/'+
		str(submission_id)+'.json')
	submission_r=requests.get(url)
	print(submission_r.status_code)
	response_dict=submission_r.json()
	
	submission_dict={
	'title':response_dict['title'],
	'xlink':'http://news.ycombinator.com/item?id='+str(submission_id),
	'value':response_dict.get('descendants',0)
	}
	submission_dicts.append(submission_dict)
submission_dicts=sorted(submission_dicts,key=itemgetter('value'),reverse=True)	

for v in submission_dicts:
	titles.append(v['title'])
for submission_dict in submission_dicts:
	print('\nTitle:',submission_dict['title'])
	print('Discussion link: ',submission_dict['xlink'])
# 可视化
chart=pygal.Bar(x_label_rotation=45)
chart.title='Hacker News'
chart.x_labels=titles
chart.add('',submission_dicts)
chart.render_to_file('hacker_news.svg')
chart.render_in_browser()
