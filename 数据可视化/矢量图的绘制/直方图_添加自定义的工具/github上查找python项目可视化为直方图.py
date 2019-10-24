
"""
调用API，查找github上python的仓库，可视化为直方图svg
"""
import requests
import pygal
from pygal.style import LightColorizedStyle as Lcs,LightenStyle as Ls
import unittest
# 执行api调用并存储响应
url="https://api.github.com/search/repositories?q=language:python&sort=stars"
r=requests.get(url)
print("Status code:",r.status_code)
#将api响应存储在一个变量中
respose_dict=r.json()
print("Total repositories",respose_dict['total_count'])

#探索有关仓库的信息
repo_dicts=respose_dict['items']
print("repositories returned: ",len(repo_dicts))

names,plot_dicts=[],[]
for repo_dict in repo_dicts:
	names.append(repo_dict['name'])
	if repo_dict['description']:
		plot_dict={
		'value':repo_dict['stargazers_count'],
		'label':repo_dict['description'],
		'xlink':repo_dict['html_url']
		}
		plot_dicts.append(plot_dict)

# 可视化
my_config=pygal.Config()
my_config.x_label_rotation=45
my_config.show_legend=False
my_config.title_font_size=24
my_config.label_font_size=14
my_config.major_label_font_size=18
my_config.truncate_label=15
my_config.show_y_guides=False
my_config.width=1000
my_style=Ls('#333366',base_style=Lcs)
chart=pygal.Bar(my_config,style=my_style)
chart.title="Most starred python project on github"
chart.x_labels=names
chart.add('number',plot_dicts)
chart.render_to_file('python_repos.svg')
chart.render_in_browser()