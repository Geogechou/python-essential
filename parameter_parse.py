import argparse
# 使用help的提示语句
description = "you should add those parameter"
parser = argparse.ArgumentParser(description=description)
# 使用的时候用python parameter_parse.py -n 2 --epochs 5
parser.add_argument("-n",help="number")
parser.add_argument("--epochs",help="epochs")
args = parser.parse_args()
# 读取参数
print("n:",args.n)
print("epochs:",args.epochs)
