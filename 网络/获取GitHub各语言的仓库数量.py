import requests
import pygal
"""
 检查各种语言的仓库
"""
def find_language(language):
	url="https://api.github.com/search/repositories?q=language:"
	url+=language+"&sort=stars"
	r=requests.get(url)
	print("status code: ",r.status_code)
	#将api响应存储在一个变量中,转化为python字典
	response_dict=r.json()
	return response_dict
program_language=['Golang','c++','php','java','python','JavaScript'
			,'r','c#','Swift','ObjectiveC']

program_language_num=[]			
for v in program_language:
	language_dict=find_language(v)
	program_language_num.append(int(language_dict['total_count']))
#可视化数据
hist=pygal.Bar()
hist.title="github编程语言仓库数量"
hist.x_labels=program_language
hist.x_title="language"
hist.y_title="number"

hist.add('仓库数量',program_language_num)
hist.render_to_file('language_num.svg')
	

	
