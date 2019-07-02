'''
该程序旨在抽取出被成功调用的API，且按时间进行排序，最后写入CSV中
'''


import json
import pprint
from operator import itemgetter
import csv

with open(r"E:\PycharmWorkSpace\RansomwareAnalysis\AnalysisReportJsonFile\Cerber\2ba78955416bc13b30574aa7dfab9069.json") as f:
	jf = json.load(f)
	api_timelist = []
	apilist = []
	# print(jf.keys())
	# print("-------------------------------------------------------------------------")
	# print(jf["static"].keys())
	# print("-------------------------------------------------------------------------")
	# pprint.pprint(jf["static"]["pe_imports"])
	print("-------------------------------------------------------------------------")
	# print(jf["behavior"]["processes"])
	for i in range(len(jf["behavior"]["processes"])):
		for j in range(len(jf["behavior"]["processes"][i]["calls"])):
			if(jf["behavior"]["processes"][i]["calls"][j]["status"] == 1):
				temp_dict = {}
				# print(jf["behavior"]["processes"][i]["calls"][j]["api"], jf["behavior"]["processes"][i]["calls"][j]["time"])
				# pprint.pprint(jf["behavior"]["processes"][i]["calls"][j]["arguments"])
				# print(jf["behavior"]["processes"][i]["calls"][j]["return_value"])
				temp_dict["api"] = jf["behavior"]["processes"][i]["calls"][j]["api"]
				temp_dict["time"] = jf["behavior"]["processes"][i]["calls"][j]["time"]
				api_timelist.append(temp_dict)
	# pprint.pprint(api_timelist)
	# print("sort list:------------------------------------------------------------------------------")
	"""
	api_timelist的形式为：api_timelist = [{api: FindFirstFile, time: 1542785768.525373}, {api: FindNextFile, time: 1542785768.525373},.......]
	"""
	#以time值排序
	sorted(api_timelist, key=itemgetter("time"))
	for i in range(len(api_timelist)):
		apilist.append(api_timelist[i]["api"])
	print(apilist)
	# with open(r"E:\PycharmWorkSpace\RansomwareAnalysis\testfunction.csv","a+", newline="") as csvf:
	# 	for lines in apilist:#写入list时换行
	# 		csvf.write(lines+"\n")
	# 	# writer = csv.writer(csvf, dialect="excel")
	# 	# writer.writerow(apilist)