from zhconv import convert
import sys
if len(sys.argv)<2:
				print("this program is Chinese Tradition/Simple convert,example:\nhanc 汉")
param=sys.argv
#print(param)
param.pop(0)
if "-s" in sys.argv:
				param.remove("-s")
				if len(param)>0:
								print(convert(param[0],'zh-hans'))
				#print("将繁体转换为简体")
else:
				if "-t" in param:
								param.remove("-t")
				#print("将简体转换为繁体")
				if len(param)>0:
								print(convert(param[0],'zh-hant'))
