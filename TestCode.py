'''

用于测试的代码，误删，不可用于其他功能，不可覆盖

'''


import json
import os
import pandas as pd
from pprint import pprint

# with open(r"E:\PycharmWorkSpace\RansomwareAnalysis\AnalysisReportJsonFile\Cerber\0c6fe26a87700ba6d72d023fa3a5376e.json") as f:
# 	jf = json.load(f)
# 	print(jf["static"].keys())
# 	print("-------------------------")
# 	pprint(jf["static"]["pe_imports"])
# 	print("-------------------------")
# 	for pid in range(len(jf["behavior"]["processes"])):
# 		print(jf["behavior"]["processes"][pid]["command_line"])

def GetAPI(filepath):
	list = os.listdir(filepath)
	for i in range(len(list)):
		print()
		path = os.path.join(filepath,list[i])
		if os.path.isfile(path):
			with open(path) as file:
				js = json.load(file)
				for pid in range(len(js["behavior"]["processes"])):
					print(js["behavior"]["processes"][pid]["command_line"])
				print("---------------------------Printed Over!!----------------------------")

if __name__ == "__main__":
	GetAPI(r"E:\PycharmWorkSpace\RansomwareAnalysis\AnalysisReportJsonFile\Cerber")