"""
矢量图传入字典，当鼠标movin时，会提示字典中的值
"""
import pygal
from pygal.style import LightColorizedStyle as LCS,LightenStyle as LS
my_style=LS('#333366',base_style=LCS)
chart=pygal.Bar(width=500,style=my_style,x_label_rotation=45,show_legend=False)
chart.title="Python Project"
# 设置x轴
chart.x_labels=['httpie','django','flask']

plot_dicts=[
{'value':16101,'label':'Description of httpie'},
{'value':15028,'label':'Description of django'},
{'value':14798,'label':'Description of flask'}
]
chart.add('',plot_dicts)
chart.render_to_file('bar_description.svg')